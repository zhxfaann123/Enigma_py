
class Alphabet:
    """
    The alphabet of encodable characters. Each character has two presentations:
    the raw character of its index(started with 0).
    """
    def __init__(self, *self_defined_alphabet):
        self.alphabetString = self_defined_alphabet[0]

    def size(self):
        return len(self.alphabetString)

    def contains(self, item):
        return self.alphabetString.find(item) != -1

    def toChar(self, index):
        assert 0 <= index < self.size()
        return self.alphabetString[index]

    def toInt(self, char):
        assert char in self.alphabetString
        return self.alphabetString.find(char)




