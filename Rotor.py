from Alphabet import Alphabet
from Permutation import Permutation


class Rotor:
    def __init__(self, name, perm: Permutation):
        self._name = name
        self._perm = perm
        self._cPos = 'a'
        self._iPos = 1

    def name(self):
        return self._name

    @staticmethod
    def rotates(self):
        return False

    @staticmethod
    def reflecting(self):
        return False

    @staticmethod
    def setting(self):
        return 0

    def set(self, cposn):
        try:
            iposn = self.alphabet_string().index(cposn)
        except ValueError:
            raise Exception("The character is not in the alphabet")
        self._cPos = cposn
        self._iPos = iposn

    def convertForward(self, p):
        p = self._perm.warp(p)
        image = self._perm.permute(p)
        return image

    def convertBackward(self, e):
        e = self._perm.warp(e)
        preimage = self._perm.invert(e)
        return preimage

    @staticmethod
    def atNotch(self):
        return False

    def int2char(self, x):
        return self._perm.alphabet().toChar(x)

    def char2int(self, x):
        return self._perm.alphabet().toInt(x)

    def alphabet_size(self):
        return self._perm.size()

    def alphabet_string(self):
        return self._perm.alphabet().alphabetString

    def permute(self, x):
        return self._perm.permute(x)

    def invert(self, x):
        return self._perm.invert(x)

    def warp(self, x):
        return self._perm.warp(x)