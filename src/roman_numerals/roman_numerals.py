from bisect import bisect_left
from copy import copy

"""
Usually the code kata just consider the basic conversion which doesn't take minus abbreviation into account (IX, CD)
The idea of this algorithm is to use falling and raising edges

    M C M L X X X I V
     \ / \
           \
             - - 
                 \ /   
"""

ROMAN_NUMERALS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
ROMAN_VALUES = [1, 5, 10, 50, 100, 500, 1000]
RAMON_NUMBERS = dict(zip(ROMAN_NUMERALS, (ROMAN_VALUES)))
ROMAN_CARDINAL_VALUE = dict(zip(ROMAN_NUMERALS, enumerate(ROMAN_VALUES)))

NORMALISATION = {'BASE', 'NORMAL', 'SHORT_NORMAL', 'OPTIMIZED'}


def get_numeral_iterator(numeral):
    def inner():
        if numeral_l:
            character = numeral_l.pop(0)
            cardinality, arabic_value = ROMAN_CARDINAL_VALUE[character]
            return character, cardinality, arabic_value
        else:
            return ()

    numeral_l = list(numeral)

    return inner


def calc_falling(num_iter, rn_res):
    num_sum = copy(rn_res[2])
    prev_card = copy(rn_res[1])

    rn_res = num_iter()

    while rn_res:
        rn, card, value = rn_res
        if card == prev_card:
            num_sum += value
        elif card > prev_card:  # stop signal for minus sequence
            return value - num_sum, card
        elif card < prev_card:
            part_sum, prev_card = calc_falling(num_iter, rn_res)
            return part_sum + num_sum, prev_card

        rn_res = num_iter()

    return num_sum, prev_card


def convert_to_arabic(numeral):
    num_iter = get_numeral_iterator(numeral)
    roman_digit = num_iter()

    prev_card = -1
    num_sum = 0

    while roman_digit:
        rn, card, value = roman_digit

        if card == prev_card or prev_card == -1:
            num_sum, prev_card = num_sum + value, card
        elif card > prev_card:  # signal to stop sequence
            num_sum, prev_card = value - num_sum, card
        elif card < prev_card:
            part_sum, prev_card = calc_falling(num_iter, roman_digit)
            num_sum += part_sum

        roman_digit = num_iter()

    return num_sum


def convert_to_roman(number: str, normalisation=None):
    if normalisation == 'BASE' or None:
        pass
    pass


def convert_to_roman_base(number: int):
    numeral = ''
    while True:
        idx = min(bisect_left(ROMAN_VALUES, number), 6)
        if ROMAN_VALUES[idx] > number:
            idx -= 1

        numeral += ROMAN_NUMERALS[idx]
        number -= ROMAN_VALUES[idx]
        if number == 0:
            break
    return numeral
