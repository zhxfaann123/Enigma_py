from Rotor import Rotor


class FixedRotor(Rotor):
    def __init__(self, name, perm):
        super().__init__(name, perm)

    def set(self, posn):
        if posn >= len(super().alphabet_string()):
            raise Exception("The setting is out of the range!")
        else:
            super()._iPos = posn
            super()._cPos = super().int2char(posn)

    def convertForward(self, p):
        p += super()._iPos
        p = super().warp(p)
        image = super().permute(p)
        image -= super()._iPos
        image = super().warp(image)
        return image

    def convertBackward(self, e):
        e += super()._iPos
        e = super().warp(e)
        preimage = super().permute(e)
        preimage = super().warp(preimage)
        return preimage

