import unittest
from roman_numerals import convert_to_roman_base, replace_4_clusters
from roman_numerals.roman_numerals import replace_3_clusters, convert_to_roman_short


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

    def test_replace_9_cluster(self):
        res = replace_4_clusters('VIIII')
        self.assertEqual('IX', res)

        res = replace_4_clusters('VIIIIVIIII')
        self.assertEqual('IXIX', res)

        res = convert_to_roman_base(1984)
        res = replace_4_clusters(res)
        self.assertEqual('MCMLXXXIIII', res)

    def test_replace_3_cluster(self):
        res = replace_3_clusters('VIII')
        self.assertEqual('IIX', res)

        res = replace_3_clusters('VIIIVIII')
        self.assertEqual('IIXIIX', res)

        res = convert_to_roman_short(1984)
        self.assertEqual('MCMXXCIV', res)

if __name__ == '__main__':
    unittest.main()
