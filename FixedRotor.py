from Rotor import Rotor


class FixedRotor(Rotor):
    def __init__(self, name, perm):
        super().__init__(name, perm)

    def set(self, c_posn: str):
        i_posn = super().char2int(c_posn)
        if i_posn >= len(super().alphabet_string()):
            raise Exception("The setting is out of the range!")
        else:
            self._cPos = c_posn
            self._iPos = i_posn

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

