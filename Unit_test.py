import unittest
from io import StringIO
from _io import TextIOWrapper


def test_io_func(file_d: TextIOWrapper):
    print(file_d.read())


class MyTestCase(unittest.TestCase):
    def test_string_reader(self):
        test_str = "ABC"
        str_reader = StringIO(test_str)
        print(str_reader.read(1))
        print(str_reader.read(1))
        print(str_reader.read(1))
        a = str_reader.read(1)
        a = 1

    def test_string_idx(self):
        str = "ABC"
        print(str[-1])

    def test_range(self):
        for i in range(5, 0, -1):
            print(i)

    def test_list_to_str(self):
        list = ['a', 'b', 'c']

    def test_string_features(self):
        string = "abc"
        for c in string:
            print(c)

    def test_line_file(self):
        file = open("test/output/output.txt", 'r')
        for line in file:
            for word in line.split():
                print(word)

    def test_file_read(self):
        file = open("test/output/output.txt", 'r')
        print(file.readline())
        print(file.readline())
        print(file.readline() == "")

    def test_get_class(self):
        file = open("test/output/output.txt", 'r')
        print(type(file))

    def test_textIO(self):
        file = open("test/output/output.txt", 'r')
        test_io_func(file)
        file.close()

    def test_negate(self):
        if not "":
            print("nothing")

    def test_len_str(self):
        str = "abc\n"
        print(len(str))


if __name__ == '__main__':
    unittest.main()
