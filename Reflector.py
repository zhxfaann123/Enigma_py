from Rotor import Rotor


class Reflector(Rotor):
    def __init__(self, name, perm):
        super().__init__(name, perm)

    def set(self, posn):
        if posn != 0:
            raise Exception("reflector has only default position")

    def reflecting(self):
        return True
