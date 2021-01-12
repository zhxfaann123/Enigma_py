from Alphabet import Alphabet
from Reflector import Reflector
from Permutation import Permutation
from Utils import *


class Machine:
    """
    The Enigma Machine, consisting several rotors(Reflector/FixRotor/MovingRotor)
    """
    def __init__(self, alphabet: Alphabet, num_rotors: int, num_pawls: int, rotors: list):
        self._alphabet = alphabet
        self._num_rotors = num_rotors
        self._num_pawls = num_pawls
        self._all_rotors = rotors
        self._inserted_rotors = []
        self._plugboard = Permutation("", self._alphabet)

    def convert_char(self, c: int):
        self.machine_advance()
        output = self._plugboard.permute(c)
        for i in range(self._num_rotors - 1, -1, -1):
            output = self._inserted_rotors[i].convertForward(output)
        for i in range(1, self._num_rotors):
            output = self._inserted_rotors[i].convertBackward(output)
        output = self._plugboard.permute(output)
        return output

    def convert_str(self, msg: str):
        coded_msg = ""
        for ch in msg:
            if ch == '\n':
                return coded_msg
            if ch == ' ':
                continue
            else:
                print(self.get_current_setting())
                idx_ch = self._alphabet.toInt(ch)
                coded_idx_ch = self.convert_char(idx_ch)
                coded_msg += self._alphabet.toChar(coded_idx_ch)
        return coded_msg

    def check_rotor_configure(self):
        if not self._inserted_rotors:
            raise Exception("No rotor is inserted into the machine")
        if not isinstance(self._inserted_rotors[0], Reflector):
            raise Exception("The leftmost rotor isn't the reflector")
        for i in range(self._num_rotors - self._num_pawls):
            if self._inserted_rotors[i].rotates():
                raise Exception("One leftmost rotor can rotate")
        for i in range(self._num_rotors - self._num_pawls, self.num_rotors()):
            if not self._inserted_rotors[i].rotates():
                raise Exception("One rightmost rotor can't rotate")

    def insert_one_rotor(self, rotor_name: str):
        for rotor in self._all_rotors:
            if rotor.name() == rotor_name:
                self._inserted_rotors.append(rotor)

    def insert_all_rotors(self, rotor_name_list: list):
        for rotor_name in rotor_name_list:
            self.insert_one_rotor(rotor_name)

        self.check_rotor_configure()

    def num_rotors(self):
        return self._num_rotors

    def num_pawls(self):
        return self._num_pawls

    def machine_advance(self):
        idx_rotor_advance = []
        for i in range(self._num_rotors - self._num_pawls, self._num_rotors):
            if i == self._num_rotors - 1 \
                    or self._inserted_rotors[i + 1].atNotch() \
                    or (self._inserted_rotors[i].atNotch() and (i != self._num_rotors - self._num_pawls)):
                idx_rotor_advance.append(i)

        for idx in idx_rotor_advance:
            self._inserted_rotors[idx].advance()

    def set_rotors(self, setting: str):
        if not len(setting) == self._num_rotors - 1:
            raise Exception("The number of rotors to be set should be # of rotors - 1(all rotors excluding reflector)")
        else:
            for i in range(1, self._num_rotors):
                self._inserted_rotors[i].set(setting[i - 1])

    def set_plugboard(self, cycles: str):
        self._plugboard = Permutation(cycles, self._alphabet)

    def get_current_setting(self):
        machine_setting = ""
        for i in range(1, self._num_rotors):
            machine_setting += self._alphabet.toChar(self._inserted_rotors[i].setting())
        return machine_setting

    def reset_rotors(self):
        self._inserted_rotors = []

    def reset_plugboard(self):
        self._plugboard = Permutation("", self._alphabet)

    def get_rotors(self):
        return self._inserted_rotors

