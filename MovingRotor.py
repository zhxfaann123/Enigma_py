from Rotor import Rotor


class MovingRotor(Rotor):
    def __init__(self, name, perm, notches):
        super().__init__(name, perm)
        self._notches = notches

    @staticmethod
    def rotates():
        return True

    def atNotch(self):
        return self._cPos in self._notches

    def advance(self):
        if self._iPos == super().alphabet_size() - 1:
            self._iPos = 0
        else:
            self._iPos += 1
        self._cPos = super().int2char(self._iPos)

    def set(self, input):
        if isinstance(input, int):
            if input > super().alphabet_size():
                raise Exception("The input is not in the range of 0~size-1.")
            else:
                self._iPos = input
                self._cPos = super().int2char(self._iPos)
        elif isinstance(input, str):
            if input not in super().alphabet_string():
                raise Exception("the character is not in the alphabet.")
            else:
                self._cPos = input
                self._iPos = super().char2int(self._cPos)

    def convertForward(self, p):
        p += self._iPos
        p = super().warp(p)
        image = super().permute(p)
        image -= self._iPos
        image = super().warp(image)
        return image

    def convertBackward(self, e):
        e += self._iPos
        e = super().warp(e)
        preimage = super().invert(e)
        preimage -= self._iPos
        preimage = super().warp(preimage)
        return preimage

    def setting(self):
        return self._iPos


