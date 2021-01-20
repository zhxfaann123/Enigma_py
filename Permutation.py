from io import StringIO
from Alphabet import Alphabet
from Utils import Default_Alphabet_String


class Permutation:
    def __init__(self, cycles, alphabet: Alphabet):
        self._alphabet = alphabet
        self._cycles = []
        self._char_perm = list(alphabet.alphabetString)
        self._int_perm = [i for i in range(self._alphabet.size())]

        string_reader = StringIO(cycles)
        while True:
            char = string_reader.read(1)
            if char == '':
                break
            elif char == ' ':
                continue
            elif char != '(':
                raise Exception("Invalid input of cycles, which is supposed to start with '('")
            else:
                cyclech = ""
                while True:
                    ch = string_reader.read(1)
                    if ch == "":
                        raise Exception("reach null while expect ')' or a char")
                    elif ch == ")":
                        self._cycles.append(cyclech)
                        break
                    else:
                        cyclech += ch

        string_reader.close()
        self.cycles2perm(self._cycles)
        self.cast_perm_char2int()

    def cycles2perm(self, cycles):
        for cycle in cycles:
            if len(cycle) == 1:
                char = cycle[0]
                idx_char = self._alphabet.toInt(char)
                self._char_perm[idx_char] = char
            else:
                for char in cycle:
                    idx_cycle_char = cycle.index(char)
                    # idx_alpha_char = self._alphabet.toInt(char)
                    pred_char = cycle[idx_cycle_char - 1]
                    idx_alpha_pred_char = self._alphabet.toInt(pred_char)
                    self._char_perm[idx_alpha_pred_char] = char

    def cast_perm_char2int(self):
        for char in self._char_perm:
            idx = self._char_perm.index(char)
            self._int_perm[idx] = self._alphabet.toInt(char)

    def permute(self, input):
        if isinstance(input, int):
            return self._int_perm[input]
        if isinstance(input, str):
            idx_alpha = self._alphabet.toInt(input)
            return self._char_perm[idx_alpha]

    def invert(self, input):
        if isinstance(input, int):
            return self._int_perm.index(input)
        if isinstance(input, str):
            idx_alpha = self._alphabet.toInt(input)
            return self._alphabet.toChar(self.invert(idx_alpha))

    def size(self):
        return self._alphabet.size()

    def warp(self, p):
        r = p % self.size()
        if r < 0:
            r += self.size()
        return r

    def alphabet(self):
        return self._alphabet









