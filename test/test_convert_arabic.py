import unittest
from roman_numerals import convert_to_roman_base


class ToRomanConversions(unittest.TestCase):
    def test_convert_to_roman_10(self):

        res = convert_to_roman_base(10)
        print (res)

    def test_convert_to_roman_14(self):

        res = convert_to_roman_base(14)
        print (res)

    def test_convert_to_roman_1984(self):

        res = convert_to_roman_base(1984)
        print (res)

if __name__ == '__main__':
    unittest.main()
