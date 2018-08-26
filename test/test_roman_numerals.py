import unittest

from src.roman_numerals.roman_numerals import ROMAN_NUMERALS, ROMAN_VALUES, get_numeral_iterator, \
    convert_to_arabic


class MyTestCase(unittest.TestCase):



    def test_roman_numeral(self):
        for c in ROMAN_NUMERALS:
            print(c)
        self.assertEqual(True, True)

    def test_num_card_val(self):
        d = dict(zip(ROMAN_NUMERALS, enumerate(ROMAN_VALUES)))
        for rn, value_t in d.items():
            print(rn, value_t)
        pass

    def test_zip_numerals(self):
        d = dict(zip(ROMAN_NUMERALS, ROMAN_VALUES))

        for rn, val in d.items():
            print(rn, val)

    def test_numeral_iter(self):
        f = get_numeral_iterator('IIX')
        rnc = f()
        while rnc:
            print(rnc)
            rnc = f()

    # def test_MCCMLXXXIV(self):
    #     res = signal_trigger('MCCMLXXXIV')
    #     self.assertEqual(1884, res)
    #
    # def test_MCMLXXXIV(self):
    #     res = signal_trigger('MCMLXXXIV')
    #     self.assertEqual(1984, res)

    def test_I(self):
        res = convert_to_arabic('I')
        self.assertEqual(1, res)

    def test_II(self):
        res = convert_to_arabic('II')
        self.assertEqual(2, res)

    def test_III(self):
        res = convert_to_arabic('III')
        self.assertEqual(3, res)

    def test_IV(self):
        res = convert_to_arabic('IV')
        self.assertEqual(4, res)

    def test_V(self):
        res = convert_to_arabic('V')
        self.assertEqual(5, res)

    def test_VI(self):
        res = convert_to_arabic('VI')
        self.assertEqual(6, res)

    def test_VII(self):
        res = convert_to_arabic('VII')
        self.assertEqual(7, res)

    def test_VIII(self):
        res = convert_to_arabic('VIII')
        self.assertEqual(8, res)

    def test_IX(self):
        res = convert_to_arabic('IX')
        self.assertEqual(9, res)

    def test_X(self):
        res = convert_to_arabic('X')
        self.assertEqual(10, res)

    def test_XI(self):
        res = convert_to_arabic('XI')
        self.assertEqual(11, res)

    def test_XII(self):
        res = convert_to_arabic('XII')
        self.assertEqual(12, res)

    def test_XIII(self):
        res = convert_to_arabic('XIII')
        self.assertEqual(13, res)

    def test_XIV(self):
        res = convert_to_arabic('XIV')
        self.assertEqual(14, res)

    def test_XV(self):
        res = convert_to_arabic('XV')
        self.assertEqual(15, res)

    def test_XVI(self):
        res = convert_to_arabic('XVI')
        self.assertEqual(16, res)

    def test_XVII(self):
        res = convert_to_arabic('XVII')
        self.assertEqual(17, res)

    def test_XVIII(self):
        res = convert_to_arabic('XVIII')
        self.assertEqual(18, res)

    def test_XIX(self):
        res = convert_to_arabic('XIX')
        self.assertEqual(19, res)

    def test_XX(self):
        res = convert_to_arabic('XX')
        self.assertEqual(20, res)

    def test_XXI(self):
        res = convert_to_arabic('XXI')
        self.assertEqual(21, res)

    def test_XXII(self):
        res = convert_to_arabic('XXII')
        self.assertEqual(22, res)

    def test_XXIII(self):
        res = convert_to_arabic('XXIII')
        self.assertEqual(23, res)

    def test_XXIV(self):
        res = convert_to_arabic('XXIV')
        self.assertEqual(24, res)

    def test_XXV(self):
        res = convert_to_arabic('XXV')
        self.assertEqual(25, res)

    def test_XXVI(self):
        res = convert_to_arabic('XXVI')
        self.assertEqual(26, res)

    def test_XXVII(self):
        res = convert_to_arabic('XXVII')
        self.assertEqual(27, res)

    def test_XXVIII(self):
        res = convert_to_arabic('XXVIII')
        self.assertEqual(28, res)

    def test_XXIX(self):
        res = convert_to_arabic('XXIX')
        self.assertEqual(29, res)

    def test_XXX(self):
        res = convert_to_arabic('XXX')
        self.assertEqual(30, res)

    def test_XXXI(self):
        res = convert_to_arabic('XXXI')
        self.assertEqual(31, res)

    def test_XXXII(self):
        res = convert_to_arabic('XXXII')
        self.assertEqual(32, res)

    def test_XXXIII(self):
        res = convert_to_arabic('XXXIII')
        self.assertEqual(33, res)

    def test_XXXIV(self):
        res = convert_to_arabic('XXXIV')
        self.assertEqual(34, res)

    def test_XXXV(self):
        res = convert_to_arabic('XXXV')
        self.assertEqual(35, res)

    def test_XXXVI(self):
        res = convert_to_arabic('XXXVI')
        self.assertEqual(36, res)

    def test_XXXVII(self):
        res = convert_to_arabic('XXXVII')
        self.assertEqual(37, res)

    def test_XXXVIII(self):
        res = convert_to_arabic('XXXVIII')
        self.assertEqual(38, res)

    def test_XXXIX(self):
        res = convert_to_arabic('XXXIX')
        self.assertEqual(39, res)

    def test_XL(self):
        res = convert_to_arabic('XL')
        self.assertEqual(40, res)

    def test_XLI(self):
        res = convert_to_arabic('XLI')
        self.assertEqual(41, res)

    def test_XLII(self):
        res = convert_to_arabic('XLII')
        self.assertEqual(42, res)

    def test_XLIII(self):
        res = convert_to_arabic('XLIII')
        self.assertEqual(43, res)

    def test_XLIV(self):
        res = convert_to_arabic('XLIV')
        self.assertEqual(44, res)

    def test_XLV(self):
        res = convert_to_arabic('XLV')
        self.assertEqual(45, res)

    def test_XLVI(self):
        res = convert_to_arabic('XLVI')
        self.assertEqual(46, res)

    def test_XLVII(self):
        res = convert_to_arabic('XLVII')
        self.assertEqual(47, res)

    def test_XLVIII(self):
        res = convert_to_arabic('XLVIII')
        self.assertEqual(48, res)

    def test_XLIX(self):
        res = convert_to_arabic('XLIX')
        self.assertEqual(49, res)

    def test_L(self):
        res = convert_to_arabic('L')
        self.assertEqual(50, res)

    def test_LI(self):
        res = convert_to_arabic('LI')
        self.assertEqual(51, res)

    def test_LII(self):
        res = convert_to_arabic('LII')
        self.assertEqual(52, res)

    def test_LIII(self):
        res = convert_to_arabic('LIII')
        self.assertEqual(53, res)

    def test_LIV(self):
        res = convert_to_arabic('LIV')
        self.assertEqual(54, res)

    def test_LV(self):
        res = convert_to_arabic('LV')
        self.assertEqual(55, res)

    def test_LVI(self):
        res = convert_to_arabic('LVI')
        self.assertEqual(56, res)

    def test_LVII(self):
        res = convert_to_arabic('LVII')
        self.assertEqual(57, res)

    def test_LVIII(self):
        res = convert_to_arabic('LVIII')
        self.assertEqual(58, res)

    def test_LIX(self):
        res = convert_to_arabic('LIX')
        self.assertEqual(59, res)

    def test_LX(self):
        res = convert_to_arabic('LX')
        self.assertEqual(60, res)

    def test_LXI(self):
        res = convert_to_arabic('LXI')
        self.assertEqual(61, res)

    def test_LXII(self):
        res = convert_to_arabic('LXII')
        self.assertEqual(62, res)

    def test_LXIII(self):
        res = convert_to_arabic('LXIII')
        self.assertEqual(63, res)

    def test_LXIV(self):
        res = convert_to_arabic('LXIV')
        self.assertEqual(64, res)

    def test_LXV(self):
        res = convert_to_arabic('LXV')
        self.assertEqual(65, res)

    def test_LXVI(self):
        res = convert_to_arabic('LXVI')
        self.assertEqual(66, res)

    def test_LXVII(self):
        res = convert_to_arabic('LXVII')
        self.assertEqual(67, res)

    def test_LXVIII(self):
        res = convert_to_arabic('LXVIII')
        self.assertEqual(68, res)

    def test_LXIX(self):
        res = convert_to_arabic('LXIX')
        self.assertEqual(69, res)

    def test_LXX(self):
        res = convert_to_arabic('LXX')
        self.assertEqual(70, res)

    def test_LXXI(self):
        res = convert_to_arabic('LXXI')
        self.assertEqual(71, res)

    def test_LXXII(self):
        res = convert_to_arabic('LXXII')
        self.assertEqual(72, res)

    def test_LXXIII(self):
        res = convert_to_arabic('LXXIII')
        self.assertEqual(73, res)

    def test_LXXIV(self):
        res = convert_to_arabic('LXXIV')
        self.assertEqual(74, res)

    def test_LXXV(self):
        res = convert_to_arabic('LXXV')
        self.assertEqual(75, res)

    def test_LXXVI(self):
        res = convert_to_arabic('LXXVI')
        self.assertEqual(76, res)

    def test_LXXVII(self):
        res = convert_to_arabic('LXXVII')
        self.assertEqual(77, res)

    def test_LXXVIII(self):
        res = convert_to_arabic('LXXVIII')
        self.assertEqual(78, res)

    def test_LXXIX(self):
        res = convert_to_arabic('LXXIX')
        self.assertEqual(79, res)

    def test_LXXX(self):
        res = convert_to_arabic('LXXX')
        self.assertEqual(80, res)

    def test_LXXXI(self):
        res = convert_to_arabic('LXXXI')
        self.assertEqual(81, res)

    def test_LXXXII(self):
        res = convert_to_arabic('LXXXII')
        self.assertEqual(82, res)

    def test_LXXXIII(self):
        res = convert_to_arabic('LXXXIII')
        self.assertEqual(83, res)

    def test_LXXXIV(self):
        res = convert_to_arabic('LXXXIV')
        self.assertEqual(84, res)

    def test_LXXXV(self):
        res = convert_to_arabic('LXXXV')
        self.assertEqual(85, res)

    def test_LXXXVI(self):
        res = convert_to_arabic('LXXXVI')
        self.assertEqual(86, res)

    def test_LXXXVII(self):
        res = convert_to_arabic('LXXXVII')
        self.assertEqual(87, res)

    def test_LXXXVIII(self):
        res = convert_to_arabic('LXXXVIII')
        self.assertEqual(88, res)

    def test_LXXXIX(self):
        res = convert_to_arabic('LXXXIX')
        self.assertEqual(89, res)

    def test_XC(self):
        res = convert_to_arabic('XC')
        self.assertEqual(90, res)

    def test_XCI(self):
        res = convert_to_arabic('XCI')
        self.assertEqual(91, res)

    def test_XCII(self):
        res = convert_to_arabic('XCII')
        self.assertEqual(92, res)

    def test_XCIII(self):
        res = convert_to_arabic('XCIII')
        self.assertEqual(93, res)

    def test_XCIV(self):
        res = convert_to_arabic('XCIV')
        self.assertEqual(94, res)

    def test_XCV(self):
        res = convert_to_arabic('XCV')
        self.assertEqual(95, res)

    def test_XCVI(self):
        res = convert_to_arabic('XCVI')
        self.assertEqual(96, res)

    def test_XCVII(self):
        res = convert_to_arabic('XCVII')
        self.assertEqual(97, res)

    def test_XCVIII(self):
        res = convert_to_arabic('XCVIII')
        self.assertEqual(98, res)

    def test_XCIX(self):
        res = convert_to_arabic('XCIX')
        self.assertEqual(99, res)

    def test_C(self):
        res = convert_to_arabic('C')
        self.assertEqual(100, res)

    def test_CI(self):
        res = convert_to_arabic('CI')
        self.assertEqual(101, res)

    def test_CII(self):
        res = convert_to_arabic('CII')
        self.assertEqual(102, res)

    def test_CIII(self):
        res = convert_to_arabic('CIII')
        self.assertEqual(103, res)

    def test_CIV(self):
        res = convert_to_arabic('CIV')
        self.assertEqual(104, res)

    def test_CV(self):
        res = convert_to_arabic('CV')
        self.assertEqual(105, res)

    def test_CVI(self):
        res = convert_to_arabic('CVI')
        self.assertEqual(106, res)

    def test_CVII(self):
        res = convert_to_arabic('CVII')
        self.assertEqual(107, res)

    def test_CVIII(self):
        res = convert_to_arabic('CVIII')
        self.assertEqual(108, res)

    def test_CIX(self):
        res = convert_to_arabic('CIX')
        self.assertEqual(109, res)

    def test_CX(self):
        res = convert_to_arabic('CX')
        self.assertEqual(110, res)

    def test_CXI(self):
        res = convert_to_arabic('CXI')
        self.assertEqual(111, res)

    def test_CXII(self):
        res = convert_to_arabic('CXII')
        self.assertEqual(112, res)

    def test_CXIII(self):
        res = convert_to_arabic('CXIII')
        self.assertEqual(113, res)

    def test_CXIV(self):
        res = convert_to_arabic('CXIV')
        self.assertEqual(114, res)

    def test_CXV(self):
        res = convert_to_arabic('CXV')
        self.assertEqual(115, res)

    def test_CXVI(self):
        res = convert_to_arabic('CXVI')
        self.assertEqual(116, res)

    def test_CXVII(self):
        res = convert_to_arabic('CXVII')
        self.assertEqual(117, res)

    def test_CXVIII(self):
        res = convert_to_arabic('CXVIII')
        self.assertEqual(118, res)

    def test_CXIX(self):
        res = convert_to_arabic('CXIX')
        self.assertEqual(119, res)

    def test_CXX(self):
        res = convert_to_arabic('CXX')
        self.assertEqual(120, res)

    def test_CXXI(self):
        res = convert_to_arabic('CXXI')
        self.assertEqual(121, res)

    def test_CXXII(self):
        res = convert_to_arabic('CXXII')
        self.assertEqual(122, res)

    def test_CXXIII(self):
        res = convert_to_arabic('CXXIII')
        self.assertEqual(123, res)

    def test_CXXIV(self):
        res = convert_to_arabic('CXXIV')
        self.assertEqual(124, res)

    def test_CXXV(self):
        res = convert_to_arabic('CXXV')
        self.assertEqual(125, res)

    def test_CXXVI(self):
        res = convert_to_arabic('CXXVI')
        self.assertEqual(126, res)

    def test_CXXVII(self):
        res = convert_to_arabic('CXXVII')
        self.assertEqual(127, res)

    def test_CXXVIII(self):
        res = convert_to_arabic('CXXVIII')
        self.assertEqual(128, res)

    def test_CXXIX(self):
        res = convert_to_arabic('CXXIX')
        self.assertEqual(129, res)

    def test_CXXX(self):
        res = convert_to_arabic('CXXX')
        self.assertEqual(130, res)

    def test_CXXXI(self):
        res = convert_to_arabic('CXXXI')
        self.assertEqual(131, res)

    def test_CXXXII(self):
        res = convert_to_arabic('CXXXII')
        self.assertEqual(132, res)

    def test_CXXXIII(self):
        res = convert_to_arabic('CXXXIII')
        self.assertEqual(133, res)

    def test_CXXXIV(self):
        res = convert_to_arabic('CXXXIV')
        self.assertEqual(134, res)

    def test_CXXXV(self):
        res = convert_to_arabic('CXXXV')
        self.assertEqual(135, res)

    def test_CXXXVI(self):
        res = convert_to_arabic('CXXXVI')
        self.assertEqual(136, res)

    def test_CXXXVII(self):
        res = convert_to_arabic('CXXXVII')
        self.assertEqual(137, res)

    def test_CXXXVIII(self):
        res = convert_to_arabic('CXXXVIII')
        self.assertEqual(138, res)

    def test_CXXXIX(self):
        res = convert_to_arabic('CXXXIX')
        self.assertEqual(139, res)

    def test_CXL(self):
        res = convert_to_arabic('CXL')
        self.assertEqual(140, res)

    def test_CXLI(self):
        res = convert_to_arabic('CXLI')
        self.assertEqual(141, res)

    def test_CXLII(self):
        res = convert_to_arabic('CXLII')
        self.assertEqual(142, res)

    def test_CXLIII(self):
        res = convert_to_arabic('CXLIII')
        self.assertEqual(143, res)

    def test_CXLIV(self):
        res = convert_to_arabic('CXLIV')
        self.assertEqual(144, res)

    def test_CXLV(self):
        res = convert_to_arabic('CXLV')
        self.assertEqual(145, res)

    def test_CXLVI(self):
        res = convert_to_arabic('CXLVI')
        self.assertEqual(146, res)

    def test_CXLVII(self):
        res = convert_to_arabic('CXLVII')
        self.assertEqual(147, res)

    def test_CXLVIII(self):
        res = convert_to_arabic('CXLVIII')
        self.assertEqual(148, res)

    def test_CXLIX(self):
        res = convert_to_arabic('CXLIX')
        self.assertEqual(149, res)

    def test_CL(self):
        res = convert_to_arabic('CL')
        self.assertEqual(150, res)

    def test_CLI(self):
        res = convert_to_arabic('CLI')
        self.assertEqual(151, res)

    def test_CLII(self):
        res = convert_to_arabic('CLII')
        self.assertEqual(152, res)

    def test_CLIII(self):
        res = convert_to_arabic('CLIII')
        self.assertEqual(153, res)

    def test_CLIV(self):
        res = convert_to_arabic('CLIV')
        self.assertEqual(154, res)

    def test_CLV(self):
        res = convert_to_arabic('CLV')
        self.assertEqual(155, res)

    def test_CLVI(self):
        res = convert_to_arabic('CLVI')
        self.assertEqual(156, res)

    def test_CLVII(self):
        res = convert_to_arabic('CLVII')
        self.assertEqual(157, res)

    def test_CLVIII(self):
        res = convert_to_arabic('CLVIII')
        self.assertEqual(158, res)

    def test_CLIX(self):
        res = convert_to_arabic('CLIX')
        self.assertEqual(159, res)

    def test_CLX(self):
        res = convert_to_arabic('CLX')
        self.assertEqual(160, res)

    def test_CLXI(self):
        res = convert_to_arabic('CLXI')
        self.assertEqual(161, res)

    def test_CLXII(self):
        res = convert_to_arabic('CLXII')
        self.assertEqual(162, res)

    def test_CLXIII(self):
        res = convert_to_arabic('CLXIII')
        self.assertEqual(163, res)

    def test_CLXIV(self):
        res = convert_to_arabic('CLXIV')
        self.assertEqual(164, res)

    def test_CLXV(self):
        res = convert_to_arabic('CLXV')
        self.assertEqual(165, res)

    def test_CLXVI(self):
        res = convert_to_arabic('CLXVI')
        self.assertEqual(166, res)

    def test_CLXVII(self):
        res = convert_to_arabic('CLXVII')
        self.assertEqual(167, res)

    def test_CLXVIII(self):
        res = convert_to_arabic('CLXVIII')
        self.assertEqual(168, res)

    def test_CLXIX(self):
        res = convert_to_arabic('CLXIX')
        self.assertEqual(169, res)

    def test_CLXX(self):
        res = convert_to_arabic('CLXX')
        self.assertEqual(170, res)

    def test_CLXXI(self):
        res = convert_to_arabic('CLXXI')
        self.assertEqual(171, res)

    def test_CLXXII(self):
        res = convert_to_arabic('CLXXII')
        self.assertEqual(172, res)

    def test_CLXXIII(self):
        res = convert_to_arabic('CLXXIII')
        self.assertEqual(173, res)

    def test_CLXXIV(self):
        res = convert_to_arabic('CLXXIV')
        self.assertEqual(174, res)

    def test_CLXXV(self):
        res = convert_to_arabic('CLXXV')
        self.assertEqual(175, res)

    def test_CLXXVI(self):
        res = convert_to_arabic('CLXXVI')
        self.assertEqual(176, res)

    def test_CLXXVII(self):
        res = convert_to_arabic('CLXXVII')
        self.assertEqual(177, res)

    def test_CLXXVIII(self):
        res = convert_to_arabic('CLXXVIII')
        self.assertEqual(178, res)

    def test_CLXXIX(self):
        res = convert_to_arabic('CLXXIX')
        self.assertEqual(179, res)

    def test_CLXXX(self):
        res = convert_to_arabic('CLXXX')
        self.assertEqual(180, res)

    def test_CLXXXI(self):
        res = convert_to_arabic('CLXXXI')
        self.assertEqual(181, res)

    def test_CLXXXII(self):
        res = convert_to_arabic('CLXXXII')
        self.assertEqual(182, res)

    def test_CLXXXIII(self):
        res = convert_to_arabic('CLXXXIII')
        self.assertEqual(183, res)

    def test_CLXXXIV(self):
        res = convert_to_arabic('CLXXXIV')
        self.assertEqual(184, res)

    def test_CLXXXV(self):
        res = convert_to_arabic('CLXXXV')
        self.assertEqual(185, res)

    def test_CLXXXVI(self):
        res = convert_to_arabic('CLXXXVI')
        self.assertEqual(186, res)

    def test_CLXXXVII(self):
        res = convert_to_arabic('CLXXXVII')
        self.assertEqual(187, res)

    def test_CLXXXVIII(self):
        res = convert_to_arabic('CLXXXVIII')
        self.assertEqual(188, res)

    def test_CLXXXIX(self):
        res = convert_to_arabic('CLXXXIX')
        self.assertEqual(189, res)

    def test_CXC(self):
        res = convert_to_arabic('CXC')
        self.assertEqual(190, res)

    def test_CXCI(self):
        res = convert_to_arabic('CXCI')
        self.assertEqual(191, res)

    def test_CXCII(self):
        res = convert_to_arabic('CXCII')
        self.assertEqual(192, res)

    def test_CXCIII(self):
        res = convert_to_arabic('CXCIII')
        self.assertEqual(193, res)

    def test_CXCIV(self):
        res = convert_to_arabic('CXCIV')
        self.assertEqual(194, res)

    def test_CXCV(self):
        res = convert_to_arabic('CXCV')
        self.assertEqual(195, res)

    def test_CXCVI(self):
        res = convert_to_arabic('CXCVI')
        self.assertEqual(196, res)

    def test_CXCVII(self):
        res = convert_to_arabic('CXCVII')
        self.assertEqual(197, res)

    def test_CXCVIII(self):
        res = convert_to_arabic('CXCVIII')
        self.assertEqual(198, res)

    def test_CXCIX(self):
        res = convert_to_arabic('CXCIX')
        self.assertEqual(199, res)

    def test_CC(self):
        res = convert_to_arabic('CC')
        self.assertEqual(200, res)

    def test_CCI(self):
        res = convert_to_arabic('CCI')
        self.assertEqual(201, res)

    def test_CCII(self):
        res = convert_to_arabic('CCII')
        self.assertEqual(202, res)

    def test_CCIII(self):
        res = convert_to_arabic('CCIII')
        self.assertEqual(203, res)

    def test_CCIV(self):
        res = convert_to_arabic('CCIV')
        self.assertEqual(204, res)

    def test_CCV(self):
        res = convert_to_arabic('CCV')
        self.assertEqual(205, res)

    def test_CCVI(self):
        res = convert_to_arabic('CCVI')
        self.assertEqual(206, res)

    def test_CCVII(self):
        res = convert_to_arabic('CCVII')
        self.assertEqual(207, res)

    def test_CCVIII(self):
        res = convert_to_arabic('CCVIII')
        self.assertEqual(208, res)

    def test_CCIX(self):
        res = convert_to_arabic('CCIX')
        self.assertEqual(209, res)

    def test_CCX(self):
        res = convert_to_arabic('CCX')
        self.assertEqual(210, res)

    def test_CCXI(self):
        res = convert_to_arabic('CCXI')
        self.assertEqual(211, res)

    def test_CCXII(self):
        res = convert_to_arabic('CCXII')
        self.assertEqual(212, res)

    def test_CCXIII(self):
        res = convert_to_arabic('CCXIII')
        self.assertEqual(213, res)

    def test_CCXIV(self):
        res = convert_to_arabic('CCXIV')
        self.assertEqual(214, res)

    def test_CCXV(self):
        res = convert_to_arabic('CCXV')
        self.assertEqual(215, res)

    def test_CCXVI(self):
        res = convert_to_arabic('CCXVI')
        self.assertEqual(216, res)

    def test_CCXVII(self):
        res = convert_to_arabic('CCXVII')
        self.assertEqual(217, res)

    def test_CCXVIII(self):
        res = convert_to_arabic('CCXVIII')
        self.assertEqual(218, res)

    def test_CCXIX(self):
        res = convert_to_arabic('CCXIX')
        self.assertEqual(219, res)

    def test_CCXX(self):
        res = convert_to_arabic('CCXX')
        self.assertEqual(220, res)

    def test_CCXXI(self):
        res = convert_to_arabic('CCXXI')
        self.assertEqual(221, res)

    def test_CCXXII(self):
        res = convert_to_arabic('CCXXII')
        self.assertEqual(222, res)

    def test_CCXXIII(self):
        res = convert_to_arabic('CCXXIII')
        self.assertEqual(223, res)

    def test_CCXXIV(self):
        res = convert_to_arabic('CCXXIV')
        self.assertEqual(224, res)

    def test_CCXXV(self):
        res = convert_to_arabic('CCXXV')
        self.assertEqual(225, res)

    def test_CCXXVI(self):
        res = convert_to_arabic('CCXXVI')
        self.assertEqual(226, res)

    def test_CCXXVII(self):
        res = convert_to_arabic('CCXXVII')
        self.assertEqual(227, res)

    def test_CCXXVIII(self):
        res = convert_to_arabic('CCXXVIII')
        self.assertEqual(228, res)

    def test_CCXXIX(self):
        res = convert_to_arabic('CCXXIX')
        self.assertEqual(229, res)

    def test_CCXXX(self):
        res = convert_to_arabic('CCXXX')
        self.assertEqual(230, res)

    def test_CCXXXI(self):
        res = convert_to_arabic('CCXXXI')
        self.assertEqual(231, res)

    def test_CCXXXII(self):
        res = convert_to_arabic('CCXXXII')
        self.assertEqual(232, res)

    def test_CCXXXIII(self):
        res = convert_to_arabic('CCXXXIII')
        self.assertEqual(233, res)

    def test_CCXXXIV(self):
        res = convert_to_arabic('CCXXXIV')
        self.assertEqual(234, res)

    def test_CCXXXV(self):
        res = convert_to_arabic('CCXXXV')
        self.assertEqual(235, res)

    def test_CCXXXVI(self):
        res = convert_to_arabic('CCXXXVI')
        self.assertEqual(236, res)

    def test_CCXXXVII(self):
        res = convert_to_arabic('CCXXXVII')
        self.assertEqual(237, res)

    def test_CCXXXVIII(self):
        res = convert_to_arabic('CCXXXVIII')
        self.assertEqual(238, res)

    def test_CCXXXIX(self):
        res = convert_to_arabic('CCXXXIX')
        self.assertEqual(239, res)

    def test_CCXL(self):
        res = convert_to_arabic('CCXL')
        self.assertEqual(240, res)

    def test_CCXLI(self):
        res = convert_to_arabic('CCXLI')
        self.assertEqual(241, res)

    def test_CCXLII(self):
        res = convert_to_arabic('CCXLII')
        self.assertEqual(242, res)

    def test_CCXLIII(self):
        res = convert_to_arabic('CCXLIII')
        self.assertEqual(243, res)

    def test_CCXLIV(self):
        res = convert_to_arabic('CCXLIV')
        self.assertEqual(244, res)

    def test_CCXLV(self):
        res = convert_to_arabic('CCXLV')
        self.assertEqual(245, res)

    def test_CCXLVI(self):
        res = convert_to_arabic('CCXLVI')
        self.assertEqual(246, res)

    def test_CCXLVII(self):
        res = convert_to_arabic('CCXLVII')
        self.assertEqual(247, res)

    def test_CCXLVIII(self):
        res = convert_to_arabic('CCXLVIII')
        self.assertEqual(248, res)

    def test_CCXLIX(self):
        res = convert_to_arabic('CCXLIX')
        self.assertEqual(249, res)

    def test_CCL(self):
        res = convert_to_arabic('CCL')
        self.assertEqual(250, res)

    def test_CCLI(self):
        res = convert_to_arabic('CCLI')
        self.assertEqual(251, res)

    def test_CCLII(self):
        res = convert_to_arabic('CCLII')
        self.assertEqual(252, res)

    def test_CCLIII(self):
        res = convert_to_arabic('CCLIII')
        self.assertEqual(253, res)

    def test_CCLIV(self):
        res = convert_to_arabic('CCLIV')
        self.assertEqual(254, res)

    def test_CCLV(self):
        res = convert_to_arabic('CCLV')
        self.assertEqual(255, res)

    def test_CCLVI(self):
        res = convert_to_arabic('CCLVI')
        self.assertEqual(256, res)

    def test_CCLVII(self):
        res = convert_to_arabic('CCLVII')
        self.assertEqual(257, res)

    def test_CCLVIII(self):
        res = convert_to_arabic('CCLVIII')
        self.assertEqual(258, res)

    def test_CCLIX(self):
        res = convert_to_arabic('CCLIX')
        self.assertEqual(259, res)

    def test_CCLX(self):
        res = convert_to_arabic('CCLX')
        self.assertEqual(260, res)

    def test_CCLXI(self):
        res = convert_to_arabic('CCLXI')
        self.assertEqual(261, res)

    def test_CCLXII(self):
        res = convert_to_arabic('CCLXII')
        self.assertEqual(262, res)

    def test_CCLXIII(self):
        res = convert_to_arabic('CCLXIII')
        self.assertEqual(263, res)

    def test_CCLXIV(self):
        res = convert_to_arabic('CCLXIV')
        self.assertEqual(264, res)

    def test_CCLXV(self):
        res = convert_to_arabic('CCLXV')
        self.assertEqual(265, res)

    def test_CCLXVI(self):
        res = convert_to_arabic('CCLXVI')
        self.assertEqual(266, res)

    def test_CCLXVII(self):
        res = convert_to_arabic('CCLXVII')
        self.assertEqual(267, res)

    def test_CCLXVIII(self):
        res = convert_to_arabic('CCLXVIII')
        self.assertEqual(268, res)

    def test_CCLXIX(self):
        res = convert_to_arabic('CCLXIX')
        self.assertEqual(269, res)

    def test_CCLXX(self):
        res = convert_to_arabic('CCLXX')
        self.assertEqual(270, res)

    def test_CCLXXI(self):
        res = convert_to_arabic('CCLXXI')
        self.assertEqual(271, res)

    def test_CCLXXII(self):
        res = convert_to_arabic('CCLXXII')
        self.assertEqual(272, res)

    def test_CCLXXIII(self):
        res = convert_to_arabic('CCLXXIII')
        self.assertEqual(273, res)

    def test_CCLXXIV(self):
        res = convert_to_arabic('CCLXXIV')
        self.assertEqual(274, res)

    def test_CCLXXV(self):
        res = convert_to_arabic('CCLXXV')
        self.assertEqual(275, res)

    def test_CCLXXVI(self):
        res = convert_to_arabic('CCLXXVI')
        self.assertEqual(276, res)

    def test_CCLXXVII(self):
        res = convert_to_arabic('CCLXXVII')
        self.assertEqual(277, res)

    def test_CCLXXVIII(self):
        res = convert_to_arabic('CCLXXVIII')
        self.assertEqual(278, res)

    def test_CCLXXIX(self):
        res = convert_to_arabic('CCLXXIX')
        self.assertEqual(279, res)

    def test_CCLXXX(self):
        res = convert_to_arabic('CCLXXX')
        self.assertEqual(280, res)

    def test_CCLXXXI(self):
        res = convert_to_arabic('CCLXXXI')
        self.assertEqual(281, res)

    def test_CCLXXXII(self):
        res = convert_to_arabic('CCLXXXII')
        self.assertEqual(282, res)

    def test_CCLXXXIII(self):
        res = convert_to_arabic('CCLXXXIII')
        self.assertEqual(283, res)

    def test_CCLXXXIV(self):
        res = convert_to_arabic('CCLXXXIV')
        self.assertEqual(284, res)

    def test_CCLXXXV(self):
        res = convert_to_arabic('CCLXXXV')
        self.assertEqual(285, res)

    def test_CCLXXXVI(self):
        res = convert_to_arabic('CCLXXXVI')
        self.assertEqual(286, res)

    def test_CCLXXXVII(self):
        res = convert_to_arabic('CCLXXXVII')
        self.assertEqual(287, res)

    def test_CCLXXXVIII(self):
        res = convert_to_arabic('CCLXXXVIII')
        self.assertEqual(288, res)

    def test_CCLXXXIX(self):
        res = convert_to_arabic('CCLXXXIX')
        self.assertEqual(289, res)

    def test_CCXC(self):
        res = convert_to_arabic('CCXC')
        self.assertEqual(290, res)

    def test_CCXCI(self):
        res = convert_to_arabic('CCXCI')
        self.assertEqual(291, res)

    def test_CCXCII(self):
        res = convert_to_arabic('CCXCII')
        self.assertEqual(292, res)

    def test_CCXCIII(self):
        res = convert_to_arabic('CCXCIII')
        self.assertEqual(293, res)

    def test_CCXCIV(self):
        res = convert_to_arabic('CCXCIV')
        self.assertEqual(294, res)

    def test_CCXCV(self):
        res = convert_to_arabic('CCXCV')
        self.assertEqual(295, res)

    def test_CCXCVI(self):
        res = convert_to_arabic('CCXCVI')
        self.assertEqual(296, res)

    def test_CCXCVII(self):
        res = convert_to_arabic('CCXCVII')
        self.assertEqual(297, res)

    def test_CCXCVIII(self):
        res = convert_to_arabic('CCXCVIII')
        self.assertEqual(298, res)

    def test_CCXCIX(self):
        res = convert_to_arabic('CCXCIX')
        self.assertEqual(299, res)

    def test_CCC(self):
        res = convert_to_arabic('CCC')
        self.assertEqual(300, res)

    def test_CCCI(self):
        res = convert_to_arabic('CCCI')
        self.assertEqual(301, res)

    def test_CCCII(self):
        res = convert_to_arabic('CCCII')
        self.assertEqual(302, res)

    def test_CCCIII(self):
        res = convert_to_arabic('CCCIII')
        self.assertEqual(303, res)

    def test_CCCIV(self):
        res = convert_to_arabic('CCCIV')
        self.assertEqual(304, res)

    def test_CCCV(self):
        res = convert_to_arabic('CCCV')
        self.assertEqual(305, res)

    def test_CCCVI(self):
        res = convert_to_arabic('CCCVI')
        self.assertEqual(306, res)

    def test_CCCVII(self):
        res = convert_to_arabic('CCCVII')
        self.assertEqual(307, res)

    def test_CCCVIII(self):
        res = convert_to_arabic('CCCVIII')
        self.assertEqual(308, res)

    def test_CCCIX(self):
        res = convert_to_arabic('CCCIX')
        self.assertEqual(309, res)

    def test_CCCX(self):
        res = convert_to_arabic('CCCX')
        self.assertEqual(310, res)

    def test_CCCXI(self):
        res = convert_to_arabic('CCCXI')
        self.assertEqual(311, res)

    def test_CCCXII(self):
        res = convert_to_arabic('CCCXII')
        self.assertEqual(312, res)

    def test_CCCXIII(self):
        res = convert_to_arabic('CCCXIII')
        self.assertEqual(313, res)

    def test_CCCXIV(self):
        res = convert_to_arabic('CCCXIV')
        self.assertEqual(314, res)

    def test_CCCXV(self):
        res = convert_to_arabic('CCCXV')
        self.assertEqual(315, res)

    def test_CCCXVI(self):
        res = convert_to_arabic('CCCXVI')
        self.assertEqual(316, res)

    def test_CCCXVII(self):
        res = convert_to_arabic('CCCXVII')
        self.assertEqual(317, res)

    def test_CCCXVIII(self):
        res = convert_to_arabic('CCCXVIII')
        self.assertEqual(318, res)

    def test_CCCXIX(self):
        res = convert_to_arabic('CCCXIX')
        self.assertEqual(319, res)

    def test_CCCXX(self):
        res = convert_to_arabic('CCCXX')
        self.assertEqual(320, res)

    def test_CCCXXI(self):
        res = convert_to_arabic('CCCXXI')
        self.assertEqual(321, res)

    def test_CCCXXII(self):
        res = convert_to_arabic('CCCXXII')
        self.assertEqual(322, res)

    def test_CCCXXIII(self):
        res = convert_to_arabic('CCCXXIII')
        self.assertEqual(323, res)

    def test_CCCXXIV(self):
        res = convert_to_arabic('CCCXXIV')
        self.assertEqual(324, res)

    def test_CCCXXV(self):
        res = convert_to_arabic('CCCXXV')
        self.assertEqual(325, res)

    def test_CCCXXVI(self):
        res = convert_to_arabic('CCCXXVI')
        self.assertEqual(326, res)

    def test_CCCXXVII(self):
        res = convert_to_arabic('CCCXXVII')
        self.assertEqual(327, res)

    def test_CCCXXVIII(self):
        res = convert_to_arabic('CCCXXVIII')
        self.assertEqual(328, res)

    def test_CCCXXIX(self):
        res = convert_to_arabic('CCCXXIX')
        self.assertEqual(329, res)

    def test_CCCXXX(self):
        res = convert_to_arabic('CCCXXX')
        self.assertEqual(330, res)

    def test_CCCXXXI(self):
        res = convert_to_arabic('CCCXXXI')
        self.assertEqual(331, res)

    def test_CCCXXXII(self):
        res = convert_to_arabic('CCCXXXII')
        self.assertEqual(332, res)

    def test_CCCXXXIII(self):
        res = convert_to_arabic('CCCXXXIII')
        self.assertEqual(333, res)

    def test_CCCXXXIV(self):
        res = convert_to_arabic('CCCXXXIV')
        self.assertEqual(334, res)

    def test_CCCXXXV(self):
        res = convert_to_arabic('CCCXXXV')
        self.assertEqual(335, res)

    def test_CCCXXXVI(self):
        res = convert_to_arabic('CCCXXXVI')
        self.assertEqual(336, res)

    def test_CCCXXXVII(self):
        res = convert_to_arabic('CCCXXXVII')
        self.assertEqual(337, res)

    def test_CCCXXXVIII(self):
        res = convert_to_arabic('CCCXXXVIII')
        self.assertEqual(338, res)

    def test_CCCXXXIX(self):
        res = convert_to_arabic('CCCXXXIX')
        self.assertEqual(339, res)

    def test_CCCXL(self):
        res = convert_to_arabic('CCCXL')
        self.assertEqual(340, res)

    def test_CCCXLI(self):
        res = convert_to_arabic('CCCXLI')
        self.assertEqual(341, res)

    def test_CCCXLII(self):
        res = convert_to_arabic('CCCXLII')
        self.assertEqual(342, res)

    def test_CCCXLIII(self):
        res = convert_to_arabic('CCCXLIII')
        self.assertEqual(343, res)

    def test_CCCXLIV(self):
        res = convert_to_arabic('CCCXLIV')
        self.assertEqual(344, res)

    def test_CCCXLV(self):
        res = convert_to_arabic('CCCXLV')
        self.assertEqual(345, res)

    def test_CCCXLVI(self):
        res = convert_to_arabic('CCCXLVI')
        self.assertEqual(346, res)

    def test_CCCXLVII(self):
        res = convert_to_arabic('CCCXLVII')
        self.assertEqual(347, res)

    def test_CCCXLVIII(self):
        res = convert_to_arabic('CCCXLVIII')
        self.assertEqual(348, res)

    def test_CCCXLIX(self):
        res = convert_to_arabic('CCCXLIX')
        self.assertEqual(349, res)

    def test_CCCL(self):
        res = convert_to_arabic('CCCL')
        self.assertEqual(350, res)

    def test_CCCLI(self):
        res = convert_to_arabic('CCCLI')
        self.assertEqual(351, res)

    def test_CCCLII(self):
        res = convert_to_arabic('CCCLII')
        self.assertEqual(352, res)

    def test_CCCLIII(self):
        res = convert_to_arabic('CCCLIII')
        self.assertEqual(353, res)

    def test_CCCLIV(self):
        res = convert_to_arabic('CCCLIV')
        self.assertEqual(354, res)

    def test_CCCLV(self):
        res = convert_to_arabic('CCCLV')
        self.assertEqual(355, res)

    def test_CCCLVI(self):
        res = convert_to_arabic('CCCLVI')
        self.assertEqual(356, res)

    def test_CCCLVII(self):
        res = convert_to_arabic('CCCLVII')
        self.assertEqual(357, res)

    def test_CCCLVIII(self):
        res = convert_to_arabic('CCCLVIII')
        self.assertEqual(358, res)

    def test_CCCLIX(self):
        res = convert_to_arabic('CCCLIX')
        self.assertEqual(359, res)

    def test_CCCLX(self):
        res = convert_to_arabic('CCCLX')
        self.assertEqual(360, res)

    def test_CCCLXI(self):
        res = convert_to_arabic('CCCLXI')
        self.assertEqual(361, res)

    def test_CCCLXII(self):
        res = convert_to_arabic('CCCLXII')
        self.assertEqual(362, res)

    def test_CCCLXIII(self):
        res = convert_to_arabic('CCCLXIII')
        self.assertEqual(363, res)

    def test_CCCLXIV(self):
        res = convert_to_arabic('CCCLXIV')
        self.assertEqual(364, res)

    def test_CCCLXV(self):
        res = convert_to_arabic('CCCLXV')
        self.assertEqual(365, res)

    def test_CCCLXVI(self):
        res = convert_to_arabic('CCCLXVI')
        self.assertEqual(366, res)

    def test_CCCLXVII(self):
        res = convert_to_arabic('CCCLXVII')
        self.assertEqual(367, res)

    def test_CCCLXVIII(self):
        res = convert_to_arabic('CCCLXVIII')
        self.assertEqual(368, res)

    def test_CCCLXIX(self):
        res = convert_to_arabic('CCCLXIX')
        self.assertEqual(369, res)

    def test_CCCLXX(self):
        res = convert_to_arabic('CCCLXX')
        self.assertEqual(370, res)

    def test_CCCLXXI(self):
        res = convert_to_arabic('CCCLXXI')
        self.assertEqual(371, res)

    def test_CCCLXXII(self):
        res = convert_to_arabic('CCCLXXII')
        self.assertEqual(372, res)

    def test_CCCLXXIII(self):
        res = convert_to_arabic('CCCLXXIII')
        self.assertEqual(373, res)

    def test_CCCLXXIV(self):
        res = convert_to_arabic('CCCLXXIV')
        self.assertEqual(374, res)

    def test_CCCLXXV(self):
        res = convert_to_arabic('CCCLXXV')
        self.assertEqual(375, res)

    def test_CCCLXXVI(self):
        res = convert_to_arabic('CCCLXXVI')
        self.assertEqual(376, res)

    def test_CCCLXXVII(self):
        res = convert_to_arabic('CCCLXXVII')
        self.assertEqual(377, res)

    def test_CCCLXXVIII(self):
        res = convert_to_arabic('CCCLXXVIII')
        self.assertEqual(378, res)

    def test_CCCLXXIX(self):
        res = convert_to_arabic('CCCLXXIX')
        self.assertEqual(379, res)

    def test_CCCLXXX(self):
        res = convert_to_arabic('CCCLXXX')
        self.assertEqual(380, res)

    def test_CCCLXXXI(self):
        res = convert_to_arabic('CCCLXXXI')
        self.assertEqual(381, res)

    def test_CCCLXXXII(self):
        res = convert_to_arabic('CCCLXXXII')
        self.assertEqual(382, res)

    def test_CCCLXXXIII(self):
        res = convert_to_arabic('CCCLXXXIII')
        self.assertEqual(383, res)

    def test_CCCLXXXIV(self):
        res = convert_to_arabic('CCCLXXXIV')
        self.assertEqual(384, res)

    def test_CCCLXXXV(self):
        res = convert_to_arabic('CCCLXXXV')
        self.assertEqual(385, res)

    def test_CCCLXXXVI(self):
        res = convert_to_arabic('CCCLXXXVI')
        self.assertEqual(386, res)

    def test_CCCLXXXVII(self):
        res = convert_to_arabic('CCCLXXXVII')
        self.assertEqual(387, res)

    def test_CCCLXXXVIII(self):
        res = convert_to_arabic('CCCLXXXVIII')
        self.assertEqual(388, res)

    def test_CCCLXXXIX(self):
        res = convert_to_arabic('CCCLXXXIX')
        self.assertEqual(389, res)

    def test_CCCXC(self):
        res = convert_to_arabic('CCCXC')
        self.assertEqual(390, res)

    def test_CCCXCI(self):
        res = convert_to_arabic('CCCXCI')
        self.assertEqual(391, res)

    def test_CCCXCII(self):
        res = convert_to_arabic('CCCXCII')
        self.assertEqual(392, res)

    def test_CCCXCIII(self):
        res = convert_to_arabic('CCCXCIII')
        self.assertEqual(393, res)

    def test_CCCXCIV(self):
        res = convert_to_arabic('CCCXCIV')
        self.assertEqual(394, res)

    def test_CCCXCV(self):
        res = convert_to_arabic('CCCXCV')
        self.assertEqual(395, res)

    def test_CCCXCVI(self):
        res = convert_to_arabic('CCCXCVI')
        self.assertEqual(396, res)

    def test_CCCXCVII(self):
        res = convert_to_arabic('CCCXCVII')
        self.assertEqual(397, res)

    def test_CCCXCVIII(self):
        res = convert_to_arabic('CCCXCVIII')
        self.assertEqual(398, res)

    def test_CCCXCIX(self):
        res = convert_to_arabic('CCCXCIX')
        self.assertEqual(399, res)

    def test_CD(self):
        res = convert_to_arabic('CD')
        self.assertEqual(400, res)

    def test_CDI(self):
        res = convert_to_arabic('CDI')
        self.assertEqual(401, res)

    def test_CDII(self):
        res = convert_to_arabic('CDII')
        self.assertEqual(402, res)

    def test_CDIII(self):
        res = convert_to_arabic('CDIII')
        self.assertEqual(403, res)

    def test_CDIV(self):
        res = convert_to_arabic('CDIV')
        self.assertEqual(404, res)

    def test_CDV(self):
        res = convert_to_arabic('CDV')
        self.assertEqual(405, res)

    def test_CDVI(self):
        res = convert_to_arabic('CDVI')
        self.assertEqual(406, res)

    def test_CDVII(self):
        res = convert_to_arabic('CDVII')
        self.assertEqual(407, res)

    def test_CDVIII(self):
        res = convert_to_arabic('CDVIII')
        self.assertEqual(408, res)

    def test_CDIX(self):
        res = convert_to_arabic('CDIX')
        self.assertEqual(409, res)

    def test_CDX(self):
        res = convert_to_arabic('CDX')
        self.assertEqual(410, res)

    def test_CDXI(self):
        res = convert_to_arabic('CDXI')
        self.assertEqual(411, res)

    def test_CDXII(self):
        res = convert_to_arabic('CDXII')
        self.assertEqual(412, res)

    def test_CDXIII(self):
        res = convert_to_arabic('CDXIII')
        self.assertEqual(413, res)

    def test_CDXIV(self):
        res = convert_to_arabic('CDXIV')
        self.assertEqual(414, res)

    def test_CDXV(self):
        res = convert_to_arabic('CDXV')
        self.assertEqual(415, res)

    def test_CDXVI(self):
        res = convert_to_arabic('CDXVI')
        self.assertEqual(416, res)

    def test_CDXVII(self):
        res = convert_to_arabic('CDXVII')
        self.assertEqual(417, res)

    def test_CDXVIII(self):
        res = convert_to_arabic('CDXVIII')
        self.assertEqual(418, res)

    def test_CDXIX(self):
        res = convert_to_arabic('CDXIX')
        self.assertEqual(419, res)

    def test_CDXX(self):
        res = convert_to_arabic('CDXX')
        self.assertEqual(420, res)

    def test_CDXXI(self):
        res = convert_to_arabic('CDXXI')
        self.assertEqual(421, res)

    def test_CDXXII(self):
        res = convert_to_arabic('CDXXII')
        self.assertEqual(422, res)

    def test_CDXXIII(self):
        res = convert_to_arabic('CDXXIII')
        self.assertEqual(423, res)

    def test_CDXXIV(self):
        res = convert_to_arabic('CDXXIV')
        self.assertEqual(424, res)

    def test_CDXXV(self):
        res = convert_to_arabic('CDXXV')
        self.assertEqual(425, res)

    def test_CDXXVI(self):
        res = convert_to_arabic('CDXXVI')
        self.assertEqual(426, res)

    def test_CDXXVII(self):
        res = convert_to_arabic('CDXXVII')
        self.assertEqual(427, res)

    def test_CDXXVIII(self):
        res = convert_to_arabic('CDXXVIII')
        self.assertEqual(428, res)

    def test_CDXXIX(self):
        res = convert_to_arabic('CDXXIX')
        self.assertEqual(429, res)

    def test_CDXXX(self):
        res = convert_to_arabic('CDXXX')
        self.assertEqual(430, res)

    def test_CDXXXI(self):
        res = convert_to_arabic('CDXXXI')
        self.assertEqual(431, res)

    def test_CDXXXII(self):
        res = convert_to_arabic('CDXXXII')
        self.assertEqual(432, res)

    def test_CDXXXIII(self):
        res = convert_to_arabic('CDXXXIII')
        self.assertEqual(433, res)

    def test_CDXXXIV(self):
        res = convert_to_arabic('CDXXXIV')
        self.assertEqual(434, res)

    def test_CDXXXV(self):
        res = convert_to_arabic('CDXXXV')
        self.assertEqual(435, res)

    def test_CDXXXVI(self):
        res = convert_to_arabic('CDXXXVI')
        self.assertEqual(436, res)

    def test_CDXXXVII(self):
        res = convert_to_arabic('CDXXXVII')
        self.assertEqual(437, res)

    def test_CDXXXVIII(self):
        res = convert_to_arabic('CDXXXVIII')
        self.assertEqual(438, res)

    def test_CDXXXIX(self):
        res = convert_to_arabic('CDXXXIX')
        self.assertEqual(439, res)

    def test_CDXL(self):
        res = convert_to_arabic('CDXL')
        self.assertEqual(440, res)

    def test_CDXLI(self):
        res = convert_to_arabic('CDXLI')
        self.assertEqual(441, res)

    def test_CDXLII(self):
        res = convert_to_arabic('CDXLII')
        self.assertEqual(442, res)

    def test_CDXLIII(self):
        res = convert_to_arabic('CDXLIII')
        self.assertEqual(443, res)

    def test_CDXLIV(self):
        res = convert_to_arabic('CDXLIV')
        self.assertEqual(444, res)

    def test_CDXLV(self):
        res = convert_to_arabic('CDXLV')
        self.assertEqual(445, res)

    def test_CDXLVI(self):
        res = convert_to_arabic('CDXLVI')
        self.assertEqual(446, res)

    def test_CDXLVII(self):
        res = convert_to_arabic('CDXLVII')
        self.assertEqual(447, res)

    def test_CDXLVIII(self):
        res = convert_to_arabic('CDXLVIII')
        self.assertEqual(448, res)

    def test_CDXLIX(self):
        res = convert_to_arabic('CDXLIX')
        self.assertEqual(449, res)

    def test_CDL(self):
        res = convert_to_arabic('CDL')
        self.assertEqual(450, res)

    def test_CDLI(self):
        res = convert_to_arabic('CDLI')
        self.assertEqual(451, res)

    def test_CDLII(self):
        res = convert_to_arabic('CDLII')
        self.assertEqual(452, res)

    def test_CDLIII(self):
        res = convert_to_arabic('CDLIII')
        self.assertEqual(453, res)

    def test_CDLIV(self):
        res = convert_to_arabic('CDLIV')
        self.assertEqual(454, res)

    def test_CDLV(self):
        res = convert_to_arabic('CDLV')
        self.assertEqual(455, res)

    def test_CDLVI(self):
        res = convert_to_arabic('CDLVI')
        self.assertEqual(456, res)

    def test_CDLVII(self):
        res = convert_to_arabic('CDLVII')
        self.assertEqual(457, res)

    def test_CDLVIII(self):
        res = convert_to_arabic('CDLVIII')
        self.assertEqual(458, res)

    def test_CDLIX(self):
        res = convert_to_arabic('CDLIX')
        self.assertEqual(459, res)

    def test_CDLX(self):
        res = convert_to_arabic('CDLX')
        self.assertEqual(460, res)

    def test_CDLXI(self):
        res = convert_to_arabic('CDLXI')
        self.assertEqual(461, res)

    def test_CDLXII(self):
        res = convert_to_arabic('CDLXII')
        self.assertEqual(462, res)

    def test_CDLXIII(self):
        res = convert_to_arabic('CDLXIII')
        self.assertEqual(463, res)

    def test_CDLXIV(self):
        res = convert_to_arabic('CDLXIV')
        self.assertEqual(464, res)

    def test_CDLXV(self):
        res = convert_to_arabic('CDLXV')
        self.assertEqual(465, res)

    def test_CDLXVI(self):
        res = convert_to_arabic('CDLXVI')
        self.assertEqual(466, res)

    def test_CDLXVII(self):
        res = convert_to_arabic('CDLXVII')
        self.assertEqual(467, res)

    def test_CDLXVIII(self):
        res = convert_to_arabic('CDLXVIII')
        self.assertEqual(468, res)

    def test_CDLXIX(self):
        res = convert_to_arabic('CDLXIX')
        self.assertEqual(469, res)

    def test_CDLXX(self):
        res = convert_to_arabic('CDLXX')
        self.assertEqual(470, res)

    def test_CDLXXI(self):
        res = convert_to_arabic('CDLXXI')
        self.assertEqual(471, res)

    def test_CDLXXII(self):
        res = convert_to_arabic('CDLXXII')
        self.assertEqual(472, res)

    def test_CDLXXIII(self):
        res = convert_to_arabic('CDLXXIII')
        self.assertEqual(473, res)

    def test_CDLXXIV(self):
        res = convert_to_arabic('CDLXXIV')
        self.assertEqual(474, res)

    def test_CDLXXV(self):
        res = convert_to_arabic('CDLXXV')
        self.assertEqual(475, res)

    def test_CDLXXVI(self):
        res = convert_to_arabic('CDLXXVI')
        self.assertEqual(476, res)

    def test_CDLXXVII(self):
        res = convert_to_arabic('CDLXXVII')
        self.assertEqual(477, res)

    def test_CDLXXVIII(self):
        res = convert_to_arabic('CDLXXVIII')
        self.assertEqual(478, res)

    def test_CDLXXIX(self):
        res = convert_to_arabic('CDLXXIX')
        self.assertEqual(479, res)

    def test_CDLXXX(self):
        res = convert_to_arabic('CDLXXX')
        self.assertEqual(480, res)

    def test_CDLXXXI(self):
        res = convert_to_arabic('CDLXXXI')
        self.assertEqual(481, res)

    def test_CDLXXXII(self):
        res = convert_to_arabic('CDLXXXII')
        self.assertEqual(482, res)

    def test_CDLXXXIII(self):
        res = convert_to_arabic('CDLXXXIII')
        self.assertEqual(483, res)

    def test_CDLXXXIV(self):
        res = convert_to_arabic('CDLXXXIV')
        self.assertEqual(484, res)

    def test_CDLXXXV(self):
        res = convert_to_arabic('CDLXXXV')
        self.assertEqual(485, res)

    def test_CDLXXXVI(self):
        res = convert_to_arabic('CDLXXXVI')
        self.assertEqual(486, res)

    def test_CDLXXXVII(self):
        res = convert_to_arabic('CDLXXXVII')
        self.assertEqual(487, res)

    def test_CDLXXXVIII(self):
        res = convert_to_arabic('CDLXXXVIII')
        self.assertEqual(488, res)

    def test_CDLXXXIX(self):
        res = convert_to_arabic('CDLXXXIX')
        self.assertEqual(489, res)

    def test_CDXC(self):
        res = convert_to_arabic('CDXC')
        self.assertEqual(490, res)

    def test_CDXCI(self):
        res = convert_to_arabic('CDXCI')
        self.assertEqual(491, res)

    def test_CDXCII(self):
        res = convert_to_arabic('CDXCII')
        self.assertEqual(492, res)

    def test_CDXCIII(self):
        res = convert_to_arabic('CDXCIII')
        self.assertEqual(493, res)

    def test_CDXCIV(self):
        res = convert_to_arabic('CDXCIV')
        self.assertEqual(494, res)

    def test_CDXCV(self):
        res = convert_to_arabic('CDXCV')
        self.assertEqual(495, res)

    def test_CDXCVI(self):
        res = convert_to_arabic('CDXCVI')
        self.assertEqual(496, res)

    def test_CDXCVII(self):
        res = convert_to_arabic('CDXCVII')
        self.assertEqual(497, res)

    def test_CDXCVIII(self):
        res = convert_to_arabic('CDXCVIII')
        self.assertEqual(498, res)

    def test_CDXCIX(self):
        res = convert_to_arabic('CDXCIX')
        self.assertEqual(499, res)

    def test_D(self):
        res = convert_to_arabic('D')
        self.assertEqual(500, res)

    def test_DI(self):
        res = convert_to_arabic('DI')
        self.assertEqual(501, res)

    def test_DII(self):
        res = convert_to_arabic('DII')
        self.assertEqual(502, res)

    def test_DIII(self):
        res = convert_to_arabic('DIII')
        self.assertEqual(503, res)

    def test_DIV(self):
        res = convert_to_arabic('DIV')
        self.assertEqual(504, res)

    def test_DV(self):
        res = convert_to_arabic('DV')
        self.assertEqual(505, res)

    def test_DVI(self):
        res = convert_to_arabic('DVI')
        self.assertEqual(506, res)

    def test_DVII(self):
        res = convert_to_arabic('DVII')
        self.assertEqual(507, res)

    def test_DVIII(self):
        res = convert_to_arabic('DVIII')
        self.assertEqual(508, res)

    def test_DIX(self):
        res = convert_to_arabic('DIX')
        self.assertEqual(509, res)

    def test_DX(self):
        res = convert_to_arabic('DX')
        self.assertEqual(510, res)

    def test_DXI(self):
        res = convert_to_arabic('DXI')
        self.assertEqual(511, res)

    def test_DXII(self):
        res = convert_to_arabic('DXII')
        self.assertEqual(512, res)

    def test_DXIII(self):
        res = convert_to_arabic('DXIII')
        self.assertEqual(513, res)

    def test_DXIV(self):
        res = convert_to_arabic('DXIV')
        self.assertEqual(514, res)

    def test_DXV(self):
        res = convert_to_arabic('DXV')
        self.assertEqual(515, res)

    def test_DXVI(self):
        res = convert_to_arabic('DXVI')
        self.assertEqual(516, res)

    def test_DXVII(self):
        res = convert_to_arabic('DXVII')
        self.assertEqual(517, res)

    def test_DXVIII(self):
        res = convert_to_arabic('DXVIII')
        self.assertEqual(518, res)

    def test_DXIX(self):
        res = convert_to_arabic('DXIX')
        self.assertEqual(519, res)

    def test_DXX(self):
        res = convert_to_arabic('DXX')
        self.assertEqual(520, res)

    def test_DXXI(self):
        res = convert_to_arabic('DXXI')
        self.assertEqual(521, res)

    def test_DXXII(self):
        res = convert_to_arabic('DXXII')
        self.assertEqual(522, res)

    def test_DXXIII(self):
        res = convert_to_arabic('DXXIII')
        self.assertEqual(523, res)

    def test_DXXIV(self):
        res = convert_to_arabic('DXXIV')
        self.assertEqual(524, res)

    def test_DXXV(self):
        res = convert_to_arabic('DXXV')
        self.assertEqual(525, res)

    def test_DXXVI(self):
        res = convert_to_arabic('DXXVI')
        self.assertEqual(526, res)

    def test_DXXVII(self):
        res = convert_to_arabic('DXXVII')
        self.assertEqual(527, res)

    def test_DXXVIII(self):
        res = convert_to_arabic('DXXVIII')
        self.assertEqual(528, res)

    def test_DXXIX(self):
        res = convert_to_arabic('DXXIX')
        self.assertEqual(529, res)

    def test_DXXX(self):
        res = convert_to_arabic('DXXX')
        self.assertEqual(530, res)

    def test_DXXXI(self):
        res = convert_to_arabic('DXXXI')
        self.assertEqual(531, res)

    def test_DXXXII(self):
        res = convert_to_arabic('DXXXII')
        self.assertEqual(532, res)

    def test_DXXXIII(self):
        res = convert_to_arabic('DXXXIII')
        self.assertEqual(533, res)

    def test_DXXXIV(self):
        res = convert_to_arabic('DXXXIV')
        self.assertEqual(534, res)

    def test_DXXXV(self):
        res = convert_to_arabic('DXXXV')
        self.assertEqual(535, res)

    def test_DXXXVI(self):
        res = convert_to_arabic('DXXXVI')
        self.assertEqual(536, res)

    def test_DXXXVII(self):
        res = convert_to_arabic('DXXXVII')
        self.assertEqual(537, res)

    def test_DXXXVIII(self):
        res = convert_to_arabic('DXXXVIII')
        self.assertEqual(538, res)

    def test_DXXXIX(self):
        res = convert_to_arabic('DXXXIX')
        self.assertEqual(539, res)

    def test_DXL(self):
        res = convert_to_arabic('DXL')
        self.assertEqual(540, res)

    def test_DXLI(self):
        res = convert_to_arabic('DXLI')
        self.assertEqual(541, res)

    def test_DXLII(self):
        res = convert_to_arabic('DXLII')
        self.assertEqual(542, res)

    def test_DXLIII(self):
        res = convert_to_arabic('DXLIII')
        self.assertEqual(543, res)

    def test_DXLIV(self):
        res = convert_to_arabic('DXLIV')
        self.assertEqual(544, res)

    def test_DXLV(self):
        res = convert_to_arabic('DXLV')
        self.assertEqual(545, res)

    def test_DXLVI(self):
        res = convert_to_arabic('DXLVI')
        self.assertEqual(546, res)

    def test_DXLVII(self):
        res = convert_to_arabic('DXLVII')
        self.assertEqual(547, res)

    def test_DXLVIII(self):
        res = convert_to_arabic('DXLVIII')
        self.assertEqual(548, res)

    def test_DXLIX(self):
        res = convert_to_arabic('DXLIX')
        self.assertEqual(549, res)

    def test_DL(self):
        res = convert_to_arabic('DL')
        self.assertEqual(550, res)

    def test_DLI(self):
        res = convert_to_arabic('DLI')
        self.assertEqual(551, res)

    def test_DLII(self):
        res = convert_to_arabic('DLII')
        self.assertEqual(552, res)

    def test_DLIII(self):
        res = convert_to_arabic('DLIII')
        self.assertEqual(553, res)

    def test_DLIV(self):
        res = convert_to_arabic('DLIV')
        self.assertEqual(554, res)

    def test_DLV(self):
        res = convert_to_arabic('DLV')
        self.assertEqual(555, res)

    def test_DLVI(self):
        res = convert_to_arabic('DLVI')
        self.assertEqual(556, res)

    def test_DLVII(self):
        res = convert_to_arabic('DLVII')
        self.assertEqual(557, res)

    def test_DLVIII(self):
        res = convert_to_arabic('DLVIII')
        self.assertEqual(558, res)

    def test_DLIX(self):
        res = convert_to_arabic('DLIX')
        self.assertEqual(559, res)

    def test_DLX(self):
        res = convert_to_arabic('DLX')
        self.assertEqual(560, res)

    def test_DLXI(self):
        res = convert_to_arabic('DLXI')
        self.assertEqual(561, res)

    def test_DLXII(self):
        res = convert_to_arabic('DLXII')
        self.assertEqual(562, res)

    def test_DLXIII(self):
        res = convert_to_arabic('DLXIII')
        self.assertEqual(563, res)

    def test_DLXIV(self):
        res = convert_to_arabic('DLXIV')
        self.assertEqual(564, res)

    def test_DLXV(self):
        res = convert_to_arabic('DLXV')
        self.assertEqual(565, res)

    def test_DLXVI(self):
        res = convert_to_arabic('DLXVI')
        self.assertEqual(566, res)

    def test_DLXVII(self):
        res = convert_to_arabic('DLXVII')
        self.assertEqual(567, res)

    def test_DLXVIII(self):
        res = convert_to_arabic('DLXVIII')
        self.assertEqual(568, res)

    def test_DLXIX(self):
        res = convert_to_arabic('DLXIX')
        self.assertEqual(569, res)

    def test_DLXX(self):
        res = convert_to_arabic('DLXX')
        self.assertEqual(570, res)

    def test_DLXXI(self):
        res = convert_to_arabic('DLXXI')
        self.assertEqual(571, res)

    def test_DLXXII(self):
        res = convert_to_arabic('DLXXII')
        self.assertEqual(572, res)

    def test_DLXXIII(self):
        res = convert_to_arabic('DLXXIII')
        self.assertEqual(573, res)

    def test_DLXXIV(self):
        res = convert_to_arabic('DLXXIV')
        self.assertEqual(574, res)

    def test_DLXXV(self):
        res = convert_to_arabic('DLXXV')
        self.assertEqual(575, res)

    def test_DLXXVI(self):
        res = convert_to_arabic('DLXXVI')
        self.assertEqual(576, res)

    def test_DLXXVII(self):
        res = convert_to_arabic('DLXXVII')
        self.assertEqual(577, res)

    def test_DLXXVIII(self):
        res = convert_to_arabic('DLXXVIII')
        self.assertEqual(578, res)

    def test_DLXXIX(self):
        res = convert_to_arabic('DLXXIX')
        self.assertEqual(579, res)

    def test_DLXXX(self):
        res = convert_to_arabic('DLXXX')
        self.assertEqual(580, res)

    def test_DLXXXI(self):
        res = convert_to_arabic('DLXXXI')
        self.assertEqual(581, res)

    def test_DLXXXII(self):
        res = convert_to_arabic('DLXXXII')
        self.assertEqual(582, res)

    def test_DLXXXIII(self):
        res = convert_to_arabic('DLXXXIII')
        self.assertEqual(583, res)

    def test_DLXXXIV(self):
        res = convert_to_arabic('DLXXXIV')
        self.assertEqual(584, res)

    def test_DLXXXV(self):
        res = convert_to_arabic('DLXXXV')
        self.assertEqual(585, res)

    def test_DLXXXVI(self):
        res = convert_to_arabic('DLXXXVI')
        self.assertEqual(586, res)

    def test_DLXXXVII(self):
        res = convert_to_arabic('DLXXXVII')
        self.assertEqual(587, res)

    def test_DLXXXVIII(self):
        res = convert_to_arabic('DLXXXVIII')
        self.assertEqual(588, res)

    def test_DLXXXIX(self):
        res = convert_to_arabic('DLXXXIX')
        self.assertEqual(589, res)

    def test_DXC(self):
        res = convert_to_arabic('DXC')
        self.assertEqual(590, res)

    def test_DXCI(self):
        res = convert_to_arabic('DXCI')
        self.assertEqual(591, res)

    def test_DXCII(self):
        res = convert_to_arabic('DXCII')
        self.assertEqual(592, res)

    def test_DXCIII(self):
        res = convert_to_arabic('DXCIII')
        self.assertEqual(593, res)

    def test_DXCIV(self):
        res = convert_to_arabic('DXCIV')
        self.assertEqual(594, res)

    def test_DXCV(self):
        res = convert_to_arabic('DXCV')
        self.assertEqual(595, res)

    def test_DXCVI(self):
        res = convert_to_arabic('DXCVI')
        self.assertEqual(596, res)

    def test_DXCVII(self):
        res = convert_to_arabic('DXCVII')
        self.assertEqual(597, res)

    def test_DXCVIII(self):
        res = convert_to_arabic('DXCVIII')
        self.assertEqual(598, res)

    def test_DXCIX(self):
        res = convert_to_arabic('DXCIX')
        self.assertEqual(599, res)

    def test_DC(self):
        res = convert_to_arabic('DC')
        self.assertEqual(600, res)

    def test_DCI(self):
        res = convert_to_arabic('DCI')
        self.assertEqual(601, res)

    def test_DCII(self):
        res = convert_to_arabic('DCII')
        self.assertEqual(602, res)

    def test_DCIII(self):
        res = convert_to_arabic('DCIII')
        self.assertEqual(603, res)

    def test_DCIV(self):
        res = convert_to_arabic('DCIV')
        self.assertEqual(604, res)

    def test_DCV(self):
        res = convert_to_arabic('DCV')
        self.assertEqual(605, res)

    def test_DCVI(self):
        res = convert_to_arabic('DCVI')
        self.assertEqual(606, res)

    def test_DCVII(self):
        res = convert_to_arabic('DCVII')
        self.assertEqual(607, res)

    def test_DCVIII(self):
        res = convert_to_arabic('DCVIII')
        self.assertEqual(608, res)

    def test_DCIX(self):
        res = convert_to_arabic('DCIX')
        self.assertEqual(609, res)

    def test_DCX(self):
        res = convert_to_arabic('DCX')
        self.assertEqual(610, res)

    def test_DCXI(self):
        res = convert_to_arabic('DCXI')
        self.assertEqual(611, res)

    def test_DCXII(self):
        res = convert_to_arabic('DCXII')
        self.assertEqual(612, res)

    def test_DCXIII(self):
        res = convert_to_arabic('DCXIII')
        self.assertEqual(613, res)

    def test_DCXIV(self):
        res = convert_to_arabic('DCXIV')
        self.assertEqual(614, res)

    def test_DCXV(self):
        res = convert_to_arabic('DCXV')
        self.assertEqual(615, res)

    def test_DCXVI(self):
        res = convert_to_arabic('DCXVI')
        self.assertEqual(616, res)

    def test_DCXVII(self):
        res = convert_to_arabic('DCXVII')
        self.assertEqual(617, res)

    def test_DCXVIII(self):
        res = convert_to_arabic('DCXVIII')
        self.assertEqual(618, res)

    def test_DCXIX(self):
        res = convert_to_arabic('DCXIX')
        self.assertEqual(619, res)

    def test_DCXX(self):
        res = convert_to_arabic('DCXX')
        self.assertEqual(620, res)

    def test_DCXXI(self):
        res = convert_to_arabic('DCXXI')
        self.assertEqual(621, res)

    def test_DCXXII(self):
        res = convert_to_arabic('DCXXII')
        self.assertEqual(622, res)

    def test_DCXXIII(self):
        res = convert_to_arabic('DCXXIII')
        self.assertEqual(623, res)

    def test_DCXXIV(self):
        res = convert_to_arabic('DCXXIV')
        self.assertEqual(624, res)

    def test_DCXXV(self):
        res = convert_to_arabic('DCXXV')
        self.assertEqual(625, res)

    def test_DCXXVI(self):
        res = convert_to_arabic('DCXXVI')
        self.assertEqual(626, res)

    def test_DCXXVII(self):
        res = convert_to_arabic('DCXXVII')
        self.assertEqual(627, res)

    def test_DCXXVIII(self):
        res = convert_to_arabic('DCXXVIII')
        self.assertEqual(628, res)

    def test_DCXXIX(self):
        res = convert_to_arabic('DCXXIX')
        self.assertEqual(629, res)

    def test_DCXXX(self):
        res = convert_to_arabic('DCXXX')
        self.assertEqual(630, res)

    def test_DCXXXI(self):
        res = convert_to_arabic('DCXXXI')
        self.assertEqual(631, res)

    def test_DCXXXII(self):
        res = convert_to_arabic('DCXXXII')
        self.assertEqual(632, res)

    def test_DCXXXIII(self):
        res = convert_to_arabic('DCXXXIII')
        self.assertEqual(633, res)

    def test_DCXXXIV(self):
        res = convert_to_arabic('DCXXXIV')
        self.assertEqual(634, res)

    def test_DCXXXV(self):
        res = convert_to_arabic('DCXXXV')
        self.assertEqual(635, res)

    def test_DCXXXVI(self):
        res = convert_to_arabic('DCXXXVI')
        self.assertEqual(636, res)

    def test_DCXXXVII(self):
        res = convert_to_arabic('DCXXXVII')
        self.assertEqual(637, res)

    def test_DCXXXVIII(self):
        res = convert_to_arabic('DCXXXVIII')
        self.assertEqual(638, res)

    def test_DCXXXIX(self):
        res = convert_to_arabic('DCXXXIX')
        self.assertEqual(639, res)

    def test_DCXL(self):
        res = convert_to_arabic('DCXL')
        self.assertEqual(640, res)

    def test_DCXLI(self):
        res = convert_to_arabic('DCXLI')
        self.assertEqual(641, res)

    def test_DCXLII(self):
        res = convert_to_arabic('DCXLII')
        self.assertEqual(642, res)

    def test_DCXLIII(self):
        res = convert_to_arabic('DCXLIII')
        self.assertEqual(643, res)

    def test_DCXLIV(self):
        res = convert_to_arabic('DCXLIV')
        self.assertEqual(644, res)

    def test_DCXLV(self):
        res = convert_to_arabic('DCXLV')
        self.assertEqual(645, res)

    def test_DCXLVI(self):
        res = convert_to_arabic('DCXLVI')
        self.assertEqual(646, res)

    def test_DCXLVII(self):
        res = convert_to_arabic('DCXLVII')
        self.assertEqual(647, res)

    def test_DCXLVIII(self):
        res = convert_to_arabic('DCXLVIII')
        self.assertEqual(648, res)

    def test_DCXLIX(self):
        res = convert_to_arabic('DCXLIX')
        self.assertEqual(649, res)

    def test_DCL(self):
        res = convert_to_arabic('DCL')
        self.assertEqual(650, res)

    def test_DCLI(self):
        res = convert_to_arabic('DCLI')
        self.assertEqual(651, res)

    def test_DCLII(self):
        res = convert_to_arabic('DCLII')
        self.assertEqual(652, res)

    def test_DCLIII(self):
        res = convert_to_arabic('DCLIII')
        self.assertEqual(653, res)

    def test_DCLIV(self):
        res = convert_to_arabic('DCLIV')
        self.assertEqual(654, res)

    def test_DCLV(self):
        res = convert_to_arabic('DCLV')
        self.assertEqual(655, res)

    def test_DCLVI(self):
        res = convert_to_arabic('DCLVI')
        self.assertEqual(656, res)

    def test_DCLVII(self):
        res = convert_to_arabic('DCLVII')
        self.assertEqual(657, res)

    def test_DCLVIII(self):
        res = convert_to_arabic('DCLVIII')
        self.assertEqual(658, res)

    def test_DCLIX(self):
        res = convert_to_arabic('DCLIX')
        self.assertEqual(659, res)

    def test_DCLX(self):
        res = convert_to_arabic('DCLX')
        self.assertEqual(660, res)

    def test_DCLXI(self):
        res = convert_to_arabic('DCLXI')
        self.assertEqual(661, res)

    def test_DCLXII(self):
        res = convert_to_arabic('DCLXII')
        self.assertEqual(662, res)

    def test_DCLXIII(self):
        res = convert_to_arabic('DCLXIII')
        self.assertEqual(663, res)

    def test_DCLXIV(self):
        res = convert_to_arabic('DCLXIV')
        self.assertEqual(664, res)

    def test_DCLXV(self):
        res = convert_to_arabic('DCLXV')
        self.assertEqual(665, res)

    def test_DCLXVI(self):
        res = convert_to_arabic('DCLXVI')
        self.assertEqual(666, res)

    def test_DCLXVII(self):
        res = convert_to_arabic('DCLXVII')
        self.assertEqual(667, res)

    def test_DCLXVIII(self):
        res = convert_to_arabic('DCLXVIII')
        self.assertEqual(668, res)

    def test_DCLXIX(self):
        res = convert_to_arabic('DCLXIX')
        self.assertEqual(669, res)

    def test_DCLXX(self):
        res = convert_to_arabic('DCLXX')
        self.assertEqual(670, res)

    def test_DCLXXI(self):
        res = convert_to_arabic('DCLXXI')
        self.assertEqual(671, res)

    def test_DCLXXII(self):
        res = convert_to_arabic('DCLXXII')
        self.assertEqual(672, res)

    def test_DCLXXIII(self):
        res = convert_to_arabic('DCLXXIII')
        self.assertEqual(673, res)

    def test_DCLXXIV(self):
        res = convert_to_arabic('DCLXXIV')
        self.assertEqual(674, res)

    def test_DCLXXV(self):
        res = convert_to_arabic('DCLXXV')
        self.assertEqual(675, res)

    def test_DCLXXVI(self):
        res = convert_to_arabic('DCLXXVI')
        self.assertEqual(676, res)

    def test_DCLXXVII(self):
        res = convert_to_arabic('DCLXXVII')
        self.assertEqual(677, res)

    def test_DCLXXVIII(self):
        res = convert_to_arabic('DCLXXVIII')
        self.assertEqual(678, res)

    def test_DCLXXIX(self):
        res = convert_to_arabic('DCLXXIX')
        self.assertEqual(679, res)

    def test_DCLXXX(self):
        res = convert_to_arabic('DCLXXX')
        self.assertEqual(680, res)

    def test_DCLXXXI(self):
        res = convert_to_arabic('DCLXXXI')
        self.assertEqual(681, res)

    def test_DCLXXXII(self):
        res = convert_to_arabic('DCLXXXII')
        self.assertEqual(682, res)

    def test_DCLXXXIII(self):
        res = convert_to_arabic('DCLXXXIII')
        self.assertEqual(683, res)

    def test_DCLXXXIV(self):
        res = convert_to_arabic('DCLXXXIV')
        self.assertEqual(684, res)

    def test_DCLXXXV(self):
        res = convert_to_arabic('DCLXXXV')
        self.assertEqual(685, res)

    def test_DCLXXXVI(self):
        res = convert_to_arabic('DCLXXXVI')
        self.assertEqual(686, res)

    def test_DCLXXXVII(self):
        res = convert_to_arabic('DCLXXXVII')
        self.assertEqual(687, res)

    def test_DCLXXXVIII(self):
        res = convert_to_arabic('DCLXXXVIII')
        self.assertEqual(688, res)

    def test_DCLXXXIX(self):
        res = convert_to_arabic('DCLXXXIX')
        self.assertEqual(689, res)

    def test_DCXC(self):
        res = convert_to_arabic('DCXC')
        self.assertEqual(690, res)

    def test_DCXCI(self):
        res = convert_to_arabic('DCXCI')
        self.assertEqual(691, res)

    def test_DCXCII(self):
        res = convert_to_arabic('DCXCII')
        self.assertEqual(692, res)

    def test_DCXCIII(self):
        res = convert_to_arabic('DCXCIII')
        self.assertEqual(693, res)

    def test_DCXCIV(self):
        res = convert_to_arabic('DCXCIV')
        self.assertEqual(694, res)

    def test_DCXCV(self):
        res = convert_to_arabic('DCXCV')
        self.assertEqual(695, res)

    def test_DCXCVI(self):
        res = convert_to_arabic('DCXCVI')
        self.assertEqual(696, res)

    def test_DCXCVII(self):
        res = convert_to_arabic('DCXCVII')
        self.assertEqual(697, res)

    def test_DCXCVIII(self):
        res = convert_to_arabic('DCXCVIII')
        self.assertEqual(698, res)

    def test_DCXCIX(self):
        res = convert_to_arabic('DCXCIX')
        self.assertEqual(699, res)

    def test_DCC(self):
        res = convert_to_arabic('DCC')
        self.assertEqual(700, res)

    def test_DCCI(self):
        res = convert_to_arabic('DCCI')
        self.assertEqual(701, res)

    def test_DCCII(self):
        res = convert_to_arabic('DCCII')
        self.assertEqual(702, res)

    def test_DCCIII(self):
        res = convert_to_arabic('DCCIII')
        self.assertEqual(703, res)

    def test_DCCIV(self):
        res = convert_to_arabic('DCCIV')
        self.assertEqual(704, res)

    def test_DCCV(self):
        res = convert_to_arabic('DCCV')
        self.assertEqual(705, res)

    def test_DCCVI(self):
        res = convert_to_arabic('DCCVI')
        self.assertEqual(706, res)

    def test_DCCVII(self):
        res = convert_to_arabic('DCCVII')
        self.assertEqual(707, res)

    def test_DCCVIII(self):
        res = convert_to_arabic('DCCVIII')
        self.assertEqual(708, res)

    def test_DCCIX(self):
        res = convert_to_arabic('DCCIX')
        self.assertEqual(709, res)

    def test_DCCX(self):
        res = convert_to_arabic('DCCX')
        self.assertEqual(710, res)

    def test_DCCXI(self):
        res = convert_to_arabic('DCCXI')
        self.assertEqual(711, res)

    def test_DCCXII(self):
        res = convert_to_arabic('DCCXII')
        self.assertEqual(712, res)

    def test_DCCXIII(self):
        res = convert_to_arabic('DCCXIII')
        self.assertEqual(713, res)

    def test_DCCXIV(self):
        res = convert_to_arabic('DCCXIV')
        self.assertEqual(714, res)

    def test_DCCXV(self):
        res = convert_to_arabic('DCCXV')
        self.assertEqual(715, res)

    def test_DCCXVI(self):
        res = convert_to_arabic('DCCXVI')
        self.assertEqual(716, res)

    def test_DCCXVII(self):
        res = convert_to_arabic('DCCXVII')
        self.assertEqual(717, res)

    def test_DCCXVIII(self):
        res = convert_to_arabic('DCCXVIII')
        self.assertEqual(718, res)

    def test_DCCXIX(self):
        res = convert_to_arabic('DCCXIX')
        self.assertEqual(719, res)

    def test_DCCXX(self):
        res = convert_to_arabic('DCCXX')
        self.assertEqual(720, res)

    def test_DCCXXI(self):
        res = convert_to_arabic('DCCXXI')
        self.assertEqual(721, res)

    def test_DCCXXII(self):
        res = convert_to_arabic('DCCXXII')
        self.assertEqual(722, res)

    def test_DCCXXIII(self):
        res = convert_to_arabic('DCCXXIII')
        self.assertEqual(723, res)

    def test_DCCXXIV(self):
        res = convert_to_arabic('DCCXXIV')
        self.assertEqual(724, res)

    def test_DCCXXV(self):
        res = convert_to_arabic('DCCXXV')
        self.assertEqual(725, res)

    def test_DCCXXVI(self):
        res = convert_to_arabic('DCCXXVI')
        self.assertEqual(726, res)

    def test_DCCXXVII(self):
        res = convert_to_arabic('DCCXXVII')
        self.assertEqual(727, res)

    def test_DCCXXVIII(self):
        res = convert_to_arabic('DCCXXVIII')
        self.assertEqual(728, res)

    def test_DCCXXIX(self):
        res = convert_to_arabic('DCCXXIX')
        self.assertEqual(729, res)

    def test_DCCXXX(self):
        res = convert_to_arabic('DCCXXX')
        self.assertEqual(730, res)

    def test_DCCXXXI(self):
        res = convert_to_arabic('DCCXXXI')
        self.assertEqual(731, res)

    def test_DCCXXXII(self):
        res = convert_to_arabic('DCCXXXII')
        self.assertEqual(732, res)

    def test_DCCXXXIII(self):
        res = convert_to_arabic('DCCXXXIII')
        self.assertEqual(733, res)

    def test_DCCXXXIV(self):
        res = convert_to_arabic('DCCXXXIV')
        self.assertEqual(734, res)

    def test_DCCXXXV(self):
        res = convert_to_arabic('DCCXXXV')
        self.assertEqual(735, res)

    def test_DCCXXXVI(self):
        res = convert_to_arabic('DCCXXXVI')
        self.assertEqual(736, res)

    def test_DCCXXXVII(self):
        res = convert_to_arabic('DCCXXXVII')
        self.assertEqual(737, res)

    def test_DCCXXXVIII(self):
        res = convert_to_arabic('DCCXXXVIII')
        self.assertEqual(738, res)

    def test_DCCXXXIX(self):
        res = convert_to_arabic('DCCXXXIX')
        self.assertEqual(739, res)

    def test_DCCXL(self):
        res = convert_to_arabic('DCCXL')
        self.assertEqual(740, res)

    def test_DCCXLI(self):
        res = convert_to_arabic('DCCXLI')
        self.assertEqual(741, res)

    def test_DCCXLII(self):
        res = convert_to_arabic('DCCXLII')
        self.assertEqual(742, res)

    def test_DCCXLIII(self):
        res = convert_to_arabic('DCCXLIII')
        self.assertEqual(743, res)

    def test_DCCXLIV(self):
        res = convert_to_arabic('DCCXLIV')
        self.assertEqual(744, res)

    def test_DCCXLV(self):
        res = convert_to_arabic('DCCXLV')
        self.assertEqual(745, res)

    def test_DCCXLVI(self):
        res = convert_to_arabic('DCCXLVI')
        self.assertEqual(746, res)

    def test_DCCXLVII(self):
        res = convert_to_arabic('DCCXLVII')
        self.assertEqual(747, res)

    def test_DCCXLVIII(self):
        res = convert_to_arabic('DCCXLVIII')
        self.assertEqual(748, res)

    def test_DCCXLIX(self):
        res = convert_to_arabic('DCCXLIX')
        self.assertEqual(749, res)

    def test_DCCL(self):
        res = convert_to_arabic('DCCL')
        self.assertEqual(750, res)

    def test_DCCLI(self):
        res = convert_to_arabic('DCCLI')
        self.assertEqual(751, res)

    def test_DCCLII(self):
        res = convert_to_arabic('DCCLII')
        self.assertEqual(752, res)

    def test_DCCLIII(self):
        res = convert_to_arabic('DCCLIII')
        self.assertEqual(753, res)

    def test_DCCLIV(self):
        res = convert_to_arabic('DCCLIV')
        self.assertEqual(754, res)

    def test_DCCLV(self):
        res = convert_to_arabic('DCCLV')
        self.assertEqual(755, res)

    def test_DCCLVI(self):
        res = convert_to_arabic('DCCLVI')
        self.assertEqual(756, res)

    def test_DCCLVII(self):
        res = convert_to_arabic('DCCLVII')
        self.assertEqual(757, res)

    def test_DCCLVIII(self):
        res = convert_to_arabic('DCCLVIII')
        self.assertEqual(758, res)

    def test_DCCLIX(self):
        res = convert_to_arabic('DCCLIX')
        self.assertEqual(759, res)

    def test_DCCLX(self):
        res = convert_to_arabic('DCCLX')
        self.assertEqual(760, res)

    def test_DCCLXI(self):
        res = convert_to_arabic('DCCLXI')
        self.assertEqual(761, res)

    def test_DCCLXII(self):
        res = convert_to_arabic('DCCLXII')
        self.assertEqual(762, res)

    def test_DCCLXIII(self):
        res = convert_to_arabic('DCCLXIII')
        self.assertEqual(763, res)

    def test_DCCLXIV(self):
        res = convert_to_arabic('DCCLXIV')
        self.assertEqual(764, res)

    def test_DCCLXV(self):
        res = convert_to_arabic('DCCLXV')
        self.assertEqual(765, res)

    def test_DCCLXVI(self):
        res = convert_to_arabic('DCCLXVI')
        self.assertEqual(766, res)

    def test_DCCLXVII(self):
        res = convert_to_arabic('DCCLXVII')
        self.assertEqual(767, res)

    def test_DCCLXVIII(self):
        res = convert_to_arabic('DCCLXVIII')
        self.assertEqual(768, res)

    def test_DCCLXIX(self):
        res = convert_to_arabic('DCCLXIX')
        self.assertEqual(769, res)

    def test_DCCLXX(self):
        res = convert_to_arabic('DCCLXX')
        self.assertEqual(770, res)

    def test_DCCLXXI(self):
        res = convert_to_arabic('DCCLXXI')
        self.assertEqual(771, res)

    def test_DCCLXXII(self):
        res = convert_to_arabic('DCCLXXII')
        self.assertEqual(772, res)

    def test_DCCLXXIII(self):
        res = convert_to_arabic('DCCLXXIII')
        self.assertEqual(773, res)

    def test_DCCLXXIV(self):
        res = convert_to_arabic('DCCLXXIV')
        self.assertEqual(774, res)

    def test_DCCLXXV(self):
        res = convert_to_arabic('DCCLXXV')
        self.assertEqual(775, res)

    def test_DCCLXXVI(self):
        res = convert_to_arabic('DCCLXXVI')
        self.assertEqual(776, res)

    def test_DCCLXXVII(self):
        res = convert_to_arabic('DCCLXXVII')
        self.assertEqual(777, res)

    def test_DCCLXXVIII(self):
        res = convert_to_arabic('DCCLXXVIII')
        self.assertEqual(778, res)

    def test_DCCLXXIX(self):
        res = convert_to_arabic('DCCLXXIX')
        self.assertEqual(779, res)

    def test_DCCLXXX(self):
        res = convert_to_arabic('DCCLXXX')
        self.assertEqual(780, res)

    def test_DCCLXXXI(self):
        res = convert_to_arabic('DCCLXXXI')
        self.assertEqual(781, res)

    def test_DCCLXXXII(self):
        res = convert_to_arabic('DCCLXXXII')
        self.assertEqual(782, res)

    def test_DCCLXXXIII(self):
        res = convert_to_arabic('DCCLXXXIII')
        self.assertEqual(783, res)

    def test_DCCLXXXIV(self):
        res = convert_to_arabic('DCCLXXXIV')
        self.assertEqual(784, res)

    def test_DCCLXXXV(self):
        res = convert_to_arabic('DCCLXXXV')
        self.assertEqual(785, res)

    def test_DCCLXXXVI(self):
        res = convert_to_arabic('DCCLXXXVI')
        self.assertEqual(786, res)

    def test_DCCLXXXVII(self):
        res = convert_to_arabic('DCCLXXXVII')
        self.assertEqual(787, res)

    def test_DCCLXXXVIII(self):
        res = convert_to_arabic('DCCLXXXVIII')
        self.assertEqual(788, res)

    def test_DCCLXXXIX(self):
        res = convert_to_arabic('DCCLXXXIX')
        self.assertEqual(789, res)

    def test_DCCXC(self):
        res = convert_to_arabic('DCCXC')
        self.assertEqual(790, res)

    def test_DCCXCI(self):
        res = convert_to_arabic('DCCXCI')
        self.assertEqual(791, res)

    def test_DCCXCII(self):
        res = convert_to_arabic('DCCXCII')
        self.assertEqual(792, res)

    def test_DCCXCIII(self):
        res = convert_to_arabic('DCCXCIII')
        self.assertEqual(793, res)

    def test_DCCXCIV(self):
        res = convert_to_arabic('DCCXCIV')
        self.assertEqual(794, res)

    def test_DCCXCV(self):
        res = convert_to_arabic('DCCXCV')
        self.assertEqual(795, res)

    def test_DCCXCVI(self):
        res = convert_to_arabic('DCCXCVI')
        self.assertEqual(796, res)

    def test_DCCXCVII(self):
        res = convert_to_arabic('DCCXCVII')
        self.assertEqual(797, res)

    def test_DCCXCVIII(self):
        res = convert_to_arabic('DCCXCVIII')
        self.assertEqual(798, res)

    def test_DCCXCIX(self):
        res = convert_to_arabic('DCCXCIX')
        self.assertEqual(799, res)

    def test_DCCC(self):
        res = convert_to_arabic('DCCC')
        self.assertEqual(800, res)

    def test_DCCCI(self):
        res = convert_to_arabic('DCCCI')
        self.assertEqual(801, res)

    def test_DCCCII(self):
        res = convert_to_arabic('DCCCII')
        self.assertEqual(802, res)

    def test_DCCCIII(self):
        res = convert_to_arabic('DCCCIII')
        self.assertEqual(803, res)

    def test_DCCCIV(self):
        res = convert_to_arabic('DCCCIV')
        self.assertEqual(804, res)

    def test_DCCCV(self):
        res = convert_to_arabic('DCCCV')
        self.assertEqual(805, res)

    def test_DCCCVI(self):
        res = convert_to_arabic('DCCCVI')
        self.assertEqual(806, res)

    def test_DCCCVII(self):
        res = convert_to_arabic('DCCCVII')
        self.assertEqual(807, res)

    def test_DCCCVIII(self):
        res = convert_to_arabic('DCCCVIII')
        self.assertEqual(808, res)

    def test_DCCCIX(self):
        res = convert_to_arabic('DCCCIX')
        self.assertEqual(809, res)

    def test_DCCCX(self):
        res = convert_to_arabic('DCCCX')
        self.assertEqual(810, res)

    def test_DCCCXI(self):
        res = convert_to_arabic('DCCCXI')
        self.assertEqual(811, res)

    def test_DCCCXII(self):
        res = convert_to_arabic('DCCCXII')
        self.assertEqual(812, res)

    def test_DCCCXIII(self):
        res = convert_to_arabic('DCCCXIII')
        self.assertEqual(813, res)

    def test_DCCCXIV(self):
        res = convert_to_arabic('DCCCXIV')
        self.assertEqual(814, res)

    def test_DCCCXV(self):
        res = convert_to_arabic('DCCCXV')
        self.assertEqual(815, res)

    def test_DCCCXVI(self):
        res = convert_to_arabic('DCCCXVI')
        self.assertEqual(816, res)

    def test_DCCCXVII(self):
        res = convert_to_arabic('DCCCXVII')
        self.assertEqual(817, res)

    def test_DCCCXVIII(self):
        res = convert_to_arabic('DCCCXVIII')
        self.assertEqual(818, res)

    def test_DCCCXIX(self):
        res = convert_to_arabic('DCCCXIX')
        self.assertEqual(819, res)

    def test_DCCCXX(self):
        res = convert_to_arabic('DCCCXX')
        self.assertEqual(820, res)

    def test_DCCCXXI(self):
        res = convert_to_arabic('DCCCXXI')
        self.assertEqual(821, res)

    def test_DCCCXXII(self):
        res = convert_to_arabic('DCCCXXII')
        self.assertEqual(822, res)

    def test_DCCCXXIII(self):
        res = convert_to_arabic('DCCCXXIII')
        self.assertEqual(823, res)

    def test_DCCCXXIV(self):
        res = convert_to_arabic('DCCCXXIV')
        self.assertEqual(824, res)

    def test_DCCCXXV(self):
        res = convert_to_arabic('DCCCXXV')
        self.assertEqual(825, res)

    def test_DCCCXXVI(self):
        res = convert_to_arabic('DCCCXXVI')
        self.assertEqual(826, res)

    def test_DCCCXXVII(self):
        res = convert_to_arabic('DCCCXXVII')
        self.assertEqual(827, res)

    def test_DCCCXXVIII(self):
        res = convert_to_arabic('DCCCXXVIII')
        self.assertEqual(828, res)

    def test_DCCCXXIX(self):
        res = convert_to_arabic('DCCCXXIX')
        self.assertEqual(829, res)

    def test_DCCCXXX(self):
        res = convert_to_arabic('DCCCXXX')
        self.assertEqual(830, res)

    def test_DCCCXXXI(self):
        res = convert_to_arabic('DCCCXXXI')
        self.assertEqual(831, res)

    def test_DCCCXXXII(self):
        res = convert_to_arabic('DCCCXXXII')
        self.assertEqual(832, res)

    def test_DCCCXXXIII(self):
        res = convert_to_arabic('DCCCXXXIII')
        self.assertEqual(833, res)

    def test_DCCCXXXIV(self):
        res = convert_to_arabic('DCCCXXXIV')
        self.assertEqual(834, res)

    def test_DCCCXXXV(self):
        res = convert_to_arabic('DCCCXXXV')
        self.assertEqual(835, res)

    def test_DCCCXXXVI(self):
        res = convert_to_arabic('DCCCXXXVI')
        self.assertEqual(836, res)

    def test_DCCCXXXVII(self):
        res = convert_to_arabic('DCCCXXXVII')
        self.assertEqual(837, res)

    def test_DCCCXXXVIII(self):
        res = convert_to_arabic('DCCCXXXVIII')
        self.assertEqual(838, res)

    def test_DCCCXXXIX(self):
        res = convert_to_arabic('DCCCXXXIX')
        self.assertEqual(839, res)

    def test_DCCCXL(self):
        res = convert_to_arabic('DCCCXL')
        self.assertEqual(840, res)

    def test_DCCCXLI(self):
        res = convert_to_arabic('DCCCXLI')
        self.assertEqual(841, res)

    def test_DCCCXLII(self):
        res = convert_to_arabic('DCCCXLII')
        self.assertEqual(842, res)

    def test_DCCCXLIII(self):
        res = convert_to_arabic('DCCCXLIII')
        self.assertEqual(843, res)

    def test_DCCCXLIV(self):
        res = convert_to_arabic('DCCCXLIV')
        self.assertEqual(844, res)

    def test_DCCCXLV(self):
        res = convert_to_arabic('DCCCXLV')
        self.assertEqual(845, res)

    def test_DCCCXLVI(self):
        res = convert_to_arabic('DCCCXLVI')
        self.assertEqual(846, res)

    def test_DCCCXLVII(self):
        res = convert_to_arabic('DCCCXLVII')
        self.assertEqual(847, res)

    def test_DCCCXLVIII(self):
        res = convert_to_arabic('DCCCXLVIII')
        self.assertEqual(848, res)

    def test_DCCCXLIX(self):
        res = convert_to_arabic('DCCCXLIX')
        self.assertEqual(849, res)

    def test_DCCCL(self):
        res = convert_to_arabic('DCCCL')
        self.assertEqual(850, res)

    def test_DCCCLI(self):
        res = convert_to_arabic('DCCCLI')
        self.assertEqual(851, res)

    def test_DCCCLII(self):
        res = convert_to_arabic('DCCCLII')
        self.assertEqual(852, res)

    def test_DCCCLIII(self):
        res = convert_to_arabic('DCCCLIII')
        self.assertEqual(853, res)

    def test_DCCCLIV(self):
        res = convert_to_arabic('DCCCLIV')
        self.assertEqual(854, res)

    def test_DCCCLV(self):
        res = convert_to_arabic('DCCCLV')
        self.assertEqual(855, res)

    def test_DCCCLVI(self):
        res = convert_to_arabic('DCCCLVI')
        self.assertEqual(856, res)

    def test_DCCCLVII(self):
        res = convert_to_arabic('DCCCLVII')
        self.assertEqual(857, res)

    def test_DCCCLVIII(self):
        res = convert_to_arabic('DCCCLVIII')
        self.assertEqual(858, res)

    def test_DCCCLIX(self):
        res = convert_to_arabic('DCCCLIX')
        self.assertEqual(859, res)

    def test_DCCCLX(self):
        res = convert_to_arabic('DCCCLX')
        self.assertEqual(860, res)

    def test_DCCCLXI(self):
        res = convert_to_arabic('DCCCLXI')
        self.assertEqual(861, res)

    def test_DCCCLXII(self):
        res = convert_to_arabic('DCCCLXII')
        self.assertEqual(862, res)

    def test_DCCCLXIII(self):
        res = convert_to_arabic('DCCCLXIII')
        self.assertEqual(863, res)

    def test_DCCCLXIV(self):
        res = convert_to_arabic('DCCCLXIV')
        self.assertEqual(864, res)

    def test_DCCCLXV(self):
        res = convert_to_arabic('DCCCLXV')
        self.assertEqual(865, res)

    def test_DCCCLXVI(self):
        res = convert_to_arabic('DCCCLXVI')
        self.assertEqual(866, res)

    def test_DCCCLXVII(self):
        res = convert_to_arabic('DCCCLXVII')
        self.assertEqual(867, res)

    def test_DCCCLXVIII(self):
        res = convert_to_arabic('DCCCLXVIII')
        self.assertEqual(868, res)

    def test_DCCCLXIX(self):
        res = convert_to_arabic('DCCCLXIX')
        self.assertEqual(869, res)

    def test_DCCCLXX(self):
        res = convert_to_arabic('DCCCLXX')
        self.assertEqual(870, res)

    def test_DCCCLXXI(self):
        res = convert_to_arabic('DCCCLXXI')
        self.assertEqual(871, res)

    def test_DCCCLXXII(self):
        res = convert_to_arabic('DCCCLXXII')
        self.assertEqual(872, res)

    def test_DCCCLXXIII(self):
        res = convert_to_arabic('DCCCLXXIII')
        self.assertEqual(873, res)

    def test_DCCCLXXIV(self):
        res = convert_to_arabic('DCCCLXXIV')
        self.assertEqual(874, res)

    def test_DCCCLXXV(self):
        res = convert_to_arabic('DCCCLXXV')
        self.assertEqual(875, res)

    def test_DCCCLXXVI(self):
        res = convert_to_arabic('DCCCLXXVI')
        self.assertEqual(876, res)

    def test_DCCCLXXVII(self):
        res = convert_to_arabic('DCCCLXXVII')
        self.assertEqual(877, res)

    def test_DCCCLXXVIII(self):
        res = convert_to_arabic('DCCCLXXVIII')
        self.assertEqual(878, res)

    def test_DCCCLXXIX(self):
        res = convert_to_arabic('DCCCLXXIX')
        self.assertEqual(879, res)

    def test_DCCCLXXX(self):
        res = convert_to_arabic('DCCCLXXX')
        self.assertEqual(880, res)

    def test_DCCCLXXXI(self):
        res = convert_to_arabic('DCCCLXXXI')
        self.assertEqual(881, res)

    def test_DCCCLXXXII(self):
        res = convert_to_arabic('DCCCLXXXII')
        self.assertEqual(882, res)

    def test_DCCCLXXXIII(self):
        res = convert_to_arabic('DCCCLXXXIII')
        self.assertEqual(883, res)

    def test_DCCCLXXXIV(self):
        res = convert_to_arabic('DCCCLXXXIV')
        self.assertEqual(884, res)

    def test_DCCCLXXXV(self):
        res = convert_to_arabic('DCCCLXXXV')
        self.assertEqual(885, res)

    def test_DCCCLXXXVI(self):
        res = convert_to_arabic('DCCCLXXXVI')
        self.assertEqual(886, res)

    def test_DCCCLXXXVII(self):
        res = convert_to_arabic('DCCCLXXXVII')
        self.assertEqual(887, res)

    def test_DCCCLXXXVIII(self):
        res = convert_to_arabic('DCCCLXXXVIII')
        self.assertEqual(888, res)

    def test_DCCCLXXXIX(self):
        res = convert_to_arabic('DCCCLXXXIX')
        self.assertEqual(889, res)

    def test_DCCCXC(self):
        res = convert_to_arabic('DCCCXC')
        self.assertEqual(890, res)

    def test_DCCCXCI(self):
        res = convert_to_arabic('DCCCXCI')
        self.assertEqual(891, res)

    def test_DCCCXCII(self):
        res = convert_to_arabic('DCCCXCII')
        self.assertEqual(892, res)

    def test_DCCCXCIII(self):
        res = convert_to_arabic('DCCCXCIII')
        self.assertEqual(893, res)

    def test_DCCCXCIV(self):
        res = convert_to_arabic('DCCCXCIV')
        self.assertEqual(894, res)

    def test_DCCCXCV(self):
        res = convert_to_arabic('DCCCXCV')
        self.assertEqual(895, res)

    def test_DCCCXCVI(self):
        res = convert_to_arabic('DCCCXCVI')
        self.assertEqual(896, res)

    def test_DCCCXCVII(self):
        res = convert_to_arabic('DCCCXCVII')
        self.assertEqual(897, res)

    def test_DCCCXCVIII(self):
        res = convert_to_arabic('DCCCXCVIII')
        self.assertEqual(898, res)

    def test_DCCCXCIX(self):
        res = convert_to_arabic('DCCCXCIX')
        self.assertEqual(899, res)

    def test_CM(self):
        res = convert_to_arabic('CM')
        self.assertEqual(900, res)

    def test_CMI(self):
        res = convert_to_arabic('CMI')
        self.assertEqual(901, res)

    def test_CMII(self):
        res = convert_to_arabic('CMII')
        self.assertEqual(902, res)

    def test_CMIII(self):
        res = convert_to_arabic('CMIII')
        self.assertEqual(903, res)

    def test_CMIV(self):
        res = convert_to_arabic('CMIV')
        self.assertEqual(904, res)

    def test_CMV(self):
        res = convert_to_arabic('CMV')
        self.assertEqual(905, res)

    def test_CMVI(self):
        res = convert_to_arabic('CMVI')
        self.assertEqual(906, res)

    def test_CMVII(self):
        res = convert_to_arabic('CMVII')
        self.assertEqual(907, res)

    def test_CMVIII(self):
        res = convert_to_arabic('CMVIII')
        self.assertEqual(908, res)

    def test_CMIX(self):
        res = convert_to_arabic('CMIX')
        self.assertEqual(909, res)

    def test_CMX(self):
        res = convert_to_arabic('CMX')
        self.assertEqual(910, res)

    def test_CMXI(self):
        res = convert_to_arabic('CMXI')
        self.assertEqual(911, res)

    def test_CMXII(self):
        res = convert_to_arabic('CMXII')
        self.assertEqual(912, res)

    def test_CMXIII(self):
        res = convert_to_arabic('CMXIII')
        self.assertEqual(913, res)

    def test_CMXIV(self):
        res = convert_to_arabic('CMXIV')
        self.assertEqual(914, res)

    def test_CMXV(self):
        res = convert_to_arabic('CMXV')
        self.assertEqual(915, res)

    def test_CMXVI(self):
        res = convert_to_arabic('CMXVI')
        self.assertEqual(916, res)

    def test_CMXVII(self):
        res = convert_to_arabic('CMXVII')
        self.assertEqual(917, res)

    def test_CMXVIII(self):
        res = convert_to_arabic('CMXVIII')
        self.assertEqual(918, res)

    def test_CMXIX(self):
        res = convert_to_arabic('CMXIX')
        self.assertEqual(919, res)

    def test_CMXX(self):
        res = convert_to_arabic('CMXX')
        self.assertEqual(920, res)

    def test_CMXXI(self):
        res = convert_to_arabic('CMXXI')
        self.assertEqual(921, res)

    def test_CMXXII(self):
        res = convert_to_arabic('CMXXII')
        self.assertEqual(922, res)

    def test_CMXXIII(self):
        res = convert_to_arabic('CMXXIII')
        self.assertEqual(923, res)

    def test_CMXXIV(self):
        res = convert_to_arabic('CMXXIV')
        self.assertEqual(924, res)

    def test_CMXXV(self):
        res = convert_to_arabic('CMXXV')
        self.assertEqual(925, res)

    def test_CMXXVI(self):
        res = convert_to_arabic('CMXXVI')
        self.assertEqual(926, res)

    def test_CMXXVII(self):
        res = convert_to_arabic('CMXXVII')
        self.assertEqual(927, res)

    def test_CMXXVIII(self):
        res = convert_to_arabic('CMXXVIII')
        self.assertEqual(928, res)

    def test_CMXXIX(self):
        res = convert_to_arabic('CMXXIX')
        self.assertEqual(929, res)

    def test_CMXXX(self):
        res = convert_to_arabic('CMXXX')
        self.assertEqual(930, res)

    def test_CMXXXI(self):
        res = convert_to_arabic('CMXXXI')
        self.assertEqual(931, res)

    def test_CMXXXII(self):
        res = convert_to_arabic('CMXXXII')
        self.assertEqual(932, res)

    def test_CMXXXIII(self):
        res = convert_to_arabic('CMXXXIII')
        self.assertEqual(933, res)

    def test_CMXXXIV(self):
        res = convert_to_arabic('CMXXXIV')
        self.assertEqual(934, res)

    def test_CMXXXV(self):
        res = convert_to_arabic('CMXXXV')
        self.assertEqual(935, res)

    def test_CMXXXVI(self):
        res = convert_to_arabic('CMXXXVI')
        self.assertEqual(936, res)

    def test_CMXXXVII(self):
        res = convert_to_arabic('CMXXXVII')
        self.assertEqual(937, res)

    def test_CMXXXVIII(self):
        res = convert_to_arabic('CMXXXVIII')
        self.assertEqual(938, res)

    def test_CMXXXIX(self):
        res = convert_to_arabic('CMXXXIX')
        self.assertEqual(939, res)

    def test_CMXL(self):
        res = convert_to_arabic('CMXL')
        self.assertEqual(940, res)

    def test_CMXLI(self):
        res = convert_to_arabic('CMXLI')
        self.assertEqual(941, res)

    def test_CMXLII(self):
        res = convert_to_arabic('CMXLII')
        self.assertEqual(942, res)

    def test_CMXLIII(self):
        res = convert_to_arabic('CMXLIII')
        self.assertEqual(943, res)

    def test_CMXLIV(self):
        res = convert_to_arabic('CMXLIV')
        self.assertEqual(944, res)

    def test_CMXLV(self):
        res = convert_to_arabic('CMXLV')
        self.assertEqual(945, res)

    def test_CMXLVI(self):
        res = convert_to_arabic('CMXLVI')
        self.assertEqual(946, res)

    def test_CMXLVII(self):
        res = convert_to_arabic('CMXLVII')
        self.assertEqual(947, res)

    def test_CMXLVIII(self):
        res = convert_to_arabic('CMXLVIII')
        self.assertEqual(948, res)

    def test_CMXLIX(self):
        res = convert_to_arabic('CMXLIX')
        self.assertEqual(949, res)

    def test_CML(self):
        res = convert_to_arabic('CML')
        self.assertEqual(950, res)

    def test_CMLI(self):
        res = convert_to_arabic('CMLI')
        self.assertEqual(951, res)

    def test_CMLII(self):
        res = convert_to_arabic('CMLII')
        self.assertEqual(952, res)

    def test_CMLIII(self):
        res = convert_to_arabic('CMLIII')
        self.assertEqual(953, res)

    def test_CMLIV(self):
        res = convert_to_arabic('CMLIV')
        self.assertEqual(954, res)

    def test_CMLV(self):
        res = convert_to_arabic('CMLV')
        self.assertEqual(955, res)

    def test_CMLVI(self):
        res = convert_to_arabic('CMLVI')
        self.assertEqual(956, res)

    def test_CMLVII(self):
        res = convert_to_arabic('CMLVII')
        self.assertEqual(957, res)

    def test_CMLVIII(self):
        res = convert_to_arabic('CMLVIII')
        self.assertEqual(958, res)

    def test_CMLIX(self):
        res = convert_to_arabic('CMLIX')
        self.assertEqual(959, res)

    def test_CMLX(self):
        res = convert_to_arabic('CMLX')
        self.assertEqual(960, res)

    def test_CMLXI(self):
        res = convert_to_arabic('CMLXI')
        self.assertEqual(961, res)

    def test_CMLXII(self):
        res = convert_to_arabic('CMLXII')
        self.assertEqual(962, res)

    def test_CMLXIII(self):
        res = convert_to_arabic('CMLXIII')
        self.assertEqual(963, res)

    def test_CMLXIV(self):
        res = convert_to_arabic('CMLXIV')
        self.assertEqual(964, res)

    def test_CMLXV(self):
        res = convert_to_arabic('CMLXV')
        self.assertEqual(965, res)

    def test_CMLXVI(self):
        res = convert_to_arabic('CMLXVI')
        self.assertEqual(966, res)

    def test_CMLXVII(self):
        res = convert_to_arabic('CMLXVII')
        self.assertEqual(967, res)

    def test_CMLXVIII(self):
        res = convert_to_arabic('CMLXVIII')
        self.assertEqual(968, res)

    def test_CMLXIX(self):
        res = convert_to_arabic('CMLXIX')
        self.assertEqual(969, res)

    def test_CMLXX(self):
        res = convert_to_arabic('CMLXX')
        self.assertEqual(970, res)

    def test_CMLXXI(self):
        res = convert_to_arabic('CMLXXI')
        self.assertEqual(971, res)

    def test_CMLXXII(self):
        res = convert_to_arabic('CMLXXII')
        self.assertEqual(972, res)

    def test_CMLXXIII(self):
        res = convert_to_arabic('CMLXXIII')
        self.assertEqual(973, res)

    def test_CMLXXIV(self):
        res = convert_to_arabic('CMLXXIV')
        self.assertEqual(974, res)

    def test_CMLXXV(self):
        res = convert_to_arabic('CMLXXV')
        self.assertEqual(975, res)

    def test_CMLXXVI(self):
        res = convert_to_arabic('CMLXXVI')
        self.assertEqual(976, res)

    def test_CMLXXVII(self):
        res = convert_to_arabic('CMLXXVII')
        self.assertEqual(977, res)

    def test_CMLXXVIII(self):
        res = convert_to_arabic('CMLXXVIII')
        self.assertEqual(978, res)

    def test_CMLXXIX(self):
        res = convert_to_arabic('CMLXXIX')
        self.assertEqual(979, res)

    def test_CMLXXX(self):
        res = convert_to_arabic('CMLXXX')
        self.assertEqual(980, res)

    def test_CMLXXXI(self):
        res = convert_to_arabic('CMLXXXI')
        self.assertEqual(981, res)

    def test_CMLXXXII(self):
        res = convert_to_arabic('CMLXXXII')
        self.assertEqual(982, res)

    def test_CMLXXXIII(self):
        res = convert_to_arabic('CMLXXXIII')
        self.assertEqual(983, res)

    def test_CMLXXXIV(self):
        res = convert_to_arabic('CMLXXXIV')
        self.assertEqual(984, res)

    def test_CMLXXXV(self):
        res = convert_to_arabic('CMLXXXV')
        self.assertEqual(985, res)

    def test_CMLXXXVI(self):
        res = convert_to_arabic('CMLXXXVI')
        self.assertEqual(986, res)

    def test_CMLXXXVII(self):
        res = convert_to_arabic('CMLXXXVII')
        self.assertEqual(987, res)

    def test_CMLXXXVIII(self):
        res = convert_to_arabic('CMLXXXVIII')
        self.assertEqual(988, res)

    def test_CMLXXXIX(self):
        res = convert_to_arabic('CMLXXXIX')
        self.assertEqual(989, res)

    def test_CMXC(self):
        res = convert_to_arabic('CMXC')
        self.assertEqual(990, res)

    def test_CMXCI(self):
        res = convert_to_arabic('CMXCI')
        self.assertEqual(991, res)

    def test_CMXCII(self):
        res = convert_to_arabic('CMXCII')
        self.assertEqual(992, res)

    def test_CMXCIII(self):
        res = convert_to_arabic('CMXCIII')
        self.assertEqual(993, res)

    def test_CMXCIV(self):
        res = convert_to_arabic('CMXCIV')
        self.assertEqual(994, res)

    def test_CMXCV(self):
        res = convert_to_arabic('CMXCV')
        self.assertEqual(995, res)

    def test_CMXCVI(self):
        res = convert_to_arabic('CMXCVI')
        self.assertEqual(996, res)

    def test_CMXCVII(self):
        res = convert_to_arabic('CMXCVII')
        self.assertEqual(997, res)

    def test_CMXCVIII(self):
        res = convert_to_arabic('CMXCVIII')
        self.assertEqual(998, res)

    def test_CMXCIX(self):
        res = convert_to_arabic('CMXCIX')
        self.assertEqual(999, res)

    def test_M(self):
        res = convert_to_arabic('M')
        self.assertEqual(1000, res)

    def test_MI(self):
        res = convert_to_arabic('MI')
        self.assertEqual(1001, res)

    def test_MII(self):
        res = convert_to_arabic('MII')
        self.assertEqual(1002, res)

    def test_MIII(self):
        res = convert_to_arabic('MIII')
        self.assertEqual(1003, res)

    def test_MIV(self):
        res = convert_to_arabic('MIV')
        self.assertEqual(1004, res)

    def test_MV(self):
        res = convert_to_arabic('MV')
        self.assertEqual(1005, res)

    def test_MVI(self):
        res = convert_to_arabic('MVI')
        self.assertEqual(1006, res)

    def test_MVII(self):
        res = convert_to_arabic('MVII')
        self.assertEqual(1007, res)

    def test_MVIII(self):
        res = convert_to_arabic('MVIII')
        self.assertEqual(1008, res)

    def test_MIX(self):
        res = convert_to_arabic('MIX')
        self.assertEqual(1009, res)

    def test_MX(self):
        res = convert_to_arabic('MX')
        self.assertEqual(1010, res)

    def test_MXI(self):
        res = convert_to_arabic('MXI')
        self.assertEqual(1011, res)

    def test_MXII(self):
        res = convert_to_arabic('MXII')
        self.assertEqual(1012, res)

    def test_MXIII(self):
        res = convert_to_arabic('MXIII')
        self.assertEqual(1013, res)

    def test_MXIV(self):
        res = convert_to_arabic('MXIV')
        self.assertEqual(1014, res)

    def test_MXV(self):
        res = convert_to_arabic('MXV')
        self.assertEqual(1015, res)

    def test_MXVI(self):
        res = convert_to_arabic('MXVI')
        self.assertEqual(1016, res)

    def test_MXVII(self):
        res = convert_to_arabic('MXVII')
        self.assertEqual(1017, res)

    def test_MXVIII(self):
        res = convert_to_arabic('MXVIII')
        self.assertEqual(1018, res)

    def test_MXIX(self):
        res = convert_to_arabic('MXIX')
        self.assertEqual(1019, res)

    def test_MXX(self):
        res = convert_to_arabic('MXX')
        self.assertEqual(1020, res)

    def test_MXXI(self):
        res = convert_to_arabic('MXXI')
        self.assertEqual(1021, res)

    def test_MXXII(self):
        res = convert_to_arabic('MXXII')
        self.assertEqual(1022, res)

    def test_MXXIII(self):
        res = convert_to_arabic('MXXIII')
        self.assertEqual(1023, res)

    def test_MXXIV(self):
        res = convert_to_arabic('MXXIV')
        self.assertEqual(1024, res)

    def test_MXXV(self):
        res = convert_to_arabic('MXXV')
        self.assertEqual(1025, res)

    def test_MXXVI(self):
        res = convert_to_arabic('MXXVI')
        self.assertEqual(1026, res)

    def test_MXXVII(self):
        res = convert_to_arabic('MXXVII')
        self.assertEqual(1027, res)

    def test_MXXVIII(self):
        res = convert_to_arabic('MXXVIII')
        self.assertEqual(1028, res)

    def test_MXXIX(self):
        res = convert_to_arabic('MXXIX')
        self.assertEqual(1029, res)

    def test_MXXX(self):
        res = convert_to_arabic('MXXX')
        self.assertEqual(1030, res)

    def test_MXXXI(self):
        res = convert_to_arabic('MXXXI')
        self.assertEqual(1031, res)

    def test_MXXXII(self):
        res = convert_to_arabic('MXXXII')
        self.assertEqual(1032, res)

    def test_MXXXIII(self):
        res = convert_to_arabic('MXXXIII')
        self.assertEqual(1033, res)

    def test_MXXXIV(self):
        res = convert_to_arabic('MXXXIV')
        self.assertEqual(1034, res)

    def test_MXXXV(self):
        res = convert_to_arabic('MXXXV')
        self.assertEqual(1035, res)

    def test_MXXXVI(self):
        res = convert_to_arabic('MXXXVI')
        self.assertEqual(1036, res)

    def test_MXXXVII(self):
        res = convert_to_arabic('MXXXVII')
        self.assertEqual(1037, res)

    def test_MXXXVIII(self):
        res = convert_to_arabic('MXXXVIII')
        self.assertEqual(1038, res)

    def test_MXXXIX(self):
        res = convert_to_arabic('MXXXIX')
        self.assertEqual(1039, res)

    def test_MXL(self):
        res = convert_to_arabic('MXL')
        self.assertEqual(1040, res)

    def test_MXLI(self):
        res = convert_to_arabic('MXLI')
        self.assertEqual(1041, res)

    def test_MXLII(self):
        res = convert_to_arabic('MXLII')
        self.assertEqual(1042, res)

    def test_MXLIII(self):
        res = convert_to_arabic('MXLIII')
        self.assertEqual(1043, res)

    def test_MXLIV(self):
        res = convert_to_arabic('MXLIV')
        self.assertEqual(1044, res)

    def test_MXLV(self):
        res = convert_to_arabic('MXLV')
        self.assertEqual(1045, res)

    def test_MXLVI(self):
        res = convert_to_arabic('MXLVI')
        self.assertEqual(1046, res)

    def test_MXLVII(self):
        res = convert_to_arabic('MXLVII')
        self.assertEqual(1047, res)

    def test_MXLVIII(self):
        res = convert_to_arabic('MXLVIII')
        self.assertEqual(1048, res)

    def test_MXLIX(self):
        res = convert_to_arabic('MXLIX')
        self.assertEqual(1049, res)

    def test_ML(self):
        res = convert_to_arabic('ML')
        self.assertEqual(1050, res)

    def test_MLI(self):
        res = convert_to_arabic('MLI')
        self.assertEqual(1051, res)

    def test_MLII(self):
        res = convert_to_arabic('MLII')
        self.assertEqual(1052, res)

    def test_MLIII(self):
        res = convert_to_arabic('MLIII')
        self.assertEqual(1053, res)

    def test_MLIV(self):
        res = convert_to_arabic('MLIV')
        self.assertEqual(1054, res)

    def test_MLV(self):
        res = convert_to_arabic('MLV')
        self.assertEqual(1055, res)

    def test_MLVI(self):
        res = convert_to_arabic('MLVI')
        self.assertEqual(1056, res)

    def test_MLVII(self):
        res = convert_to_arabic('MLVII')
        self.assertEqual(1057, res)

    def test_MLVIII(self):
        res = convert_to_arabic('MLVIII')
        self.assertEqual(1058, res)

    def test_MLIX(self):
        res = convert_to_arabic('MLIX')
        self.assertEqual(1059, res)

    def test_MLX(self):
        res = convert_to_arabic('MLX')
        self.assertEqual(1060, res)

    def test_MLXI(self):
        res = convert_to_arabic('MLXI')
        self.assertEqual(1061, res)

    def test_MLXII(self):
        res = convert_to_arabic('MLXII')
        self.assertEqual(1062, res)

    def test_MLXIII(self):
        res = convert_to_arabic('MLXIII')
        self.assertEqual(1063, res)

    def test_MLXIV(self):
        res = convert_to_arabic('MLXIV')
        self.assertEqual(1064, res)

    def test_MLXV(self):
        res = convert_to_arabic('MLXV')
        self.assertEqual(1065, res)

    def test_MLXVI(self):
        res = convert_to_arabic('MLXVI')
        self.assertEqual(1066, res)

    def test_MLXVII(self):
        res = convert_to_arabic('MLXVII')
        self.assertEqual(1067, res)

    def test_MLXVIII(self):
        res = convert_to_arabic('MLXVIII')
        self.assertEqual(1068, res)

    def test_MLXIX(self):
        res = convert_to_arabic('MLXIX')
        self.assertEqual(1069, res)

    def test_MLXX(self):
        res = convert_to_arabic('MLXX')
        self.assertEqual(1070, res)

    def test_MLXXI(self):
        res = convert_to_arabic('MLXXI')
        self.assertEqual(1071, res)

    def test_MLXXII(self):
        res = convert_to_arabic('MLXXII')
        self.assertEqual(1072, res)

    def test_MLXXIII(self):
        res = convert_to_arabic('MLXXIII')
        self.assertEqual(1073, res)

    def test_MLXXIV(self):
        res = convert_to_arabic('MLXXIV')
        self.assertEqual(1074, res)

    def test_MLXXV(self):
        res = convert_to_arabic('MLXXV')
        self.assertEqual(1075, res)

    def test_MLXXVI(self):
        res = convert_to_arabic('MLXXVI')
        self.assertEqual(1076, res)

    def test_MLXXVII(self):
        res = convert_to_arabic('MLXXVII')
        self.assertEqual(1077, res)

    def test_MLXXVIII(self):
        res = convert_to_arabic('MLXXVIII')
        self.assertEqual(1078, res)

    def test_MLXXIX(self):
        res = convert_to_arabic('MLXXIX')
        self.assertEqual(1079, res)

    def test_MLXXX(self):
        res = convert_to_arabic('MLXXX')
        self.assertEqual(1080, res)

    def test_MLXXXI(self):
        res = convert_to_arabic('MLXXXI')
        self.assertEqual(1081, res)

    def test_MLXXXII(self):
        res = convert_to_arabic('MLXXXII')
        self.assertEqual(1082, res)

    def test_MLXXXIII(self):
        res = convert_to_arabic('MLXXXIII')
        self.assertEqual(1083, res)

    def test_MLXXXIV(self):
        res = convert_to_arabic('MLXXXIV')
        self.assertEqual(1084, res)

    def test_MLXXXV(self):
        res = convert_to_arabic('MLXXXV')
        self.assertEqual(1085, res)

    def test_MLXXXVI(self):
        res = convert_to_arabic('MLXXXVI')
        self.assertEqual(1086, res)

    def test_MLXXXVII(self):
        res = convert_to_arabic('MLXXXVII')
        self.assertEqual(1087, res)

    def test_MLXXXVIII(self):
        res = convert_to_arabic('MLXXXVIII')
        self.assertEqual(1088, res)

    def test_MLXXXIX(self):
        res = convert_to_arabic('MLXXXIX')
        self.assertEqual(1089, res)

    def test_MXC(self):
        res = convert_to_arabic('MXC')
        self.assertEqual(1090, res)

    def test_MXCI(self):
        res = convert_to_arabic('MXCI')
        self.assertEqual(1091, res)

    def test_MXCII(self):
        res = convert_to_arabic('MXCII')
        self.assertEqual(1092, res)

    def test_MXCIII(self):
        res = convert_to_arabic('MXCIII')
        self.assertEqual(1093, res)

    def test_MXCIV(self):
        res = convert_to_arabic('MXCIV')
        self.assertEqual(1094, res)

    def test_MXCV(self):
        res = convert_to_arabic('MXCV')
        self.assertEqual(1095, res)

    def test_MXCVI(self):
        res = convert_to_arabic('MXCVI')
        self.assertEqual(1096, res)

    def test_MXCVII(self):
        res = convert_to_arabic('MXCVII')
        self.assertEqual(1097, res)

    def test_MXCVIII(self):
        res = convert_to_arabic('MXCVIII')
        self.assertEqual(1098, res)

    def test_MXCIX(self):
        res = convert_to_arabic('MXCIX')
        self.assertEqual(1099, res)

    def test_MC(self):
        res = convert_to_arabic('MC')
        self.assertEqual(1100, res)

    def test_MCI(self):
        res = convert_to_arabic('MCI')
        self.assertEqual(1101, res)

    def test_MCII(self):
        res = convert_to_arabic('MCII')
        self.assertEqual(1102, res)

    def test_MCIII(self):
        res = convert_to_arabic('MCIII')
        self.assertEqual(1103, res)

    def test_MCIV(self):
        res = convert_to_arabic('MCIV')
        self.assertEqual(1104, res)

    def test_MCV(self):
        res = convert_to_arabic('MCV')
        self.assertEqual(1105, res)

    def test_MCVI(self):
        res = convert_to_arabic('MCVI')
        self.assertEqual(1106, res)

    def test_MCVII(self):
        res = convert_to_arabic('MCVII')
        self.assertEqual(1107, res)

    def test_MCVIII(self):
        res = convert_to_arabic('MCVIII')
        self.assertEqual(1108, res)

    def test_MCIX(self):
        res = convert_to_arabic('MCIX')
        self.assertEqual(1109, res)

    def test_MCX(self):
        res = convert_to_arabic('MCX')
        self.assertEqual(1110, res)

    def test_MCXI(self):
        res = convert_to_arabic('MCXI')
        self.assertEqual(1111, res)

    def test_MCXII(self):
        res = convert_to_arabic('MCXII')
        self.assertEqual(1112, res)

    def test_MCXIII(self):
        res = convert_to_arabic('MCXIII')
        self.assertEqual(1113, res)

    def test_MCXIV(self):
        res = convert_to_arabic('MCXIV')
        self.assertEqual(1114, res)

    def test_MCXV(self):
        res = convert_to_arabic('MCXV')
        self.assertEqual(1115, res)

    def test_MCXVI(self):
        res = convert_to_arabic('MCXVI')
        self.assertEqual(1116, res)

    def test_MCXVII(self):
        res = convert_to_arabic('MCXVII')
        self.assertEqual(1117, res)

    def test_MCXVIII(self):
        res = convert_to_arabic('MCXVIII')
        self.assertEqual(1118, res)

    def test_MCXIX(self):
        res = convert_to_arabic('MCXIX')
        self.assertEqual(1119, res)

    def test_MCXX(self):
        res = convert_to_arabic('MCXX')
        self.assertEqual(1120, res)

    def test_MCXXI(self):
        res = convert_to_arabic('MCXXI')
        self.assertEqual(1121, res)

    def test_MCXXII(self):
        res = convert_to_arabic('MCXXII')
        self.assertEqual(1122, res)

    def test_MCXXIII(self):
        res = convert_to_arabic('MCXXIII')
        self.assertEqual(1123, res)

    def test_MCXXIV(self):
        res = convert_to_arabic('MCXXIV')
        self.assertEqual(1124, res)

    def test_MCXXV(self):
        res = convert_to_arabic('MCXXV')
        self.assertEqual(1125, res)

    def test_MCXXVI(self):
        res = convert_to_arabic('MCXXVI')
        self.assertEqual(1126, res)

    def test_MCXXVII(self):
        res = convert_to_arabic('MCXXVII')
        self.assertEqual(1127, res)

    def test_MCXXVIII(self):
        res = convert_to_arabic('MCXXVIII')
        self.assertEqual(1128, res)

    def test_MCXXIX(self):
        res = convert_to_arabic('MCXXIX')
        self.assertEqual(1129, res)

    def test_MCXXX(self):
        res = convert_to_arabic('MCXXX')
        self.assertEqual(1130, res)

    def test_MCXXXI(self):
        res = convert_to_arabic('MCXXXI')
        self.assertEqual(1131, res)

    def test_MCXXXII(self):
        res = convert_to_arabic('MCXXXII')
        self.assertEqual(1132, res)

    def test_MCXXXIII(self):
        res = convert_to_arabic('MCXXXIII')
        self.assertEqual(1133, res)

    def test_MCXXXIV(self):
        res = convert_to_arabic('MCXXXIV')
        self.assertEqual(1134, res)

    def test_MCXXXV(self):
        res = convert_to_arabic('MCXXXV')
        self.assertEqual(1135, res)

    def test_MCXXXVI(self):
        res = convert_to_arabic('MCXXXVI')
        self.assertEqual(1136, res)

    def test_MCXXXVII(self):
        res = convert_to_arabic('MCXXXVII')
        self.assertEqual(1137, res)

    def test_MCXXXVIII(self):
        res = convert_to_arabic('MCXXXVIII')
        self.assertEqual(1138, res)

    def test_MCXXXIX(self):
        res = convert_to_arabic('MCXXXIX')
        self.assertEqual(1139, res)

    def test_MCXL(self):
        res = convert_to_arabic('MCXL')
        self.assertEqual(1140, res)

    def test_MCXLI(self):
        res = convert_to_arabic('MCXLI')
        self.assertEqual(1141, res)

    def test_MCXLII(self):
        res = convert_to_arabic('MCXLII')
        self.assertEqual(1142, res)

    def test_MCXLIII(self):
        res = convert_to_arabic('MCXLIII')
        self.assertEqual(1143, res)

    def test_MCXLIV(self):
        res = convert_to_arabic('MCXLIV')
        self.assertEqual(1144, res)

    def test_MCXLV(self):
        res = convert_to_arabic('MCXLV')
        self.assertEqual(1145, res)

    def test_MCXLVI(self):
        res = convert_to_arabic('MCXLVI')
        self.assertEqual(1146, res)

    def test_MCXLVII(self):
        res = convert_to_arabic('MCXLVII')
        self.assertEqual(1147, res)

    def test_MCXLVIII(self):
        res = convert_to_arabic('MCXLVIII')
        self.assertEqual(1148, res)

    def test_MCXLIX(self):
        res = convert_to_arabic('MCXLIX')
        self.assertEqual(1149, res)

    def test_MCL(self):
        res = convert_to_arabic('MCL')
        self.assertEqual(1150, res)

    def test_MCLI(self):
        res = convert_to_arabic('MCLI')
        self.assertEqual(1151, res)

    def test_MCLII(self):
        res = convert_to_arabic('MCLII')
        self.assertEqual(1152, res)

    def test_MCLIII(self):
        res = convert_to_arabic('MCLIII')
        self.assertEqual(1153, res)

    def test_MCLIV(self):
        res = convert_to_arabic('MCLIV')
        self.assertEqual(1154, res)

    def test_MCLV(self):
        res = convert_to_arabic('MCLV')
        self.assertEqual(1155, res)

    def test_MCLVI(self):
        res = convert_to_arabic('MCLVI')
        self.assertEqual(1156, res)

    def test_MCLVII(self):
        res = convert_to_arabic('MCLVII')
        self.assertEqual(1157, res)

    def test_MCLVIII(self):
        res = convert_to_arabic('MCLVIII')
        self.assertEqual(1158, res)

    def test_MCLIX(self):
        res = convert_to_arabic('MCLIX')
        self.assertEqual(1159, res)

    def test_MCLX(self):
        res = convert_to_arabic('MCLX')
        self.assertEqual(1160, res)

    def test_MCLXI(self):
        res = convert_to_arabic('MCLXI')
        self.assertEqual(1161, res)

    def test_MCLXII(self):
        res = convert_to_arabic('MCLXII')
        self.assertEqual(1162, res)

    def test_MCLXIII(self):
        res = convert_to_arabic('MCLXIII')
        self.assertEqual(1163, res)

    def test_MCLXIV(self):
        res = convert_to_arabic('MCLXIV')
        self.assertEqual(1164, res)

    def test_MCLXV(self):
        res = convert_to_arabic('MCLXV')
        self.assertEqual(1165, res)

    def test_MCLXVI(self):
        res = convert_to_arabic('MCLXVI')
        self.assertEqual(1166, res)

    def test_MCLXVII(self):
        res = convert_to_arabic('MCLXVII')
        self.assertEqual(1167, res)

    def test_MCLXVIII(self):
        res = convert_to_arabic('MCLXVIII')
        self.assertEqual(1168, res)

    def test_MCLXIX(self):
        res = convert_to_arabic('MCLXIX')
        self.assertEqual(1169, res)

    def test_MCLXX(self):
        res = convert_to_arabic('MCLXX')
        self.assertEqual(1170, res)

    def test_MCLXXI(self):
        res = convert_to_arabic('MCLXXI')
        self.assertEqual(1171, res)

    def test_MCLXXII(self):
        res = convert_to_arabic('MCLXXII')
        self.assertEqual(1172, res)

    def test_MCLXXIII(self):
        res = convert_to_arabic('MCLXXIII')
        self.assertEqual(1173, res)

    def test_MCLXXIV(self):
        res = convert_to_arabic('MCLXXIV')
        self.assertEqual(1174, res)

    def test_MCLXXV(self):
        res = convert_to_arabic('MCLXXV')
        self.assertEqual(1175, res)

    def test_MCLXXVI(self):
        res = convert_to_arabic('MCLXXVI')
        self.assertEqual(1176, res)

    def test_MCLXXVII(self):
        res = convert_to_arabic('MCLXXVII')
        self.assertEqual(1177, res)

    def test_MCLXXVIII(self):
        res = convert_to_arabic('MCLXXVIII')
        self.assertEqual(1178, res)

    def test_MCLXXIX(self):
        res = convert_to_arabic('MCLXXIX')
        self.assertEqual(1179, res)

    def test_MCLXXX(self):
        res = convert_to_arabic('MCLXXX')
        self.assertEqual(1180, res)

    def test_MCLXXXI(self):
        res = convert_to_arabic('MCLXXXI')
        self.assertEqual(1181, res)

    def test_MCLXXXII(self):
        res = convert_to_arabic('MCLXXXII')
        self.assertEqual(1182, res)

    def test_MCLXXXIII(self):
        res = convert_to_arabic('MCLXXXIII')
        self.assertEqual(1183, res)

    def test_MCLXXXIV(self):
        res = convert_to_arabic('MCLXXXIV')
        self.assertEqual(1184, res)

    def test_MCLXXXV(self):
        res = convert_to_arabic('MCLXXXV')
        self.assertEqual(1185, res)

    def test_MCLXXXVI(self):
        res = convert_to_arabic('MCLXXXVI')
        self.assertEqual(1186, res)

    def test_MCLXXXVII(self):
        res = convert_to_arabic('MCLXXXVII')
        self.assertEqual(1187, res)

    def test_MCLXXXVIII(self):
        res = convert_to_arabic('MCLXXXVIII')
        self.assertEqual(1188, res)

    def test_MCLXXXIX(self):
        res = convert_to_arabic('MCLXXXIX')
        self.assertEqual(1189, res)

    def test_MCXC(self):
        res = convert_to_arabic('MCXC')
        self.assertEqual(1190, res)

    def test_MCXCI(self):
        res = convert_to_arabic('MCXCI')
        self.assertEqual(1191, res)

    def test_MCXCII(self):
        res = convert_to_arabic('MCXCII')
        self.assertEqual(1192, res)

    def test_MCXCIII(self):
        res = convert_to_arabic('MCXCIII')
        self.assertEqual(1193, res)

    def test_MCXCIV(self):
        res = convert_to_arabic('MCXCIV')
        self.assertEqual(1194, res)

    def test_MCXCV(self):
        res = convert_to_arabic('MCXCV')
        self.assertEqual(1195, res)

    def test_MCXCVI(self):
        res = convert_to_arabic('MCXCVI')
        self.assertEqual(1196, res)

    def test_MCXCVII(self):
        res = convert_to_arabic('MCXCVII')
        self.assertEqual(1197, res)

    def test_MCXCVIII(self):
        res = convert_to_arabic('MCXCVIII')
        self.assertEqual(1198, res)

    def test_MCXCIX(self):
        res = convert_to_arabic('MCXCIX')
        self.assertEqual(1199, res)

    def test_MCC(self):
        res = convert_to_arabic('MCC')
        self.assertEqual(1200, res)

    def test_MCCI(self):
        res = convert_to_arabic('MCCI')
        self.assertEqual(1201, res)

    def test_MCCII(self):
        res = convert_to_arabic('MCCII')
        self.assertEqual(1202, res)

    def test_MCCIII(self):
        res = convert_to_arabic('MCCIII')
        self.assertEqual(1203, res)

    def test_MCCIV(self):
        res = convert_to_arabic('MCCIV')
        self.assertEqual(1204, res)

    def test_MCCV(self):
        res = convert_to_arabic('MCCV')
        self.assertEqual(1205, res)

    def test_MCCVI(self):
        res = convert_to_arabic('MCCVI')
        self.assertEqual(1206, res)

    def test_MCCVII(self):
        res = convert_to_arabic('MCCVII')
        self.assertEqual(1207, res)

    def test_MCCVIII(self):
        res = convert_to_arabic('MCCVIII')
        self.assertEqual(1208, res)

    def test_MCCIX(self):
        res = convert_to_arabic('MCCIX')
        self.assertEqual(1209, res)

    def test_MCCX(self):
        res = convert_to_arabic('MCCX')
        self.assertEqual(1210, res)

    def test_MCCXI(self):
        res = convert_to_arabic('MCCXI')
        self.assertEqual(1211, res)

    def test_MCCXII(self):
        res = convert_to_arabic('MCCXII')
        self.assertEqual(1212, res)

    def test_MCCXIII(self):
        res = convert_to_arabic('MCCXIII')
        self.assertEqual(1213, res)

    def test_MCCXIV(self):
        res = convert_to_arabic('MCCXIV')
        self.assertEqual(1214, res)

    def test_MCCXV(self):
        res = convert_to_arabic('MCCXV')
        self.assertEqual(1215, res)

    def test_MCCXVI(self):
        res = convert_to_arabic('MCCXVI')
        self.assertEqual(1216, res)

    def test_MCCXVII(self):
        res = convert_to_arabic('MCCXVII')
        self.assertEqual(1217, res)

    def test_MCCXVIII(self):
        res = convert_to_arabic('MCCXVIII')
        self.assertEqual(1218, res)

    def test_MCCXIX(self):
        res = convert_to_arabic('MCCXIX')
        self.assertEqual(1219, res)

    def test_MCCXX(self):
        res = convert_to_arabic('MCCXX')
        self.assertEqual(1220, res)

    def test_MCCXXI(self):
        res = convert_to_arabic('MCCXXI')
        self.assertEqual(1221, res)

    def test_MCCXXII(self):
        res = convert_to_arabic('MCCXXII')
        self.assertEqual(1222, res)

    def test_MCCXXIII(self):
        res = convert_to_arabic('MCCXXIII')
        self.assertEqual(1223, res)

    def test_MCCXXIV(self):
        res = convert_to_arabic('MCCXXIV')
        self.assertEqual(1224, res)

    def test_MCCXXV(self):
        res = convert_to_arabic('MCCXXV')
        self.assertEqual(1225, res)

    def test_MCCXXVI(self):
        res = convert_to_arabic('MCCXXVI')
        self.assertEqual(1226, res)

    def test_MCCXXVII(self):
        res = convert_to_arabic('MCCXXVII')
        self.assertEqual(1227, res)

    def test_MCCXXVIII(self):
        res = convert_to_arabic('MCCXXVIII')
        self.assertEqual(1228, res)

    def test_MCCXXIX(self):
        res = convert_to_arabic('MCCXXIX')
        self.assertEqual(1229, res)

    def test_MCCXXX(self):
        res = convert_to_arabic('MCCXXX')
        self.assertEqual(1230, res)

    def test_MCCXXXI(self):
        res = convert_to_arabic('MCCXXXI')
        self.assertEqual(1231, res)

    def test_MCCXXXII(self):
        res = convert_to_arabic('MCCXXXII')
        self.assertEqual(1232, res)

    def test_MCCXXXIII(self):
        res = convert_to_arabic('MCCXXXIII')
        self.assertEqual(1233, res)

    def test_MCCXXXIV(self):
        res = convert_to_arabic('MCCXXXIV')
        self.assertEqual(1234, res)

    def test_MCCXXXV(self):
        res = convert_to_arabic('MCCXXXV')
        self.assertEqual(1235, res)

    def test_MCCXXXVI(self):
        res = convert_to_arabic('MCCXXXVI')
        self.assertEqual(1236, res)

    def test_MCCXXXVII(self):
        res = convert_to_arabic('MCCXXXVII')
        self.assertEqual(1237, res)

    def test_MCCXXXVIII(self):
        res = convert_to_arabic('MCCXXXVIII')
        self.assertEqual(1238, res)

    def test_MCCXXXIX(self):
        res = convert_to_arabic('MCCXXXIX')
        self.assertEqual(1239, res)

    def test_MCCXL(self):
        res = convert_to_arabic('MCCXL')
        self.assertEqual(1240, res)

    def test_MCCXLI(self):
        res = convert_to_arabic('MCCXLI')
        self.assertEqual(1241, res)

    def test_MCCXLII(self):
        res = convert_to_arabic('MCCXLII')
        self.assertEqual(1242, res)

    def test_MCCXLIII(self):
        res = convert_to_arabic('MCCXLIII')
        self.assertEqual(1243, res)

    def test_MCCXLIV(self):
        res = convert_to_arabic('MCCXLIV')
        self.assertEqual(1244, res)

    def test_MCCXLV(self):
        res = convert_to_arabic('MCCXLV')
        self.assertEqual(1245, res)

    def test_MCCXLVI(self):
        res = convert_to_arabic('MCCXLVI')
        self.assertEqual(1246, res)

    def test_MCCXLVII(self):
        res = convert_to_arabic('MCCXLVII')
        self.assertEqual(1247, res)

    def test_MCCXLVIII(self):
        res = convert_to_arabic('MCCXLVIII')
        self.assertEqual(1248, res)

    def test_MCCXLIX(self):
        res = convert_to_arabic('MCCXLIX')
        self.assertEqual(1249, res)

    def test_MCCL(self):
        res = convert_to_arabic('MCCL')
        self.assertEqual(1250, res)

    def test_MCCLI(self):
        res = convert_to_arabic('MCCLI')
        self.assertEqual(1251, res)

    def test_MCCLII(self):
        res = convert_to_arabic('MCCLII')
        self.assertEqual(1252, res)

    def test_MCCLIII(self):
        res = convert_to_arabic('MCCLIII')
        self.assertEqual(1253, res)

    def test_MCCLIV(self):
        res = convert_to_arabic('MCCLIV')
        self.assertEqual(1254, res)

    def test_MCCLV(self):
        res = convert_to_arabic('MCCLV')
        self.assertEqual(1255, res)

    def test_MCCLVI(self):
        res = convert_to_arabic('MCCLVI')
        self.assertEqual(1256, res)

    def test_MCCLVII(self):
        res = convert_to_arabic('MCCLVII')
        self.assertEqual(1257, res)

    def test_MCCLVIII(self):
        res = convert_to_arabic('MCCLVIII')
        self.assertEqual(1258, res)

    def test_MCCLIX(self):
        res = convert_to_arabic('MCCLIX')
        self.assertEqual(1259, res)

    def test_MCCLX(self):
        res = convert_to_arabic('MCCLX')
        self.assertEqual(1260, res)

    def test_MCCLXI(self):
        res = convert_to_arabic('MCCLXI')
        self.assertEqual(1261, res)

    def test_MCCLXII(self):
        res = convert_to_arabic('MCCLXII')
        self.assertEqual(1262, res)

    def test_MCCLXIII(self):
        res = convert_to_arabic('MCCLXIII')
        self.assertEqual(1263, res)

    def test_MCCLXIV(self):
        res = convert_to_arabic('MCCLXIV')
        self.assertEqual(1264, res)

    def test_MCCLXV(self):
        res = convert_to_arabic('MCCLXV')
        self.assertEqual(1265, res)

    def test_MCCLXVI(self):
        res = convert_to_arabic('MCCLXVI')
        self.assertEqual(1266, res)

    def test_MCCLXVII(self):
        res = convert_to_arabic('MCCLXVII')
        self.assertEqual(1267, res)

    def test_MCCLXVIII(self):
        res = convert_to_arabic('MCCLXVIII')
        self.assertEqual(1268, res)

    def test_MCCLXIX(self):
        res = convert_to_arabic('MCCLXIX')
        self.assertEqual(1269, res)

    def test_MCCLXX(self):
        res = convert_to_arabic('MCCLXX')
        self.assertEqual(1270, res)

    def test_MCCLXXI(self):
        res = convert_to_arabic('MCCLXXI')
        self.assertEqual(1271, res)

    def test_MCCLXXII(self):
        res = convert_to_arabic('MCCLXXII')
        self.assertEqual(1272, res)

    def test_MCCLXXIII(self):
        res = convert_to_arabic('MCCLXXIII')
        self.assertEqual(1273, res)

    def test_MCCLXXIV(self):
        res = convert_to_arabic('MCCLXXIV')
        self.assertEqual(1274, res)

    def test_MCCLXXV(self):
        res = convert_to_arabic('MCCLXXV')
        self.assertEqual(1275, res)

    def test_MCCLXXVI(self):
        res = convert_to_arabic('MCCLXXVI')
        self.assertEqual(1276, res)

    def test_MCCLXXVII(self):
        res = convert_to_arabic('MCCLXXVII')
        self.assertEqual(1277, res)

    def test_MCCLXXVIII(self):
        res = convert_to_arabic('MCCLXXVIII')
        self.assertEqual(1278, res)

    def test_MCCLXXIX(self):
        res = convert_to_arabic('MCCLXXIX')
        self.assertEqual(1279, res)

    def test_MCCLXXX(self):
        res = convert_to_arabic('MCCLXXX')
        self.assertEqual(1280, res)

    def test_MCCLXXXI(self):
        res = convert_to_arabic('MCCLXXXI')
        self.assertEqual(1281, res)

    def test_MCCLXXXII(self):
        res = convert_to_arabic('MCCLXXXII')
        self.assertEqual(1282, res)

    def test_MCCLXXXIII(self):
        res = convert_to_arabic('MCCLXXXIII')
        self.assertEqual(1283, res)

    def test_MCCLXXXIV(self):
        res = convert_to_arabic('MCCLXXXIV')
        self.assertEqual(1284, res)

    def test_MCCLXXXV(self):
        res = convert_to_arabic('MCCLXXXV')
        self.assertEqual(1285, res)

    def test_MCCLXXXVI(self):
        res = convert_to_arabic('MCCLXXXVI')
        self.assertEqual(1286, res)

    def test_MCCLXXXVII(self):
        res = convert_to_arabic('MCCLXXXVII')
        self.assertEqual(1287, res)

    def test_MCCLXXXVIII(self):
        res = convert_to_arabic('MCCLXXXVIII')
        self.assertEqual(1288, res)

    def test_MCCLXXXIX(self):
        res = convert_to_arabic('MCCLXXXIX')
        self.assertEqual(1289, res)

    def test_MCCXC(self):
        res = convert_to_arabic('MCCXC')
        self.assertEqual(1290, res)

    def test_MCCXCI(self):
        res = convert_to_arabic('MCCXCI')
        self.assertEqual(1291, res)

    def test_MCCXCII(self):
        res = convert_to_arabic('MCCXCII')
        self.assertEqual(1292, res)

    def test_MCCXCIII(self):
        res = convert_to_arabic('MCCXCIII')
        self.assertEqual(1293, res)

    def test_MCCXCIV(self):
        res = convert_to_arabic('MCCXCIV')
        self.assertEqual(1294, res)

    def test_MCCXCV(self):
        res = convert_to_arabic('MCCXCV')
        self.assertEqual(1295, res)

    def test_MCCXCVI(self):
        res = convert_to_arabic('MCCXCVI')
        self.assertEqual(1296, res)

    def test_MCCXCVII(self):
        res = convert_to_arabic('MCCXCVII')
        self.assertEqual(1297, res)

    def test_MCCXCVIII(self):
        res = convert_to_arabic('MCCXCVIII')
        self.assertEqual(1298, res)

    def test_MCCXCIX(self):
        res = convert_to_arabic('MCCXCIX')
        self.assertEqual(1299, res)

    def test_MCCC(self):
        res = convert_to_arabic('MCCC')
        self.assertEqual(1300, res)

    def test_MCCCI(self):
        res = convert_to_arabic('MCCCI')
        self.assertEqual(1301, res)

    def test_MCCCII(self):
        res = convert_to_arabic('MCCCII')
        self.assertEqual(1302, res)

    def test_MCCCIII(self):
        res = convert_to_arabic('MCCCIII')
        self.assertEqual(1303, res)

    def test_MCCCIV(self):
        res = convert_to_arabic('MCCCIV')
        self.assertEqual(1304, res)

    def test_MCCCV(self):
        res = convert_to_arabic('MCCCV')
        self.assertEqual(1305, res)

    def test_MCCCVI(self):
        res = convert_to_arabic('MCCCVI')
        self.assertEqual(1306, res)

    def test_MCCCVII(self):
        res = convert_to_arabic('MCCCVII')
        self.assertEqual(1307, res)

    def test_MCCCVIII(self):
        res = convert_to_arabic('MCCCVIII')
        self.assertEqual(1308, res)

    def test_MCCCIX(self):
        res = convert_to_arabic('MCCCIX')
        self.assertEqual(1309, res)

    def test_MCCCX(self):
        res = convert_to_arabic('MCCCX')
        self.assertEqual(1310, res)

    def test_MCCCXI(self):
        res = convert_to_arabic('MCCCXI')
        self.assertEqual(1311, res)

    def test_MCCCXII(self):
        res = convert_to_arabic('MCCCXII')
        self.assertEqual(1312, res)

    def test_MCCCXIII(self):
        res = convert_to_arabic('MCCCXIII')
        self.assertEqual(1313, res)

    def test_MCCCXIV(self):
        res = convert_to_arabic('MCCCXIV')
        self.assertEqual(1314, res)

    def test_MCCCXV(self):
        res = convert_to_arabic('MCCCXV')
        self.assertEqual(1315, res)

    def test_MCCCXVI(self):
        res = convert_to_arabic('MCCCXVI')
        self.assertEqual(1316, res)

    def test_MCCCXVII(self):
        res = convert_to_arabic('MCCCXVII')
        self.assertEqual(1317, res)

    def test_MCCCXVIII(self):
        res = convert_to_arabic('MCCCXVIII')
        self.assertEqual(1318, res)

    def test_MCCCXIX(self):
        res = convert_to_arabic('MCCCXIX')
        self.assertEqual(1319, res)

    def test_MCCCXX(self):
        res = convert_to_arabic('MCCCXX')
        self.assertEqual(1320, res)

    def test_MCCCXXI(self):
        res = convert_to_arabic('MCCCXXI')
        self.assertEqual(1321, res)

    def test_MCCCXXII(self):
        res = convert_to_arabic('MCCCXXII')
        self.assertEqual(1322, res)

    def test_MCCCXXIII(self):
        res = convert_to_arabic('MCCCXXIII')
        self.assertEqual(1323, res)

    def test_MCCCXXIV(self):
        res = convert_to_arabic('MCCCXXIV')
        self.assertEqual(1324, res)

    def test_MCCCXXV(self):
        res = convert_to_arabic('MCCCXXV')
        self.assertEqual(1325, res)

    def test_MCCCXXVI(self):
        res = convert_to_arabic('MCCCXXVI')
        self.assertEqual(1326, res)

    def test_MCCCXXVII(self):
        res = convert_to_arabic('MCCCXXVII')
        self.assertEqual(1327, res)

    def test_MCCCXXVIII(self):
        res = convert_to_arabic('MCCCXXVIII')
        self.assertEqual(1328, res)

    def test_MCCCXXIX(self):
        res = convert_to_arabic('MCCCXXIX')
        self.assertEqual(1329, res)

    def test_MCCCXXX(self):
        res = convert_to_arabic('MCCCXXX')
        self.assertEqual(1330, res)

    def test_MCCCXXXI(self):
        res = convert_to_arabic('MCCCXXXI')
        self.assertEqual(1331, res)

    def test_MCCCXXXII(self):
        res = convert_to_arabic('MCCCXXXII')
        self.assertEqual(1332, res)

    def test_MCCCXXXIII(self):
        res = convert_to_arabic('MCCCXXXIII')
        self.assertEqual(1333, res)

    def test_MCCCXXXIV(self):
        res = convert_to_arabic('MCCCXXXIV')
        self.assertEqual(1334, res)

    def test_MCCCXXXV(self):
        res = convert_to_arabic('MCCCXXXV')
        self.assertEqual(1335, res)

    def test_MCCCXXXVI(self):
        res = convert_to_arabic('MCCCXXXVI')
        self.assertEqual(1336, res)

    def test_MCCCXXXVII(self):
        res = convert_to_arabic('MCCCXXXVII')
        self.assertEqual(1337, res)

    def test_MCCCXXXVIII(self):
        res = convert_to_arabic('MCCCXXXVIII')
        self.assertEqual(1338, res)

    def test_MCCCXXXIX(self):
        res = convert_to_arabic('MCCCXXXIX')
        self.assertEqual(1339, res)

    def test_MCCCXL(self):
        res = convert_to_arabic('MCCCXL')
        self.assertEqual(1340, res)

    def test_MCCCXLI(self):
        res = convert_to_arabic('MCCCXLI')
        self.assertEqual(1341, res)

    def test_MCCCXLII(self):
        res = convert_to_arabic('MCCCXLII')
        self.assertEqual(1342, res)

    def test_MCCCXLIII(self):
        res = convert_to_arabic('MCCCXLIII')
        self.assertEqual(1343, res)

    def test_MCCCXLIV(self):
        res = convert_to_arabic('MCCCXLIV')
        self.assertEqual(1344, res)

    def test_MCCCXLV(self):
        res = convert_to_arabic('MCCCXLV')
        self.assertEqual(1345, res)

    def test_MCCCXLVI(self):
        res = convert_to_arabic('MCCCXLVI')
        self.assertEqual(1346, res)

    def test_MCCCXLVII(self):
        res = convert_to_arabic('MCCCXLVII')
        self.assertEqual(1347, res)

    def test_MCCCXLVIII(self):
        res = convert_to_arabic('MCCCXLVIII')
        self.assertEqual(1348, res)

    def test_MCCCXLIX(self):
        res = convert_to_arabic('MCCCXLIX')
        self.assertEqual(1349, res)

    def test_MCCCL(self):
        res = convert_to_arabic('MCCCL')
        self.assertEqual(1350, res)

    def test_MCCCLI(self):
        res = convert_to_arabic('MCCCLI')
        self.assertEqual(1351, res)

    def test_MCCCLII(self):
        res = convert_to_arabic('MCCCLII')
        self.assertEqual(1352, res)

    def test_MCCCLIII(self):
        res = convert_to_arabic('MCCCLIII')
        self.assertEqual(1353, res)

    def test_MCCCLIV(self):
        res = convert_to_arabic('MCCCLIV')
        self.assertEqual(1354, res)

    def test_MCCCLV(self):
        res = convert_to_arabic('MCCCLV')
        self.assertEqual(1355, res)

    def test_MCCCLVI(self):
        res = convert_to_arabic('MCCCLVI')
        self.assertEqual(1356, res)

    def test_MCCCLVII(self):
        res = convert_to_arabic('MCCCLVII')
        self.assertEqual(1357, res)

    def test_MCCCLVIII(self):
        res = convert_to_arabic('MCCCLVIII')
        self.assertEqual(1358, res)

    def test_MCCCLIX(self):
        res = convert_to_arabic('MCCCLIX')
        self.assertEqual(1359, res)

    def test_MCCCLX(self):
        res = convert_to_arabic('MCCCLX')
        self.assertEqual(1360, res)

    def test_MCCCLXI(self):
        res = convert_to_arabic('MCCCLXI')
        self.assertEqual(1361, res)

    def test_MCCCLXII(self):
        res = convert_to_arabic('MCCCLXII')
        self.assertEqual(1362, res)

    def test_MCCCLXIII(self):
        res = convert_to_arabic('MCCCLXIII')
        self.assertEqual(1363, res)

    def test_MCCCLXIV(self):
        res = convert_to_arabic('MCCCLXIV')
        self.assertEqual(1364, res)

    def test_MCCCLXV(self):
        res = convert_to_arabic('MCCCLXV')
        self.assertEqual(1365, res)

    def test_MCCCLXVI(self):
        res = convert_to_arabic('MCCCLXVI')
        self.assertEqual(1366, res)

    def test_MCCCLXVII(self):
        res = convert_to_arabic('MCCCLXVII')
        self.assertEqual(1367, res)

    def test_MCCCLXVIII(self):
        res = convert_to_arabic('MCCCLXVIII')
        self.assertEqual(1368, res)

    def test_MCCCLXIX(self):
        res = convert_to_arabic('MCCCLXIX')
        self.assertEqual(1369, res)

    def test_MCCCLXX(self):
        res = convert_to_arabic('MCCCLXX')
        self.assertEqual(1370, res)

    def test_MCCCLXXI(self):
        res = convert_to_arabic('MCCCLXXI')
        self.assertEqual(1371, res)

    def test_MCCCLXXII(self):
        res = convert_to_arabic('MCCCLXXII')
        self.assertEqual(1372, res)

    def test_MCCCLXXIII(self):
        res = convert_to_arabic('MCCCLXXIII')
        self.assertEqual(1373, res)

    def test_MCCCLXXIV(self):
        res = convert_to_arabic('MCCCLXXIV')
        self.assertEqual(1374, res)

    def test_MCCCLXXV(self):
        res = convert_to_arabic('MCCCLXXV')
        self.assertEqual(1375, res)

    def test_MCCCLXXVI(self):
        res = convert_to_arabic('MCCCLXXVI')
        self.assertEqual(1376, res)

    def test_MCCCLXXVII(self):
        res = convert_to_arabic('MCCCLXXVII')
        self.assertEqual(1377, res)

    def test_MCCCLXXVIII(self):
        res = convert_to_arabic('MCCCLXXVIII')
        self.assertEqual(1378, res)

    def test_MCCCLXXIX(self):
        res = convert_to_arabic('MCCCLXXIX')
        self.assertEqual(1379, res)

    def test_MCCCLXXX(self):
        res = convert_to_arabic('MCCCLXXX')
        self.assertEqual(1380, res)

    def test_MCCCLXXXI(self):
        res = convert_to_arabic('MCCCLXXXI')
        self.assertEqual(1381, res)

    def test_MCCCLXXXII(self):
        res = convert_to_arabic('MCCCLXXXII')
        self.assertEqual(1382, res)

    def test_MCCCLXXXIII(self):
        res = convert_to_arabic('MCCCLXXXIII')
        self.assertEqual(1383, res)

    def test_MCCCLXXXIV(self):
        res = convert_to_arabic('MCCCLXXXIV')
        self.assertEqual(1384, res)

    def test_MCCCLXXXV(self):
        res = convert_to_arabic('MCCCLXXXV')
        self.assertEqual(1385, res)

    def test_MCCCLXXXVI(self):
        res = convert_to_arabic('MCCCLXXXVI')
        self.assertEqual(1386, res)

    def test_MCCCLXXXVII(self):
        res = convert_to_arabic('MCCCLXXXVII')
        self.assertEqual(1387, res)

    def test_MCCCLXXXVIII(self):
        res = convert_to_arabic('MCCCLXXXVIII')
        self.assertEqual(1388, res)

    def test_MCCCLXXXIX(self):
        res = convert_to_arabic('MCCCLXXXIX')
        self.assertEqual(1389, res)

    def test_MCCCXC(self):
        res = convert_to_arabic('MCCCXC')
        self.assertEqual(1390, res)

    def test_MCCCXCI(self):
        res = convert_to_arabic('MCCCXCI')
        self.assertEqual(1391, res)

    def test_MCCCXCII(self):
        res = convert_to_arabic('MCCCXCII')
        self.assertEqual(1392, res)

    def test_MCCCXCIII(self):
        res = convert_to_arabic('MCCCXCIII')
        self.assertEqual(1393, res)

    def test_MCCCXCIV(self):
        res = convert_to_arabic('MCCCXCIV')
        self.assertEqual(1394, res)

    def test_MCCCXCV(self):
        res = convert_to_arabic('MCCCXCV')
        self.assertEqual(1395, res)

    def test_MCCCXCVI(self):
        res = convert_to_arabic('MCCCXCVI')
        self.assertEqual(1396, res)

    def test_MCCCXCVII(self):
        res = convert_to_arabic('MCCCXCVII')
        self.assertEqual(1397, res)

    def test_MCCCXCVIII(self):
        res = convert_to_arabic('MCCCXCVIII')
        self.assertEqual(1398, res)

    def test_MCCCXCIX(self):
        res = convert_to_arabic('MCCCXCIX')
        self.assertEqual(1399, res)

    def test_MCD(self):
        res = convert_to_arabic('MCD')
        self.assertEqual(1400, res)

    def test_MCDI(self):
        res = convert_to_arabic('MCDI')
        self.assertEqual(1401, res)

    def test_MCDII(self):
        res = convert_to_arabic('MCDII')
        self.assertEqual(1402, res)

    def test_MCDIII(self):
        res = convert_to_arabic('MCDIII')
        self.assertEqual(1403, res)

    def test_MCDIV(self):
        res = convert_to_arabic('MCDIV')
        self.assertEqual(1404, res)

    def test_MCDV(self):
        res = convert_to_arabic('MCDV')
        self.assertEqual(1405, res)

    def test_MCDVI(self):
        res = convert_to_arabic('MCDVI')
        self.assertEqual(1406, res)

    def test_MCDVII(self):
        res = convert_to_arabic('MCDVII')
        self.assertEqual(1407, res)

    def test_MCDVIII(self):
        res = convert_to_arabic('MCDVIII')
        self.assertEqual(1408, res)

    def test_MCDIX(self):
        res = convert_to_arabic('MCDIX')
        self.assertEqual(1409, res)

    def test_MCDX(self):
        res = convert_to_arabic('MCDX')
        self.assertEqual(1410, res)

    def test_MCDXI(self):
        res = convert_to_arabic('MCDXI')
        self.assertEqual(1411, res)

    def test_MCDXII(self):
        res = convert_to_arabic('MCDXII')
        self.assertEqual(1412, res)

    def test_MCDXIII(self):
        res = convert_to_arabic('MCDXIII')
        self.assertEqual(1413, res)

    def test_MCDXIV(self):
        res = convert_to_arabic('MCDXIV')
        self.assertEqual(1414, res)

    def test_MCDXV(self):
        res = convert_to_arabic('MCDXV')
        self.assertEqual(1415, res)

    def test_MCDXVI(self):
        res = convert_to_arabic('MCDXVI')
        self.assertEqual(1416, res)

    def test_MCDXVII(self):
        res = convert_to_arabic('MCDXVII')
        self.assertEqual(1417, res)

    def test_MCDXVIII(self):
        res = convert_to_arabic('MCDXVIII')
        self.assertEqual(1418, res)

    def test_MCDXIX(self):
        res = convert_to_arabic('MCDXIX')
        self.assertEqual(1419, res)

    def test_MCDXX(self):
        res = convert_to_arabic('MCDXX')
        self.assertEqual(1420, res)

    def test_MCDXXI(self):
        res = convert_to_arabic('MCDXXI')
        self.assertEqual(1421, res)

    def test_MCDXXII(self):
        res = convert_to_arabic('MCDXXII')
        self.assertEqual(1422, res)

    def test_MCDXXIII(self):
        res = convert_to_arabic('MCDXXIII')
        self.assertEqual(1423, res)

    def test_MCDXXIV(self):
        res = convert_to_arabic('MCDXXIV')
        self.assertEqual(1424, res)

    def test_MCDXXV(self):
        res = convert_to_arabic('MCDXXV')
        self.assertEqual(1425, res)

    def test_MCDXXVI(self):
        res = convert_to_arabic('MCDXXVI')
        self.assertEqual(1426, res)

    def test_MCDXXVII(self):
        res = convert_to_arabic('MCDXXVII')
        self.assertEqual(1427, res)

    def test_MCDXXVIII(self):
        res = convert_to_arabic('MCDXXVIII')
        self.assertEqual(1428, res)

    def test_MCDXXIX(self):
        res = convert_to_arabic('MCDXXIX')
        self.assertEqual(1429, res)

    def test_MCDXXX(self):
        res = convert_to_arabic('MCDXXX')
        self.assertEqual(1430, res)

    def test_MCDXXXI(self):
        res = convert_to_arabic('MCDXXXI')
        self.assertEqual(1431, res)

    def test_MCDXXXII(self):
        res = convert_to_arabic('MCDXXXII')
        self.assertEqual(1432, res)

    def test_MCDXXXIII(self):
        res = convert_to_arabic('MCDXXXIII')
        self.assertEqual(1433, res)

    def test_MCDXXXIV(self):
        res = convert_to_arabic('MCDXXXIV')
        self.assertEqual(1434, res)

    def test_MCDXXXV(self):
        res = convert_to_arabic('MCDXXXV')
        self.assertEqual(1435, res)

    def test_MCDXXXVI(self):
        res = convert_to_arabic('MCDXXXVI')
        self.assertEqual(1436, res)

    def test_MCDXXXVII(self):
        res = convert_to_arabic('MCDXXXVII')
        self.assertEqual(1437, res)

    def test_MCDXXXVIII(self):
        res = convert_to_arabic('MCDXXXVIII')
        self.assertEqual(1438, res)

    def test_MCDXXXIX(self):
        res = convert_to_arabic('MCDXXXIX')
        self.assertEqual(1439, res)

    def test_MCDXL(self):
        res = convert_to_arabic('MCDXL')
        self.assertEqual(1440, res)

    def test_MCDXLI(self):
        res = convert_to_arabic('MCDXLI')
        self.assertEqual(1441, res)

    def test_MCDXLII(self):
        res = convert_to_arabic('MCDXLII')
        self.assertEqual(1442, res)

    def test_MCDXLIII(self):
        res = convert_to_arabic('MCDXLIII')
        self.assertEqual(1443, res)

    def test_MCDXLIV(self):
        res = convert_to_arabic('MCDXLIV')
        self.assertEqual(1444, res)

    def test_MCDXLV(self):
        res = convert_to_arabic('MCDXLV')
        self.assertEqual(1445, res)

    def test_MCDXLVI(self):
        res = convert_to_arabic('MCDXLVI')
        self.assertEqual(1446, res)

    def test_MCDXLVII(self):
        res = convert_to_arabic('MCDXLVII')
        self.assertEqual(1447, res)

    def test_MCDXLVIII(self):
        res = convert_to_arabic('MCDXLVIII')
        self.assertEqual(1448, res)

    def test_MCDXLIX(self):
        res = convert_to_arabic('MCDXLIX')
        self.assertEqual(1449, res)

    def test_MCDL(self):
        res = convert_to_arabic('MCDL')
        self.assertEqual(1450, res)

    def test_MCDLI(self):
        res = convert_to_arabic('MCDLI')
        self.assertEqual(1451, res)

    def test_MCDLII(self):
        res = convert_to_arabic('MCDLII')
        self.assertEqual(1452, res)

    def test_MCDLIII(self):
        res = convert_to_arabic('MCDLIII')
        self.assertEqual(1453, res)

    def test_MCDLIV(self):
        res = convert_to_arabic('MCDLIV')
        self.assertEqual(1454, res)

    def test_MCDLV(self):
        res = convert_to_arabic('MCDLV')
        self.assertEqual(1455, res)

    def test_MCDLVI(self):
        res = convert_to_arabic('MCDLVI')
        self.assertEqual(1456, res)

    def test_MCDLVII(self):
        res = convert_to_arabic('MCDLVII')
        self.assertEqual(1457, res)

    def test_MCDLVIII(self):
        res = convert_to_arabic('MCDLVIII')
        self.assertEqual(1458, res)

    def test_MCDLIX(self):
        res = convert_to_arabic('MCDLIX')
        self.assertEqual(1459, res)

    def test_MCDLX(self):
        res = convert_to_arabic('MCDLX')
        self.assertEqual(1460, res)

    def test_MCDLXI(self):
        res = convert_to_arabic('MCDLXI')
        self.assertEqual(1461, res)

    def test_MCDLXII(self):
        res = convert_to_arabic('MCDLXII')
        self.assertEqual(1462, res)

    def test_MCDLXIII(self):
        res = convert_to_arabic('MCDLXIII')
        self.assertEqual(1463, res)

    def test_MCDLXIV(self):
        res = convert_to_arabic('MCDLXIV')
        self.assertEqual(1464, res)

    def test_MCDLXV(self):
        res = convert_to_arabic('MCDLXV')
        self.assertEqual(1465, res)

    def test_MCDLXVI(self):
        res = convert_to_arabic('MCDLXVI')
        self.assertEqual(1466, res)

    def test_MCDLXVII(self):
        res = convert_to_arabic('MCDLXVII')
        self.assertEqual(1467, res)

    def test_MCDLXVIII(self):
        res = convert_to_arabic('MCDLXVIII')
        self.assertEqual(1468, res)

    def test_MCDLXIX(self):
        res = convert_to_arabic('MCDLXIX')
        self.assertEqual(1469, res)

    def test_MCDLXX(self):
        res = convert_to_arabic('MCDLXX')
        self.assertEqual(1470, res)

    def test_MCDLXXI(self):
        res = convert_to_arabic('MCDLXXI')
        self.assertEqual(1471, res)

    def test_MCDLXXII(self):
        res = convert_to_arabic('MCDLXXII')
        self.assertEqual(1472, res)

    def test_MCDLXXIII(self):
        res = convert_to_arabic('MCDLXXIII')
        self.assertEqual(1473, res)

    def test_MCDLXXIV(self):
        res = convert_to_arabic('MCDLXXIV')
        self.assertEqual(1474, res)

    def test_MCDLXXV(self):
        res = convert_to_arabic('MCDLXXV')
        self.assertEqual(1475, res)

    def test_MCDLXXVI(self):
        res = convert_to_arabic('MCDLXXVI')
        self.assertEqual(1476, res)

    def test_MCDLXXVII(self):
        res = convert_to_arabic('MCDLXXVII')
        self.assertEqual(1477, res)

    def test_MCDLXXVIII(self):
        res = convert_to_arabic('MCDLXXVIII')
        self.assertEqual(1478, res)

    def test_MCDLXXIX(self):
        res = convert_to_arabic('MCDLXXIX')
        self.assertEqual(1479, res)

    def test_MCDLXXX(self):
        res = convert_to_arabic('MCDLXXX')
        self.assertEqual(1480, res)

    def test_MCDLXXXI(self):
        res = convert_to_arabic('MCDLXXXI')
        self.assertEqual(1481, res)

    def test_MCDLXXXII(self):
        res = convert_to_arabic('MCDLXXXII')
        self.assertEqual(1482, res)

    def test_MCDLXXXIII(self):
        res = convert_to_arabic('MCDLXXXIII')
        self.assertEqual(1483, res)

    def test_MCDLXXXIV(self):
        res = convert_to_arabic('MCDLXXXIV')
        self.assertEqual(1484, res)

    def test_MCDLXXXV(self):
        res = convert_to_arabic('MCDLXXXV')
        self.assertEqual(1485, res)

    def test_MCDLXXXVI(self):
        res = convert_to_arabic('MCDLXXXVI')
        self.assertEqual(1486, res)

    def test_MCDLXXXVII(self):
        res = convert_to_arabic('MCDLXXXVII')
        self.assertEqual(1487, res)

    def test_MCDLXXXVIII(self):
        res = convert_to_arabic('MCDLXXXVIII')
        self.assertEqual(1488, res)

    def test_MCDLXXXIX(self):
        res = convert_to_arabic('MCDLXXXIX')
        self.assertEqual(1489, res)

    def test_MCDXC(self):
        res = convert_to_arabic('MCDXC')
        self.assertEqual(1490, res)

    def test_MCDXCI(self):
        res = convert_to_arabic('MCDXCI')
        self.assertEqual(1491, res)

    def test_MCDXCII(self):
        res = convert_to_arabic('MCDXCII')
        self.assertEqual(1492, res)

    def test_MCDXCIII(self):
        res = convert_to_arabic('MCDXCIII')
        self.assertEqual(1493, res)

    def test_MCDXCIV(self):
        res = convert_to_arabic('MCDXCIV')
        self.assertEqual(1494, res)

    def test_MCDXCV(self):
        res = convert_to_arabic('MCDXCV')
        self.assertEqual(1495, res)

    def test_MCDXCVI(self):
        res = convert_to_arabic('MCDXCVI')
        self.assertEqual(1496, res)

    def test_MCDXCVII(self):
        res = convert_to_arabic('MCDXCVII')
        self.assertEqual(1497, res)

    def test_MCDXCVIII(self):
        res = convert_to_arabic('MCDXCVIII')
        self.assertEqual(1498, res)

    def test_MCDXCIX(self):
        res = convert_to_arabic('MCDXCIX')
        self.assertEqual(1499, res)

    def test_MD(self):
        res = convert_to_arabic('MD')
        self.assertEqual(1500, res)

    def test_MDI(self):
        res = convert_to_arabic('MDI')
        self.assertEqual(1501, res)

    def test_MDII(self):
        res = convert_to_arabic('MDII')
        self.assertEqual(1502, res)

    def test_MDIII(self):
        res = convert_to_arabic('MDIII')
        self.assertEqual(1503, res)

    def test_MDIV(self):
        res = convert_to_arabic('MDIV')
        self.assertEqual(1504, res)

    def test_MDV(self):
        res = convert_to_arabic('MDV')
        self.assertEqual(1505, res)

    def test_MDVI(self):
        res = convert_to_arabic('MDVI')
        self.assertEqual(1506, res)

    def test_MDVII(self):
        res = convert_to_arabic('MDVII')
        self.assertEqual(1507, res)

    def test_MDVIII(self):
        res = convert_to_arabic('MDVIII')
        self.assertEqual(1508, res)

    def test_MDIX(self):
        res = convert_to_arabic('MDIX')
        self.assertEqual(1509, res)

    def test_MDX(self):
        res = convert_to_arabic('MDX')
        self.assertEqual(1510, res)

    def test_MDXI(self):
        res = convert_to_arabic('MDXI')
        self.assertEqual(1511, res)

    def test_MDXII(self):
        res = convert_to_arabic('MDXII')
        self.assertEqual(1512, res)

    def test_MDXIII(self):
        res = convert_to_arabic('MDXIII')
        self.assertEqual(1513, res)

    def test_MDXIV(self):
        res = convert_to_arabic('MDXIV')
        self.assertEqual(1514, res)

    def test_MDXV(self):
        res = convert_to_arabic('MDXV')
        self.assertEqual(1515, res)

    def test_MDXVI(self):
        res = convert_to_arabic('MDXVI')
        self.assertEqual(1516, res)

    def test_MDXVII(self):
        res = convert_to_arabic('MDXVII')
        self.assertEqual(1517, res)

    def test_MDXVIII(self):
        res = convert_to_arabic('MDXVIII')
        self.assertEqual(1518, res)

    def test_MDXIX(self):
        res = convert_to_arabic('MDXIX')
        self.assertEqual(1519, res)

    def test_MDXX(self):
        res = convert_to_arabic('MDXX')
        self.assertEqual(1520, res)

    def test_MDXXI(self):
        res = convert_to_arabic('MDXXI')
        self.assertEqual(1521, res)

    def test_MDXXII(self):
        res = convert_to_arabic('MDXXII')
        self.assertEqual(1522, res)

    def test_MDXXIII(self):
        res = convert_to_arabic('MDXXIII')
        self.assertEqual(1523, res)

    def test_MDXXIV(self):
        res = convert_to_arabic('MDXXIV')
        self.assertEqual(1524, res)

    def test_MDXXV(self):
        res = convert_to_arabic('MDXXV')
        self.assertEqual(1525, res)

    def test_MDXXVI(self):
        res = convert_to_arabic('MDXXVI')
        self.assertEqual(1526, res)

    def test_MDXXVII(self):
        res = convert_to_arabic('MDXXVII')
        self.assertEqual(1527, res)

    def test_MDXXVIII(self):
        res = convert_to_arabic('MDXXVIII')
        self.assertEqual(1528, res)

    def test_MDXXIX(self):
        res = convert_to_arabic('MDXXIX')
        self.assertEqual(1529, res)

    def test_MDXXX(self):
        res = convert_to_arabic('MDXXX')
        self.assertEqual(1530, res)

    def test_MDXXXI(self):
        res = convert_to_arabic('MDXXXI')
        self.assertEqual(1531, res)

    def test_MDXXXII(self):
        res = convert_to_arabic('MDXXXII')
        self.assertEqual(1532, res)

    def test_MDXXXIII(self):
        res = convert_to_arabic('MDXXXIII')
        self.assertEqual(1533, res)

    def test_MDXXXIV(self):
        res = convert_to_arabic('MDXXXIV')
        self.assertEqual(1534, res)

    def test_MDXXXV(self):
        res = convert_to_arabic('MDXXXV')
        self.assertEqual(1535, res)

    def test_MDXXXVI(self):
        res = convert_to_arabic('MDXXXVI')
        self.assertEqual(1536, res)

    def test_MDXXXVII(self):
        res = convert_to_arabic('MDXXXVII')
        self.assertEqual(1537, res)

    def test_MDXXXVIII(self):
        res = convert_to_arabic('MDXXXVIII')
        self.assertEqual(1538, res)

    def test_MDXXXIX(self):
        res = convert_to_arabic('MDXXXIX')
        self.assertEqual(1539, res)

    def test_MDXL(self):
        res = convert_to_arabic('MDXL')
        self.assertEqual(1540, res)

    def test_MDXLI(self):
        res = convert_to_arabic('MDXLI')
        self.assertEqual(1541, res)

    def test_MDXLII(self):
        res = convert_to_arabic('MDXLII')
        self.assertEqual(1542, res)

    def test_MDXLIII(self):
        res = convert_to_arabic('MDXLIII')
        self.assertEqual(1543, res)

    def test_MDXLIV(self):
        res = convert_to_arabic('MDXLIV')
        self.assertEqual(1544, res)

    def test_MDXLV(self):
        res = convert_to_arabic('MDXLV')
        self.assertEqual(1545, res)

    def test_MDXLVI(self):
        res = convert_to_arabic('MDXLVI')
        self.assertEqual(1546, res)

    def test_MDXLVII(self):
        res = convert_to_arabic('MDXLVII')
        self.assertEqual(1547, res)

    def test_MDXLVIII(self):
        res = convert_to_arabic('MDXLVIII')
        self.assertEqual(1548, res)

    def test_MDXLIX(self):
        res = convert_to_arabic('MDXLIX')
        self.assertEqual(1549, res)

    def test_MDL(self):
        res = convert_to_arabic('MDL')
        self.assertEqual(1550, res)

    def test_MDLI(self):
        res = convert_to_arabic('MDLI')
        self.assertEqual(1551, res)

    def test_MDLII(self):
        res = convert_to_arabic('MDLII')
        self.assertEqual(1552, res)

    def test_MDLIII(self):
        res = convert_to_arabic('MDLIII')
        self.assertEqual(1553, res)

    def test_MDLIV(self):
        res = convert_to_arabic('MDLIV')
        self.assertEqual(1554, res)

    def test_MDLV(self):
        res = convert_to_arabic('MDLV')
        self.assertEqual(1555, res)

    def test_MDLVI(self):
        res = convert_to_arabic('MDLVI')
        self.assertEqual(1556, res)

    def test_MDLVII(self):
        res = convert_to_arabic('MDLVII')
        self.assertEqual(1557, res)

    def test_MDLVIII(self):
        res = convert_to_arabic('MDLVIII')
        self.assertEqual(1558, res)

    def test_MDLIX(self):
        res = convert_to_arabic('MDLIX')
        self.assertEqual(1559, res)

    def test_MDLX(self):
        res = convert_to_arabic('MDLX')
        self.assertEqual(1560, res)

    def test_MDLXI(self):
        res = convert_to_arabic('MDLXI')
        self.assertEqual(1561, res)

    def test_MDLXII(self):
        res = convert_to_arabic('MDLXII')
        self.assertEqual(1562, res)

    def test_MDLXIII(self):
        res = convert_to_arabic('MDLXIII')
        self.assertEqual(1563, res)

    def test_MDLXIV(self):
        res = convert_to_arabic('MDLXIV')
        self.assertEqual(1564, res)

    def test_MDLXV(self):
        res = convert_to_arabic('MDLXV')
        self.assertEqual(1565, res)

    def test_MDLXVI(self):
        res = convert_to_arabic('MDLXVI')
        self.assertEqual(1566, res)

    def test_MDLXVII(self):
        res = convert_to_arabic('MDLXVII')
        self.assertEqual(1567, res)

    def test_MDLXVIII(self):
        res = convert_to_arabic('MDLXVIII')
        self.assertEqual(1568, res)

    def test_MDLXIX(self):
        res = convert_to_arabic('MDLXIX')
        self.assertEqual(1569, res)

    def test_MDLXX(self):
        res = convert_to_arabic('MDLXX')
        self.assertEqual(1570, res)

    def test_MDLXXI(self):
        res = convert_to_arabic('MDLXXI')
        self.assertEqual(1571, res)

    def test_MDLXXII(self):
        res = convert_to_arabic('MDLXXII')
        self.assertEqual(1572, res)

    def test_MDLXXIII(self):
        res = convert_to_arabic('MDLXXIII')
        self.assertEqual(1573, res)

    def test_MDLXXIV(self):
        res = convert_to_arabic('MDLXXIV')
        self.assertEqual(1574, res)

    def test_MDLXXV(self):
        res = convert_to_arabic('MDLXXV')
        self.assertEqual(1575, res)

    def test_MDLXXVI(self):
        res = convert_to_arabic('MDLXXVI')
        self.assertEqual(1576, res)

    def test_MDLXXVII(self):
        res = convert_to_arabic('MDLXXVII')
        self.assertEqual(1577, res)

    def test_MDLXXVIII(self):
        res = convert_to_arabic('MDLXXVIII')
        self.assertEqual(1578, res)

    def test_MDLXXIX(self):
        res = convert_to_arabic('MDLXXIX')
        self.assertEqual(1579, res)

    def test_MDLXXX(self):
        res = convert_to_arabic('MDLXXX')
        self.assertEqual(1580, res)

    def test_MDLXXXI(self):
        res = convert_to_arabic('MDLXXXI')
        self.assertEqual(1581, res)

    def test_MDLXXXII(self):
        res = convert_to_arabic('MDLXXXII')
        self.assertEqual(1582, res)

    def test_MDLXXXIII(self):
        res = convert_to_arabic('MDLXXXIII')
        self.assertEqual(1583, res)

    def test_MDLXXXIV(self):
        res = convert_to_arabic('MDLXXXIV')
        self.assertEqual(1584, res)

    def test_MDLXXXV(self):
        res = convert_to_arabic('MDLXXXV')
        self.assertEqual(1585, res)

    def test_MDLXXXVI(self):
        res = convert_to_arabic('MDLXXXVI')
        self.assertEqual(1586, res)

    def test_MDLXXXVII(self):
        res = convert_to_arabic('MDLXXXVII')
        self.assertEqual(1587, res)

    def test_MDLXXXVIII(self):
        res = convert_to_arabic('MDLXXXVIII')
        self.assertEqual(1588, res)

    def test_MDLXXXIX(self):
        res = convert_to_arabic('MDLXXXIX')
        self.assertEqual(1589, res)

    def test_MDXC(self):
        res = convert_to_arabic('MDXC')
        self.assertEqual(1590, res)

    def test_MDXCI(self):
        res = convert_to_arabic('MDXCI')
        self.assertEqual(1591, res)

    def test_MDXCII(self):
        res = convert_to_arabic('MDXCII')
        self.assertEqual(1592, res)

    def test_MDXCIII(self):
        res = convert_to_arabic('MDXCIII')
        self.assertEqual(1593, res)

    def test_MDXCIV(self):
        res = convert_to_arabic('MDXCIV')
        self.assertEqual(1594, res)

    def test_MDXCV(self):
        res = convert_to_arabic('MDXCV')
        self.assertEqual(1595, res)

    def test_MDXCVI(self):
        res = convert_to_arabic('MDXCVI')
        self.assertEqual(1596, res)

    def test_MDXCVII(self):
        res = convert_to_arabic('MDXCVII')
        self.assertEqual(1597, res)

    def test_MDXCVIII(self):
        res = convert_to_arabic('MDXCVIII')
        self.assertEqual(1598, res)

    def test_MDXCIX(self):
        res = convert_to_arabic('MDXCIX')
        self.assertEqual(1599, res)

    def test_MDC(self):
        res = convert_to_arabic('MDC')
        self.assertEqual(1600, res)

    def test_MDCI(self):
        res = convert_to_arabic('MDCI')
        self.assertEqual(1601, res)

    def test_MDCII(self):
        res = convert_to_arabic('MDCII')
        self.assertEqual(1602, res)

    def test_MDCIII(self):
        res = convert_to_arabic('MDCIII')
        self.assertEqual(1603, res)

    def test_MDCIV(self):
        res = convert_to_arabic('MDCIV')
        self.assertEqual(1604, res)

    def test_MDCV(self):
        res = convert_to_arabic('MDCV')
        self.assertEqual(1605, res)

    def test_MDCVI(self):
        res = convert_to_arabic('MDCVI')
        self.assertEqual(1606, res)

    def test_MDCVII(self):
        res = convert_to_arabic('MDCVII')
        self.assertEqual(1607, res)

    def test_MDCVIII(self):
        res = convert_to_arabic('MDCVIII')
        self.assertEqual(1608, res)

    def test_MDCIX(self):
        res = convert_to_arabic('MDCIX')
        self.assertEqual(1609, res)

    def test_MDCX(self):
        res = convert_to_arabic('MDCX')
        self.assertEqual(1610, res)

    def test_MDCXI(self):
        res = convert_to_arabic('MDCXI')
        self.assertEqual(1611, res)

    def test_MDCXII(self):
        res = convert_to_arabic('MDCXII')
        self.assertEqual(1612, res)

    def test_MDCXIII(self):
        res = convert_to_arabic('MDCXIII')
        self.assertEqual(1613, res)

    def test_MDCXIV(self):
        res = convert_to_arabic('MDCXIV')
        self.assertEqual(1614, res)

    def test_MDCXV(self):
        res = convert_to_arabic('MDCXV')
        self.assertEqual(1615, res)

    def test_MDCXVI(self):
        res = convert_to_arabic('MDCXVI')
        self.assertEqual(1616, res)

    def test_MDCXVII(self):
        res = convert_to_arabic('MDCXVII')
        self.assertEqual(1617, res)

    def test_MDCXVIII(self):
        res = convert_to_arabic('MDCXVIII')
        self.assertEqual(1618, res)

    def test_MDCXIX(self):
        res = convert_to_arabic('MDCXIX')
        self.assertEqual(1619, res)

    def test_MDCXX(self):
        res = convert_to_arabic('MDCXX')
        self.assertEqual(1620, res)

    def test_MDCXXI(self):
        res = convert_to_arabic('MDCXXI')
        self.assertEqual(1621, res)

    def test_MDCXXII(self):
        res = convert_to_arabic('MDCXXII')
        self.assertEqual(1622, res)

    def test_MDCXXIII(self):
        res = convert_to_arabic('MDCXXIII')
        self.assertEqual(1623, res)

    def test_MDCXXIV(self):
        res = convert_to_arabic('MDCXXIV')
        self.assertEqual(1624, res)

    def test_MDCXXV(self):
        res = convert_to_arabic('MDCXXV')
        self.assertEqual(1625, res)

    def test_MDCXXVI(self):
        res = convert_to_arabic('MDCXXVI')
        self.assertEqual(1626, res)

    def test_MDCXXVII(self):
        res = convert_to_arabic('MDCXXVII')
        self.assertEqual(1627, res)

    def test_MDCXXVIII(self):
        res = convert_to_arabic('MDCXXVIII')
        self.assertEqual(1628, res)

    def test_MDCXXIX(self):
        res = convert_to_arabic('MDCXXIX')
        self.assertEqual(1629, res)

    def test_MDCXXX(self):
        res = convert_to_arabic('MDCXXX')
        self.assertEqual(1630, res)

    def test_MDCXXXI(self):
        res = convert_to_arabic('MDCXXXI')
        self.assertEqual(1631, res)

    def test_MDCXXXII(self):
        res = convert_to_arabic('MDCXXXII')
        self.assertEqual(1632, res)

    def test_MDCXXXIII(self):
        res = convert_to_arabic('MDCXXXIII')
        self.assertEqual(1633, res)

    def test_MDCXXXIV(self):
        res = convert_to_arabic('MDCXXXIV')
        self.assertEqual(1634, res)

    def test_MDCXXXV(self):
        res = convert_to_arabic('MDCXXXV')
        self.assertEqual(1635, res)

    def test_MDCXXXVI(self):
        res = convert_to_arabic('MDCXXXVI')
        self.assertEqual(1636, res)

    def test_MDCXXXVII(self):
        res = convert_to_arabic('MDCXXXVII')
        self.assertEqual(1637, res)

    def test_MDCXXXVIII(self):
        res = convert_to_arabic('MDCXXXVIII')
        self.assertEqual(1638, res)

    def test_MDCXXXIX(self):
        res = convert_to_arabic('MDCXXXIX')
        self.assertEqual(1639, res)

    def test_MDCXL(self):
        res = convert_to_arabic('MDCXL')
        self.assertEqual(1640, res)

    def test_MDCXLI(self):
        res = convert_to_arabic('MDCXLI')
        self.assertEqual(1641, res)

    def test_MDCXLII(self):
        res = convert_to_arabic('MDCXLII')
        self.assertEqual(1642, res)

    def test_MDCXLIII(self):
        res = convert_to_arabic('MDCXLIII')
        self.assertEqual(1643, res)

    def test_MDCXLIV(self):
        res = convert_to_arabic('MDCXLIV')
        self.assertEqual(1644, res)

    def test_MDCXLV(self):
        res = convert_to_arabic('MDCXLV')
        self.assertEqual(1645, res)

    def test_MDCXLVI(self):
        res = convert_to_arabic('MDCXLVI')
        self.assertEqual(1646, res)

    def test_MDCXLVII(self):
        res = convert_to_arabic('MDCXLVII')
        self.assertEqual(1647, res)

    def test_MDCXLVIII(self):
        res = convert_to_arabic('MDCXLVIII')
        self.assertEqual(1648, res)

    def test_MDCXLIX(self):
        res = convert_to_arabic('MDCXLIX')
        self.assertEqual(1649, res)

    def test_MDCL(self):
        res = convert_to_arabic('MDCL')
        self.assertEqual(1650, res)

    def test_MDCLI(self):
        res = convert_to_arabic('MDCLI')
        self.assertEqual(1651, res)

    def test_MDCLII(self):
        res = convert_to_arabic('MDCLII')
        self.assertEqual(1652, res)

    def test_MDCLIII(self):
        res = convert_to_arabic('MDCLIII')
        self.assertEqual(1653, res)

    def test_MDCLIV(self):
        res = convert_to_arabic('MDCLIV')
        self.assertEqual(1654, res)

    def test_MDCLV(self):
        res = convert_to_arabic('MDCLV')
        self.assertEqual(1655, res)

    def test_MDCLVI(self):
        res = convert_to_arabic('MDCLVI')
        self.assertEqual(1656, res)

    def test_MDCLVII(self):
        res = convert_to_arabic('MDCLVII')
        self.assertEqual(1657, res)

    def test_MDCLVIII(self):
        res = convert_to_arabic('MDCLVIII')
        self.assertEqual(1658, res)

    def test_MDCLIX(self):
        res = convert_to_arabic('MDCLIX')
        self.assertEqual(1659, res)

    def test_MDCLX(self):
        res = convert_to_arabic('MDCLX')
        self.assertEqual(1660, res)

    def test_MDCLXI(self):
        res = convert_to_arabic('MDCLXI')
        self.assertEqual(1661, res)

    def test_MDCLXII(self):
        res = convert_to_arabic('MDCLXII')
        self.assertEqual(1662, res)

    def test_MDCLXIII(self):
        res = convert_to_arabic('MDCLXIII')
        self.assertEqual(1663, res)

    def test_MDCLXIV(self):
        res = convert_to_arabic('MDCLXIV')
        self.assertEqual(1664, res)

    def test_MDCLXV(self):
        res = convert_to_arabic('MDCLXV')
        self.assertEqual(1665, res)

    def test_MDCLXVI(self):
        res = convert_to_arabic('MDCLXVI')
        self.assertEqual(1666, res)

    def test_MDCLXVII(self):
        res = convert_to_arabic('MDCLXVII')
        self.assertEqual(1667, res)

    def test_MDCLXVIII(self):
        res = convert_to_arabic('MDCLXVIII')
        self.assertEqual(1668, res)

    def test_MDCLXIX(self):
        res = convert_to_arabic('MDCLXIX')
        self.assertEqual(1669, res)

    def test_MDCLXX(self):
        res = convert_to_arabic('MDCLXX')
        self.assertEqual(1670, res)

    def test_MDCLXXI(self):
        res = convert_to_arabic('MDCLXXI')
        self.assertEqual(1671, res)

    def test_MDCLXXII(self):
        res = convert_to_arabic('MDCLXXII')
        self.assertEqual(1672, res)

    def test_MDCLXXIII(self):
        res = convert_to_arabic('MDCLXXIII')
        self.assertEqual(1673, res)

    def test_MDCLXXIV(self):
        res = convert_to_arabic('MDCLXXIV')
        self.assertEqual(1674, res)

    def test_MDCLXXV(self):
        res = convert_to_arabic('MDCLXXV')
        self.assertEqual(1675, res)

    def test_MDCLXXVI(self):
        res = convert_to_arabic('MDCLXXVI')
        self.assertEqual(1676, res)

    def test_MDCLXXVII(self):
        res = convert_to_arabic('MDCLXXVII')
        self.assertEqual(1677, res)

    def test_MDCLXXVIII(self):
        res = convert_to_arabic('MDCLXXVIII')
        self.assertEqual(1678, res)

    def test_MDCLXXIX(self):
        res = convert_to_arabic('MDCLXXIX')
        self.assertEqual(1679, res)

    def test_MDCLXXX(self):
        res = convert_to_arabic('MDCLXXX')
        self.assertEqual(1680, res)

    def test_MDCLXXXI(self):
        res = convert_to_arabic('MDCLXXXI')
        self.assertEqual(1681, res)

    def test_MDCLXXXII(self):
        res = convert_to_arabic('MDCLXXXII')
        self.assertEqual(1682, res)

    def test_MDCLXXXIII(self):
        res = convert_to_arabic('MDCLXXXIII')
        self.assertEqual(1683, res)

    def test_MDCLXXXIV(self):
        res = convert_to_arabic('MDCLXXXIV')
        self.assertEqual(1684, res)

    def test_MDCLXXXV(self):
        res = convert_to_arabic('MDCLXXXV')
        self.assertEqual(1685, res)

    def test_MDCLXXXVI(self):
        res = convert_to_arabic('MDCLXXXVI')
        self.assertEqual(1686, res)

    def test_MDCLXXXVII(self):
        res = convert_to_arabic('MDCLXXXVII')
        self.assertEqual(1687, res)

    def test_MDCLXXXVIII(self):
        res = convert_to_arabic('MDCLXXXVIII')
        self.assertEqual(1688, res)

    def test_MDCLXXXIX(self):
        res = convert_to_arabic('MDCLXXXIX')
        self.assertEqual(1689, res)

    def test_MDCXC(self):
        res = convert_to_arabic('MDCXC')
        self.assertEqual(1690, res)

    def test_MDCXCI(self):
        res = convert_to_arabic('MDCXCI')
        self.assertEqual(1691, res)

    def test_MDCXCII(self):
        res = convert_to_arabic('MDCXCII')
        self.assertEqual(1692, res)

    def test_MDCXCIII(self):
        res = convert_to_arabic('MDCXCIII')
        self.assertEqual(1693, res)

    def test_MDCXCIV(self):
        res = convert_to_arabic('MDCXCIV')
        self.assertEqual(1694, res)

    def test_MDCXCV(self):
        res = convert_to_arabic('MDCXCV')
        self.assertEqual(1695, res)

    def test_MDCXCVI(self):
        res = convert_to_arabic('MDCXCVI')
        self.assertEqual(1696, res)

    def test_MDCXCVII(self):
        res = convert_to_arabic('MDCXCVII')
        self.assertEqual(1697, res)

    def test_MDCXCVIII(self):
        res = convert_to_arabic('MDCXCVIII')
        self.assertEqual(1698, res)

    def test_MDCXCIX(self):
        res = convert_to_arabic('MDCXCIX')
        self.assertEqual(1699, res)

    def test_MDCC(self):
        res = convert_to_arabic('MDCC')
        self.assertEqual(1700, res)

    def test_MDCCI(self):
        res = convert_to_arabic('MDCCI')
        self.assertEqual(1701, res)

    def test_MDCCII(self):
        res = convert_to_arabic('MDCCII')
        self.assertEqual(1702, res)

    def test_MDCCIII(self):
        res = convert_to_arabic('MDCCIII')
        self.assertEqual(1703, res)

    def test_MDCCIV(self):
        res = convert_to_arabic('MDCCIV')
        self.assertEqual(1704, res)

    def test_MDCCV(self):
        res = convert_to_arabic('MDCCV')
        self.assertEqual(1705, res)

    def test_MDCCVI(self):
        res = convert_to_arabic('MDCCVI')
        self.assertEqual(1706, res)

    def test_MDCCVII(self):
        res = convert_to_arabic('MDCCVII')
        self.assertEqual(1707, res)

    def test_MDCCVIII(self):
        res = convert_to_arabic('MDCCVIII')
        self.assertEqual(1708, res)

    def test_MDCCIX(self):
        res = convert_to_arabic('MDCCIX')
        self.assertEqual(1709, res)

    def test_MDCCX(self):
        res = convert_to_arabic('MDCCX')
        self.assertEqual(1710, res)

    def test_MDCCXI(self):
        res = convert_to_arabic('MDCCXI')
        self.assertEqual(1711, res)

    def test_MDCCXII(self):
        res = convert_to_arabic('MDCCXII')
        self.assertEqual(1712, res)

    def test_MDCCXIII(self):
        res = convert_to_arabic('MDCCXIII')
        self.assertEqual(1713, res)

    def test_MDCCXIV(self):
        res = convert_to_arabic('MDCCXIV')
        self.assertEqual(1714, res)

    def test_MDCCXV(self):
        res = convert_to_arabic('MDCCXV')
        self.assertEqual(1715, res)

    def test_MDCCXVI(self):
        res = convert_to_arabic('MDCCXVI')
        self.assertEqual(1716, res)

    def test_MDCCXVII(self):
        res = convert_to_arabic('MDCCXVII')
        self.assertEqual(1717, res)

    def test_MDCCXVIII(self):
        res = convert_to_arabic('MDCCXVIII')
        self.assertEqual(1718, res)

    def test_MDCCXIX(self):
        res = convert_to_arabic('MDCCXIX')
        self.assertEqual(1719, res)

    def test_MDCCXX(self):
        res = convert_to_arabic('MDCCXX')
        self.assertEqual(1720, res)

    def test_MDCCXXI(self):
        res = convert_to_arabic('MDCCXXI')
        self.assertEqual(1721, res)

    def test_MDCCXXII(self):
        res = convert_to_arabic('MDCCXXII')
        self.assertEqual(1722, res)

    def test_MDCCXXIII(self):
        res = convert_to_arabic('MDCCXXIII')
        self.assertEqual(1723, res)

    def test_MDCCXXIV(self):
        res = convert_to_arabic('MDCCXXIV')
        self.assertEqual(1724, res)

    def test_MDCCXXV(self):
        res = convert_to_arabic('MDCCXXV')
        self.assertEqual(1725, res)

    def test_MDCCXXVI(self):
        res = convert_to_arabic('MDCCXXVI')
        self.assertEqual(1726, res)

    def test_MDCCXXVII(self):
        res = convert_to_arabic('MDCCXXVII')
        self.assertEqual(1727, res)

    def test_MDCCXXVIII(self):
        res = convert_to_arabic('MDCCXXVIII')
        self.assertEqual(1728, res)

    def test_MDCCXXIX(self):
        res = convert_to_arabic('MDCCXXIX')
        self.assertEqual(1729, res)

    def test_MDCCXXX(self):
        res = convert_to_arabic('MDCCXXX')
        self.assertEqual(1730, res)

    def test_MDCCXXXI(self):
        res = convert_to_arabic('MDCCXXXI')
        self.assertEqual(1731, res)

    def test_MDCCXXXII(self):
        res = convert_to_arabic('MDCCXXXII')
        self.assertEqual(1732, res)

    def test_MDCCXXXIII(self):
        res = convert_to_arabic('MDCCXXXIII')
        self.assertEqual(1733, res)

    def test_MDCCXXXIV(self):
        res = convert_to_arabic('MDCCXXXIV')
        self.assertEqual(1734, res)

    def test_MDCCXXXV(self):
        res = convert_to_arabic('MDCCXXXV')
        self.assertEqual(1735, res)

    def test_MDCCXXXVI(self):
        res = convert_to_arabic('MDCCXXXVI')
        self.assertEqual(1736, res)

    def test_MDCCXXXVII(self):
        res = convert_to_arabic('MDCCXXXVII')
        self.assertEqual(1737, res)

    def test_MDCCXXXVIII(self):
        res = convert_to_arabic('MDCCXXXVIII')
        self.assertEqual(1738, res)

    def test_MDCCXXXIX(self):
        res = convert_to_arabic('MDCCXXXIX')
        self.assertEqual(1739, res)

    def test_MDCCXL(self):
        res = convert_to_arabic('MDCCXL')
        self.assertEqual(1740, res)

    def test_MDCCXLI(self):
        res = convert_to_arabic('MDCCXLI')
        self.assertEqual(1741, res)

    def test_MDCCXLII(self):
        res = convert_to_arabic('MDCCXLII')
        self.assertEqual(1742, res)

    def test_MDCCXLIII(self):
        res = convert_to_arabic('MDCCXLIII')
        self.assertEqual(1743, res)

    def test_MDCCXLIV(self):
        res = convert_to_arabic('MDCCXLIV')
        self.assertEqual(1744, res)

    def test_MDCCXLV(self):
        res = convert_to_arabic('MDCCXLV')
        self.assertEqual(1745, res)

    def test_MDCCXLVI(self):
        res = convert_to_arabic('MDCCXLVI')
        self.assertEqual(1746, res)

    def test_MDCCXLVII(self):
        res = convert_to_arabic('MDCCXLVII')
        self.assertEqual(1747, res)

    def test_MDCCXLVIII(self):
        res = convert_to_arabic('MDCCXLVIII')
        self.assertEqual(1748, res)

    def test_MDCCXLIX(self):
        res = convert_to_arabic('MDCCXLIX')
        self.assertEqual(1749, res)

    def test_MDCCL(self):
        res = convert_to_arabic('MDCCL')
        self.assertEqual(1750, res)

    def test_MDCCLI(self):
        res = convert_to_arabic('MDCCLI')
        self.assertEqual(1751, res)

    def test_MDCCLII(self):
        res = convert_to_arabic('MDCCLII')
        self.assertEqual(1752, res)

    def test_MDCCLIII(self):
        res = convert_to_arabic('MDCCLIII')
        self.assertEqual(1753, res)

    def test_MDCCLIV(self):
        res = convert_to_arabic('MDCCLIV')
        self.assertEqual(1754, res)

    def test_MDCCLV(self):
        res = convert_to_arabic('MDCCLV')
        self.assertEqual(1755, res)

    def test_MDCCLVI(self):
        res = convert_to_arabic('MDCCLVI')
        self.assertEqual(1756, res)

    def test_MDCCLVII(self):
        res = convert_to_arabic('MDCCLVII')
        self.assertEqual(1757, res)

    def test_MDCCLVIII(self):
        res = convert_to_arabic('MDCCLVIII')
        self.assertEqual(1758, res)

    def test_MDCCLIX(self):
        res = convert_to_arabic('MDCCLIX')
        self.assertEqual(1759, res)

    def test_MDCCLX(self):
        res = convert_to_arabic('MDCCLX')
        self.assertEqual(1760, res)

    def test_MDCCLXI(self):
        res = convert_to_arabic('MDCCLXI')
        self.assertEqual(1761, res)

    def test_MDCCLXII(self):
        res = convert_to_arabic('MDCCLXII')
        self.assertEqual(1762, res)

    def test_MDCCLXIII(self):
        res = convert_to_arabic('MDCCLXIII')
        self.assertEqual(1763, res)

    def test_MDCCLXIV(self):
        res = convert_to_arabic('MDCCLXIV')
        self.assertEqual(1764, res)

    def test_MDCCLXV(self):
        res = convert_to_arabic('MDCCLXV')
        self.assertEqual(1765, res)

    def test_MDCCLXVI(self):
        res = convert_to_arabic('MDCCLXVI')
        self.assertEqual(1766, res)

    def test_MDCCLXVII(self):
        res = convert_to_arabic('MDCCLXVII')
        self.assertEqual(1767, res)

    def test_MDCCLXVIII(self):
        res = convert_to_arabic('MDCCLXVIII')
        self.assertEqual(1768, res)

    def test_MDCCLXIX(self):
        res = convert_to_arabic('MDCCLXIX')
        self.assertEqual(1769, res)

    def test_MDCCLXX(self):
        res = convert_to_arabic('MDCCLXX')
        self.assertEqual(1770, res)

    def test_MDCCLXXI(self):
        res = convert_to_arabic('MDCCLXXI')
        self.assertEqual(1771, res)

    def test_MDCCLXXII(self):
        res = convert_to_arabic('MDCCLXXII')
        self.assertEqual(1772, res)

    def test_MDCCLXXIII(self):
        res = convert_to_arabic('MDCCLXXIII')
        self.assertEqual(1773, res)

    def test_MDCCLXXIV(self):
        res = convert_to_arabic('MDCCLXXIV')
        self.assertEqual(1774, res)

    def test_MDCCLXXV(self):
        res = convert_to_arabic('MDCCLXXV')
        self.assertEqual(1775, res)

    def test_MDCCLXXVI(self):
        res = convert_to_arabic('MDCCLXXVI')
        self.assertEqual(1776, res)

    def test_MDCCLXXVII(self):
        res = convert_to_arabic('MDCCLXXVII')
        self.assertEqual(1777, res)

    def test_MDCCLXXVIII(self):
        res = convert_to_arabic('MDCCLXXVIII')
        self.assertEqual(1778, res)

    def test_MDCCLXXIX(self):
        res = convert_to_arabic('MDCCLXXIX')
        self.assertEqual(1779, res)

    def test_MDCCLXXX(self):
        res = convert_to_arabic('MDCCLXXX')
        self.assertEqual(1780, res)

    def test_MDCCLXXXI(self):
        res = convert_to_arabic('MDCCLXXXI')
        self.assertEqual(1781, res)

    def test_MDCCLXXXII(self):
        res = convert_to_arabic('MDCCLXXXII')
        self.assertEqual(1782, res)

    def test_MDCCLXXXIII(self):
        res = convert_to_arabic('MDCCLXXXIII')
        self.assertEqual(1783, res)

    def test_MDCCLXXXIV(self):
        res = convert_to_arabic('MDCCLXXXIV')
        self.assertEqual(1784, res)

    def test_MDCCLXXXV(self):
        res = convert_to_arabic('MDCCLXXXV')
        self.assertEqual(1785, res)

    def test_MDCCLXXXVI(self):
        res = convert_to_arabic('MDCCLXXXVI')
        self.assertEqual(1786, res)

    def test_MDCCLXXXVII(self):
        res = convert_to_arabic('MDCCLXXXVII')
        self.assertEqual(1787, res)

    def test_MDCCLXXXVIII(self):
        res = convert_to_arabic('MDCCLXXXVIII')
        self.assertEqual(1788, res)

    def test_MDCCLXXXIX(self):
        res = convert_to_arabic('MDCCLXXXIX')
        self.assertEqual(1789, res)

    def test_MDCCXC(self):
        res = convert_to_arabic('MDCCXC')
        self.assertEqual(1790, res)

    def test_MDCCXCI(self):
        res = convert_to_arabic('MDCCXCI')
        self.assertEqual(1791, res)

    def test_MDCCXCII(self):
        res = convert_to_arabic('MDCCXCII')
        self.assertEqual(1792, res)

    def test_MDCCXCIII(self):
        res = convert_to_arabic('MDCCXCIII')
        self.assertEqual(1793, res)

    def test_MDCCXCIV(self):
        res = convert_to_arabic('MDCCXCIV')
        self.assertEqual(1794, res)

    def test_MDCCXCV(self):
        res = convert_to_arabic('MDCCXCV')
        self.assertEqual(1795, res)

    def test_MDCCXCVI(self):
        res = convert_to_arabic('MDCCXCVI')
        self.assertEqual(1796, res)

    def test_MDCCXCVII(self):
        res = convert_to_arabic('MDCCXCVII')
        self.assertEqual(1797, res)

    def test_MDCCXCVIII(self):
        res = convert_to_arabic('MDCCXCVIII')
        self.assertEqual(1798, res)

    def test_MDCCXCIX(self):
        res = convert_to_arabic('MDCCXCIX')
        self.assertEqual(1799, res)

    def test_MDCCC(self):
        res = convert_to_arabic('MDCCC')
        self.assertEqual(1800, res)

    def test_MDCCCI(self):
        res = convert_to_arabic('MDCCCI')
        self.assertEqual(1801, res)

    def test_MDCCCII(self):
        res = convert_to_arabic('MDCCCII')
        self.assertEqual(1802, res)

    def test_MDCCCIII(self):
        res = convert_to_arabic('MDCCCIII')
        self.assertEqual(1803, res)

    def test_MDCCCIV(self):
        res = convert_to_arabic('MDCCCIV')
        self.assertEqual(1804, res)

    def test_MDCCCV(self):
        res = convert_to_arabic('MDCCCV')
        self.assertEqual(1805, res)

    def test_MDCCCVI(self):
        res = convert_to_arabic('MDCCCVI')
        self.assertEqual(1806, res)

    def test_MDCCCVII(self):
        res = convert_to_arabic('MDCCCVII')
        self.assertEqual(1807, res)

    def test_MDCCCVIII(self):
        res = convert_to_arabic('MDCCCVIII')
        self.assertEqual(1808, res)

    def test_MDCCCIX(self):
        res = convert_to_arabic('MDCCCIX')
        self.assertEqual(1809, res)

    def test_MDCCCX(self):
        res = convert_to_arabic('MDCCCX')
        self.assertEqual(1810, res)

    def test_MDCCCXI(self):
        res = convert_to_arabic('MDCCCXI')
        self.assertEqual(1811, res)

    def test_MDCCCXII(self):
        res = convert_to_arabic('MDCCCXII')
        self.assertEqual(1812, res)

    def test_MDCCCXIII(self):
        res = convert_to_arabic('MDCCCXIII')
        self.assertEqual(1813, res)

    def test_MDCCCXIV(self):
        res = convert_to_arabic('MDCCCXIV')
        self.assertEqual(1814, res)

    def test_MDCCCXV(self):
        res = convert_to_arabic('MDCCCXV')
        self.assertEqual(1815, res)

    def test_MDCCCXVI(self):
        res = convert_to_arabic('MDCCCXVI')
        self.assertEqual(1816, res)

    def test_MDCCCXVII(self):
        res = convert_to_arabic('MDCCCXVII')
        self.assertEqual(1817, res)

    def test_MDCCCXVIII(self):
        res = convert_to_arabic('MDCCCXVIII')
        self.assertEqual(1818, res)

    def test_MDCCCXIX(self):
        res = convert_to_arabic('MDCCCXIX')
        self.assertEqual(1819, res)

    def test_MDCCCXX(self):
        res = convert_to_arabic('MDCCCXX')
        self.assertEqual(1820, res)

    def test_MDCCCXXI(self):
        res = convert_to_arabic('MDCCCXXI')
        self.assertEqual(1821, res)

    def test_MDCCCXXII(self):
        res = convert_to_arabic('MDCCCXXII')
        self.assertEqual(1822, res)

    def test_MDCCCXXIII(self):
        res = convert_to_arabic('MDCCCXXIII')
        self.assertEqual(1823, res)

    def test_MDCCCXXIV(self):
        res = convert_to_arabic('MDCCCXXIV')
        self.assertEqual(1824, res)

    def test_MDCCCXXV(self):
        res = convert_to_arabic('MDCCCXXV')
        self.assertEqual(1825, res)

    def test_MDCCCXXVI(self):
        res = convert_to_arabic('MDCCCXXVI')
        self.assertEqual(1826, res)

    def test_MDCCCXXVII(self):
        res = convert_to_arabic('MDCCCXXVII')
        self.assertEqual(1827, res)

    def test_MDCCCXXVIII(self):
        res = convert_to_arabic('MDCCCXXVIII')
        self.assertEqual(1828, res)

    def test_MDCCCXXIX(self):
        res = convert_to_arabic('MDCCCXXIX')
        self.assertEqual(1829, res)

    def test_MDCCCXXX(self):
        res = convert_to_arabic('MDCCCXXX')
        self.assertEqual(1830, res)

    def test_MDCCCXXXI(self):
        res = convert_to_arabic('MDCCCXXXI')
        self.assertEqual(1831, res)

    def test_MDCCCXXXII(self):
        res = convert_to_arabic('MDCCCXXXII')
        self.assertEqual(1832, res)

    def test_MDCCCXXXIII(self):
        res = convert_to_arabic('MDCCCXXXIII')
        self.assertEqual(1833, res)

    def test_MDCCCXXXIV(self):
        res = convert_to_arabic('MDCCCXXXIV')
        self.assertEqual(1834, res)

    def test_MDCCCXXXV(self):
        res = convert_to_arabic('MDCCCXXXV')
        self.assertEqual(1835, res)

    def test_MDCCCXXXVI(self):
        res = convert_to_arabic('MDCCCXXXVI')
        self.assertEqual(1836, res)

    def test_MDCCCXXXVII(self):
        res = convert_to_arabic('MDCCCXXXVII')
        self.assertEqual(1837, res)

    def test_MDCCCXXXVIII(self):
        res = convert_to_arabic('MDCCCXXXVIII')
        self.assertEqual(1838, res)

    def test_MDCCCXXXIX(self):
        res = convert_to_arabic('MDCCCXXXIX')
        self.assertEqual(1839, res)

    def test_MDCCCXL(self):
        res = convert_to_arabic('MDCCCXL')
        self.assertEqual(1840, res)

    def test_MDCCCXLI(self):
        res = convert_to_arabic('MDCCCXLI')
        self.assertEqual(1841, res)

    def test_MDCCCXLII(self):
        res = convert_to_arabic('MDCCCXLII')
        self.assertEqual(1842, res)

    def test_MDCCCXLIII(self):
        res = convert_to_arabic('MDCCCXLIII')
        self.assertEqual(1843, res)

    def test_MDCCCXLIV(self):
        res = convert_to_arabic('MDCCCXLIV')
        self.assertEqual(1844, res)

    def test_MDCCCXLV(self):
        res = convert_to_arabic('MDCCCXLV')
        self.assertEqual(1845, res)

    def test_MDCCCXLVI(self):
        res = convert_to_arabic('MDCCCXLVI')
        self.assertEqual(1846, res)

    def test_MDCCCXLVII(self):
        res = convert_to_arabic('MDCCCXLVII')
        self.assertEqual(1847, res)

    def test_MDCCCXLVIII(self):
        res = convert_to_arabic('MDCCCXLVIII')
        self.assertEqual(1848, res)

    def test_MDCCCXLIX(self):
        res = convert_to_arabic('MDCCCXLIX')
        self.assertEqual(1849, res)

    def test_MDCCCL(self):
        res = convert_to_arabic('MDCCCL')
        self.assertEqual(1850, res)

    def test_MDCCCLI(self):
        res = convert_to_arabic('MDCCCLI')
        self.assertEqual(1851, res)

    def test_MDCCCLII(self):
        res = convert_to_arabic('MDCCCLII')
        self.assertEqual(1852, res)

    def test_MDCCCLIII(self):
        res = convert_to_arabic('MDCCCLIII')
        self.assertEqual(1853, res)

    def test_MDCCCLIV(self):
        res = convert_to_arabic('MDCCCLIV')
        self.assertEqual(1854, res)

    def test_MDCCCLV(self):
        res = convert_to_arabic('MDCCCLV')
        self.assertEqual(1855, res)

    def test_MDCCCLVI(self):
        res = convert_to_arabic('MDCCCLVI')
        self.assertEqual(1856, res)

    def test_MDCCCLVII(self):
        res = convert_to_arabic('MDCCCLVII')
        self.assertEqual(1857, res)

    def test_MDCCCLVIII(self):
        res = convert_to_arabic('MDCCCLVIII')
        self.assertEqual(1858, res)

    def test_MDCCCLIX(self):
        res = convert_to_arabic('MDCCCLIX')
        self.assertEqual(1859, res)

    def test_MDCCCLX(self):
        res = convert_to_arabic('MDCCCLX')
        self.assertEqual(1860, res)

    def test_MDCCCLXI(self):
        res = convert_to_arabic('MDCCCLXI')
        self.assertEqual(1861, res)

    def test_MDCCCLXII(self):
        res = convert_to_arabic('MDCCCLXII')
        self.assertEqual(1862, res)

    def test_MDCCCLXIII(self):
        res = convert_to_arabic('MDCCCLXIII')
        self.assertEqual(1863, res)

    def test_MDCCCLXIV(self):
        res = convert_to_arabic('MDCCCLXIV')
        self.assertEqual(1864, res)

    def test_MDCCCLXV(self):
        res = convert_to_arabic('MDCCCLXV')
        self.assertEqual(1865, res)

    def test_MDCCCLXVI(self):
        res = convert_to_arabic('MDCCCLXVI')
        self.assertEqual(1866, res)

    def test_MDCCCLXVII(self):
        res = convert_to_arabic('MDCCCLXVII')
        self.assertEqual(1867, res)

    def test_MDCCCLXVIII(self):
        res = convert_to_arabic('MDCCCLXVIII')
        self.assertEqual(1868, res)

    def test_MDCCCLXIX(self):
        res = convert_to_arabic('MDCCCLXIX')
        self.assertEqual(1869, res)

    def test_MDCCCLXX(self):
        res = convert_to_arabic('MDCCCLXX')
        self.assertEqual(1870, res)

    def test_MDCCCLXXI(self):
        res = convert_to_arabic('MDCCCLXXI')
        self.assertEqual(1871, res)

    def test_MDCCCLXXII(self):
        res = convert_to_arabic('MDCCCLXXII')
        self.assertEqual(1872, res)

    def test_MDCCCLXXIII(self):
        res = convert_to_arabic('MDCCCLXXIII')
        self.assertEqual(1873, res)

    def test_MDCCCLXXIV(self):
        res = convert_to_arabic('MDCCCLXXIV')
        self.assertEqual(1874, res)

    def test_MDCCCLXXV(self):
        res = convert_to_arabic('MDCCCLXXV')
        self.assertEqual(1875, res)

    def test_MDCCCLXXVI(self):
        res = convert_to_arabic('MDCCCLXXVI')
        self.assertEqual(1876, res)

    def test_MDCCCLXXVII(self):
        res = convert_to_arabic('MDCCCLXXVII')
        self.assertEqual(1877, res)

    def test_MDCCCLXXVIII(self):
        res = convert_to_arabic('MDCCCLXXVIII')
        self.assertEqual(1878, res)

    def test_MDCCCLXXIX(self):
        res = convert_to_arabic('MDCCCLXXIX')
        self.assertEqual(1879, res)

    def test_MDCCCLXXX(self):
        res = convert_to_arabic('MDCCCLXXX')
        self.assertEqual(1880, res)

    def test_MDCCCLXXXI(self):
        res = convert_to_arabic('MDCCCLXXXI')
        self.assertEqual(1881, res)

    def test_MDCCCLXXXII(self):
        res = convert_to_arabic('MDCCCLXXXII')
        self.assertEqual(1882, res)

    def test_MDCCCLXXXIII(self):
        res = convert_to_arabic('MDCCCLXXXIII')
        self.assertEqual(1883, res)

    def test_MDCCCLXXXIV(self):
        res = convert_to_arabic('MDCCCLXXXIV')
        self.assertEqual(1884, res)

    def test_MDCCCLXXXV(self):
        res = convert_to_arabic('MDCCCLXXXV')
        self.assertEqual(1885, res)

    def test_MDCCCLXXXVI(self):
        res = convert_to_arabic('MDCCCLXXXVI')
        self.assertEqual(1886, res)

    def test_MDCCCLXXXVII(self):
        res = convert_to_arabic('MDCCCLXXXVII')
        self.assertEqual(1887, res)

    def test_MDCCCLXXXVIII(self):
        res = convert_to_arabic('MDCCCLXXXVIII')
        self.assertEqual(1888, res)

    def test_MDCCCLXXXIX(self):
        res = convert_to_arabic('MDCCCLXXXIX')
        self.assertEqual(1889, res)

    def test_MDCCCXC(self):
        res = convert_to_arabic('MDCCCXC')
        self.assertEqual(1890, res)

    def test_MDCCCXCI(self):
        res = convert_to_arabic('MDCCCXCI')
        self.assertEqual(1891, res)

    def test_MDCCCXCII(self):
        res = convert_to_arabic('MDCCCXCII')
        self.assertEqual(1892, res)

    def test_MDCCCXCIII(self):
        res = convert_to_arabic('MDCCCXCIII')
        self.assertEqual(1893, res)

    def test_MDCCCXCIV(self):
        res = convert_to_arabic('MDCCCXCIV')
        self.assertEqual(1894, res)

    def test_MDCCCXCV(self):
        res = convert_to_arabic('MDCCCXCV')
        self.assertEqual(1895, res)

    def test_MDCCCXCVI(self):
        res = convert_to_arabic('MDCCCXCVI')
        self.assertEqual(1896, res)

    def test_MDCCCXCVII(self):
        res = convert_to_arabic('MDCCCXCVII')
        self.assertEqual(1897, res)

    def test_MDCCCXCVIII(self):
        res = convert_to_arabic('MDCCCXCVIII')
        self.assertEqual(1898, res)

    def test_MDCCCXCIX(self):
        res = convert_to_arabic('MDCCCXCIX')
        self.assertEqual(1899, res)

    def test_MCM(self):
        res = convert_to_arabic('MCM')
        self.assertEqual(1900, res)

    def test_MCMI(self):
        res = convert_to_arabic('MCMI')
        self.assertEqual(1901, res)

    def test_MCMII(self):
        res = convert_to_arabic('MCMII')
        self.assertEqual(1902, res)

    def test_MCMIII(self):
        res = convert_to_arabic('MCMIII')
        self.assertEqual(1903, res)

    def test_MCMIV(self):
        res = convert_to_arabic('MCMIV')
        self.assertEqual(1904, res)

    def test_MCMV(self):
        res = convert_to_arabic('MCMV')
        self.assertEqual(1905, res)

    def test_MCMVI(self):
        res = convert_to_arabic('MCMVI')
        self.assertEqual(1906, res)

    def test_MCMVII(self):
        res = convert_to_arabic('MCMVII')
        self.assertEqual(1907, res)

    def test_MCMVIII(self):
        res = convert_to_arabic('MCMVIII')
        self.assertEqual(1908, res)

    def test_MCMIX(self):
        res = convert_to_arabic('MCMIX')
        self.assertEqual(1909, res)

    def test_MCMX(self):
        res = convert_to_arabic('MCMX')
        self.assertEqual(1910, res)

    def test_MCMXI(self):
        res = convert_to_arabic('MCMXI')
        self.assertEqual(1911, res)

    def test_MCMXII(self):
        res = convert_to_arabic('MCMXII')
        self.assertEqual(1912, res)

    def test_MCMXIII(self):
        res = convert_to_arabic('MCMXIII')
        self.assertEqual(1913, res)

    def test_MCMXIV(self):
        res = convert_to_arabic('MCMXIV')
        self.assertEqual(1914, res)

    def test_MCMXV(self):
        res = convert_to_arabic('MCMXV')
        self.assertEqual(1915, res)

    def test_MCMXVI(self):
        res = convert_to_arabic('MCMXVI')
        self.assertEqual(1916, res)

    def test_MCMXVII(self):
        res = convert_to_arabic('MCMXVII')
        self.assertEqual(1917, res)

    def test_MCMXVIII(self):
        res = convert_to_arabic('MCMXVIII')
        self.assertEqual(1918, res)

    def test_MCMXIX(self):
        res = convert_to_arabic('MCMXIX')
        self.assertEqual(1919, res)

    def test_MCMXX(self):
        res = convert_to_arabic('MCMXX')
        self.assertEqual(1920, res)

    def test_MCMXXI(self):
        res = convert_to_arabic('MCMXXI')
        self.assertEqual(1921, res)

    def test_MCMXXII(self):
        res = convert_to_arabic('MCMXXII')
        self.assertEqual(1922, res)

    def test_MCMXXIII(self):
        res = convert_to_arabic('MCMXXIII')
        self.assertEqual(1923, res)

    def test_MCMXXIV(self):
        res = convert_to_arabic('MCMXXIV')
        self.assertEqual(1924, res)

    def test_MCMXXV(self):
        res = convert_to_arabic('MCMXXV')
        self.assertEqual(1925, res)

    def test_MCMXXVI(self):
        res = convert_to_arabic('MCMXXVI')
        self.assertEqual(1926, res)

    def test_MCMXXVII(self):
        res = convert_to_arabic('MCMXXVII')
        self.assertEqual(1927, res)

    def test_MCMXXVIII(self):
        res = convert_to_arabic('MCMXXVIII')
        self.assertEqual(1928, res)

    def test_MCMXXIX(self):
        res = convert_to_arabic('MCMXXIX')
        self.assertEqual(1929, res)

    def test_MCMXXX(self):
        res = convert_to_arabic('MCMXXX')
        self.assertEqual(1930, res)

    def test_MCMXXXI(self):
        res = convert_to_arabic('MCMXXXI')
        self.assertEqual(1931, res)

    def test_MCMXXXII(self):
        res = convert_to_arabic('MCMXXXII')
        self.assertEqual(1932, res)

    def test_MCMXXXIII(self):
        res = convert_to_arabic('MCMXXXIII')
        self.assertEqual(1933, res)

    def test_MCMXXXIV(self):
        res = convert_to_arabic('MCMXXXIV')
        self.assertEqual(1934, res)

    def test_MCMXXXV(self):
        res = convert_to_arabic('MCMXXXV')
        self.assertEqual(1935, res)

    def test_MCMXXXVI(self):
        res = convert_to_arabic('MCMXXXVI')
        self.assertEqual(1936, res)

    def test_MCMXXXVII(self):
        res = convert_to_arabic('MCMXXXVII')
        self.assertEqual(1937, res)

    def test_MCMXXXVIII(self):
        res = convert_to_arabic('MCMXXXVIII')
        self.assertEqual(1938, res)

    def test_MCMXXXIX(self):
        res = convert_to_arabic('MCMXXXIX')
        self.assertEqual(1939, res)

    def test_MCMXL(self):
        res = convert_to_arabic('MCMXL')
        self.assertEqual(1940, res)

    def test_MCMXLI(self):
        res = convert_to_arabic('MCMXLI')
        self.assertEqual(1941, res)

    def test_MCMXLII(self):
        res = convert_to_arabic('MCMXLII')
        self.assertEqual(1942, res)

    def test_MCMXLIII(self):
        res = convert_to_arabic('MCMXLIII')
        self.assertEqual(1943, res)

    def test_MCMXLIV(self):
        res = convert_to_arabic('MCMXLIV')
        self.assertEqual(1944, res)

    def test_MCMXLV(self):
        res = convert_to_arabic('MCMXLV')
        self.assertEqual(1945, res)

    def test_MCMXLVI(self):
        res = convert_to_arabic('MCMXLVI')
        self.assertEqual(1946, res)

    def test_MCMXLVII(self):
        res = convert_to_arabic('MCMXLVII')
        self.assertEqual(1947, res)

    def test_MCMXLVIII(self):
        res = convert_to_arabic('MCMXLVIII')
        self.assertEqual(1948, res)

    def test_MCMXLIX(self):
        res = convert_to_arabic('MCMXLIX')
        self.assertEqual(1949, res)

    def test_MCML(self):
        res = convert_to_arabic('MCML')
        self.assertEqual(1950, res)

    def test_MCMLI(self):
        res = convert_to_arabic('MCMLI')
        self.assertEqual(1951, res)

    def test_MCMLII(self):
        res = convert_to_arabic('MCMLII')
        self.assertEqual(1952, res)

    def test_MCMLIII(self):
        res = convert_to_arabic('MCMLIII')
        self.assertEqual(1953, res)

    def test_MCMLIV(self):
        res = convert_to_arabic('MCMLIV')
        self.assertEqual(1954, res)

    def test_MCMLV(self):
        res = convert_to_arabic('MCMLV')
        self.assertEqual(1955, res)

    def test_MCMLVI(self):
        res = convert_to_arabic('MCMLVI')
        self.assertEqual(1956, res)

    def test_MCMLVII(self):
        res = convert_to_arabic('MCMLVII')
        self.assertEqual(1957, res)

    def test_MCMLVIII(self):
        res = convert_to_arabic('MCMLVIII')
        self.assertEqual(1958, res)

    def test_MCMLIX(self):
        res = convert_to_arabic('MCMLIX')
        self.assertEqual(1959, res)

    def test_MCMLX(self):
        res = convert_to_arabic('MCMLX')
        self.assertEqual(1960, res)

    def test_MCMLXI(self):
        res = convert_to_arabic('MCMLXI')
        self.assertEqual(1961, res)

    def test_MCMLXII(self):
        res = convert_to_arabic('MCMLXII')
        self.assertEqual(1962, res)

    def test_MCMLXIII(self):
        res = convert_to_arabic('MCMLXIII')
        self.assertEqual(1963, res)

    def test_MCMLXIV(self):
        res = convert_to_arabic('MCMLXIV')
        self.assertEqual(1964, res)

    def test_MCMLXV(self):
        res = convert_to_arabic('MCMLXV')
        self.assertEqual(1965, res)

    def test_MCMLXVI(self):
        res = convert_to_arabic('MCMLXVI')
        self.assertEqual(1966, res)

    def test_MCMLXVII(self):
        res = convert_to_arabic('MCMLXVII')
        self.assertEqual(1967, res)

    def test_MCMLXVIII(self):
        res = convert_to_arabic('MCMLXVIII')
        self.assertEqual(1968, res)

    def test_MCMLXIX(self):
        res = convert_to_arabic('MCMLXIX')
        self.assertEqual(1969, res)

    def test_MCMLXX(self):
        res = convert_to_arabic('MCMLXX')
        self.assertEqual(1970, res)

    def test_MCMLXXI(self):
        res = convert_to_arabic('MCMLXXI')
        self.assertEqual(1971, res)

    def test_MCMLXXII(self):
        res = convert_to_arabic('MCMLXXII')
        self.assertEqual(1972, res)

    def test_MCMLXXIII(self):
        res = convert_to_arabic('MCMLXXIII')
        self.assertEqual(1973, res)

    def test_MCMLXXIV(self):
        res = convert_to_arabic('MCMLXXIV')
        self.assertEqual(1974, res)

    def test_MCMLXXV(self):
        res = convert_to_arabic('MCMLXXV')
        self.assertEqual(1975, res)

    def test_MCMLXXVI(self):
        res = convert_to_arabic('MCMLXXVI')
        self.assertEqual(1976, res)

    def test_MCMLXXVII(self):
        res = convert_to_arabic('MCMLXXVII')
        self.assertEqual(1977, res)

    def test_MCMLXXVIII(self):
        res = convert_to_arabic('MCMLXXVIII')
        self.assertEqual(1978, res)

    def test_MCMLXXIX(self):
        res = convert_to_arabic('MCMLXXIX')
        self.assertEqual(1979, res)

    def test_MCMLXXX(self):
        res = convert_to_arabic('MCMLXXX')
        self.assertEqual(1980, res)

    def test_MCMLXXXI(self):
        res = convert_to_arabic('MCMLXXXI')
        self.assertEqual(1981, res)

    def test_MCMLXXXII(self):
        res = convert_to_arabic('MCMLXXXII')
        self.assertEqual(1982, res)

    def test_MCMLXXXIII(self):
        res = convert_to_arabic('MCMLXXXIII')
        self.assertEqual(1983, res)

    def test_MCMLXXXIV(self):
        res = convert_to_arabic('MCMLXXXIV')
        self.assertEqual(1984, res)

    def test_MCMLXXXV(self):
        res = convert_to_arabic('MCMLXXXV')
        self.assertEqual(1985, res)

    def test_MCMLXXXVI(self):
        res = convert_to_arabic('MCMLXXXVI')
        self.assertEqual(1986, res)

    def test_MCMLXXXVII(self):
        res = convert_to_arabic('MCMLXXXVII')
        self.assertEqual(1987, res)

    def test_MCMLXXXVIII(self):
        res = convert_to_arabic('MCMLXXXVIII')
        self.assertEqual(1988, res)

    def test_MCMLXXXIX(self):
        res = convert_to_arabic('MCMLXXXIX')
        self.assertEqual(1989, res)

    def test_MCMXC(self):
        res = convert_to_arabic('MCMXC')
        self.assertEqual(1990, res)

    def test_MCMXCI(self):
        res = convert_to_arabic('MCMXCI')
        self.assertEqual(1991, res)

    def test_MCMXCII(self):
        res = convert_to_arabic('MCMXCII')
        self.assertEqual(1992, res)

    def test_MCMXCIII(self):
        res = convert_to_arabic('MCMXCIII')
        self.assertEqual(1993, res)

    def test_MCMXCIV(self):
        res = convert_to_arabic('MCMXCIV')
        self.assertEqual(1994, res)

    def test_MCMXCV(self):
        res = convert_to_arabic('MCMXCV')
        self.assertEqual(1995, res)

    def test_MCMXCVI(self):
        res = convert_to_arabic('MCMXCVI')
        self.assertEqual(1996, res)

    def test_MCMXCVII(self):
        res = convert_to_arabic('MCMXCVII')
        self.assertEqual(1997, res)

    def test_MCMXCVIII(self):
        res = convert_to_arabic('MCMXCVIII')
        self.assertEqual(1998, res)

    def test_MCMXCIX(self):
        res = convert_to_arabic('MCMXCIX')
        self.assertEqual(1999, res)

    def test_MM(self):
        res = convert_to_arabic('MM')
        self.assertEqual(2000, res)

    def test_MMI(self):
        res = convert_to_arabic('MMI')
        self.assertEqual(2001, res)

    def test_MMII(self):
        res = convert_to_arabic('MMII')
        self.assertEqual(2002, res)

    def test_MMIII(self):
        res = convert_to_arabic('MMIII')
        self.assertEqual(2003, res)

    def test_MMIV(self):
        res = convert_to_arabic('MMIV')
        self.assertEqual(2004, res)

    def test_MMV(self):
        res = convert_to_arabic('MMV')
        self.assertEqual(2005, res)

    def test_MMVI(self):
        res = convert_to_arabic('MMVI')
        self.assertEqual(2006, res)

    def test_MMVII(self):
        res = convert_to_arabic('MMVII')
        self.assertEqual(2007, res)

    def test_MMVIII(self):
        res = convert_to_arabic('MMVIII')
        self.assertEqual(2008, res)

    def test_MMIX(self):
        res = convert_to_arabic('MMIX')
        self.assertEqual(2009, res)

    def test_MMX(self):
        res = convert_to_arabic('MMX')
        self.assertEqual(2010, res)

    def test_MMXI(self):
        res = convert_to_arabic('MMXI')
        self.assertEqual(2011, res)

    def test_MMXII(self):
        res = convert_to_arabic('MMXII')
        self.assertEqual(2012, res)

    def test_MMXIII(self):
        res = convert_to_arabic('MMXIII')
        self.assertEqual(2013, res)

    def test_MMXIV(self):
        res = convert_to_arabic('MMXIV')
        self.assertEqual(2014, res)

    def test_MMXV(self):
        res = convert_to_arabic('MMXV')
        self.assertEqual(2015, res)

    def test_MMXVI(self):
        res = convert_to_arabic('MMXVI')
        self.assertEqual(2016, res)

    def test_MMXVII(self):
        res = convert_to_arabic('MMXVII')
        self.assertEqual(2017, res)

    def test_MMXVIII(self):
        res = convert_to_arabic('MMXVIII')
        self.assertEqual(2018, res)

    def test_MMXIX(self):
        res = convert_to_arabic('MMXIX')
        self.assertEqual(2019, res)

    def test_MMXX(self):
        res = convert_to_arabic('MMXX')
        self.assertEqual(2020, res)

    def test_MMXXI(self):
        res = convert_to_arabic('MMXXI')
        self.assertEqual(2021, res)

    def test_MMXXII(self):
        res = convert_to_arabic('MMXXII')
        self.assertEqual(2022, res)

    def test_MMXXIII(self):
        res = convert_to_arabic('MMXXIII')
        self.assertEqual(2023, res)

    def test_MMXXIV(self):
        res = convert_to_arabic('MMXXIV')
        self.assertEqual(2024, res)

    def test_MMXXV(self):
        res = convert_to_arabic('MMXXV')
        self.assertEqual(2025, res)

    def test_MMXXVI(self):
        res = convert_to_arabic('MMXXVI')
        self.assertEqual(2026, res)

    def test_MMXXVII(self):
        res = convert_to_arabic('MMXXVII')
        self.assertEqual(2027, res)

    def test_MMXXVIII(self):
        res = convert_to_arabic('MMXXVIII')
        self.assertEqual(2028, res)

    def test_MMXXIX(self):
        res = convert_to_arabic('MMXXIX')
        self.assertEqual(2029, res)

    def test_MMXXX(self):
        res = convert_to_arabic('MMXXX')
        self.assertEqual(2030, res)

    def test_MMXXXI(self):
        res = convert_to_arabic('MMXXXI')
        self.assertEqual(2031, res)

    def test_MMXXXII(self):
        res = convert_to_arabic('MMXXXII')
        self.assertEqual(2032, res)

    def test_MMXXXIII(self):
        res = convert_to_arabic('MMXXXIII')
        self.assertEqual(2033, res)

    def test_MMXXXIV(self):
        res = convert_to_arabic('MMXXXIV')
        self.assertEqual(2034, res)

    def test_MMXXXV(self):
        res = convert_to_arabic('MMXXXV')
        self.assertEqual(2035, res)

    def test_MMXXXVI(self):
        res = convert_to_arabic('MMXXXVI')
        self.assertEqual(2036, res)

    def test_MMXXXVII(self):
        res = convert_to_arabic('MMXXXVII')
        self.assertEqual(2037, res)

    def test_MMXXXVIII(self):
        res = convert_to_arabic('MMXXXVIII')
        self.assertEqual(2038, res)

    def test_MMXXXIX(self):
        res = convert_to_arabic('MMXXXIX')
        self.assertEqual(2039, res)

    def test_MMXL(self):
        res = convert_to_arabic('MMXL')
        self.assertEqual(2040, res)

    def test_MMXLI(self):
        res = convert_to_arabic('MMXLI')
        self.assertEqual(2041, res)

    def test_MMXLII(self):
        res = convert_to_arabic('MMXLII')
        self.assertEqual(2042, res)

    def test_MMXLIII(self):
        res = convert_to_arabic('MMXLIII')
        self.assertEqual(2043, res)

    def test_MMXLIV(self):
        res = convert_to_arabic('MMXLIV')
        self.assertEqual(2044, res)

    def test_MMXLV(self):
        res = convert_to_arabic('MMXLV')
        self.assertEqual(2045, res)

    def test_MMXLVI(self):
        res = convert_to_arabic('MMXLVI')
        self.assertEqual(2046, res)

    def test_MMXLVII(self):
        res = convert_to_arabic('MMXLVII')
        self.assertEqual(2047, res)

    def test_MMXLVIII(self):
        res = convert_to_arabic('MMXLVIII')
        self.assertEqual(2048, res)

    def test_MMXLIX(self):
        res = convert_to_arabic('MMXLIX')
        self.assertEqual(2049, res)

    def test_MML(self):
        res = convert_to_arabic('MML')
        self.assertEqual(2050, res)

    def test_MMLI(self):
        res = convert_to_arabic('MMLI')
        self.assertEqual(2051, res)

    def test_MMLII(self):
        res = convert_to_arabic('MMLII')
        self.assertEqual(2052, res)

    def test_MMLIII(self):
        res = convert_to_arabic('MMLIII')
        self.assertEqual(2053, res)

    def test_MMLIV(self):
        res = convert_to_arabic('MMLIV')
        self.assertEqual(2054, res)

    def test_MMLV(self):
        res = convert_to_arabic('MMLV')
        self.assertEqual(2055, res)

    def test_MMLVI(self):
        res = convert_to_arabic('MMLVI')
        self.assertEqual(2056, res)

    def test_MMLVII(self):
        res = convert_to_arabic('MMLVII')
        self.assertEqual(2057, res)

    def test_MMLVIII(self):
        res = convert_to_arabic('MMLVIII')
        self.assertEqual(2058, res)

    def test_MMLIX(self):
        res = convert_to_arabic('MMLIX')
        self.assertEqual(2059, res)

    def test_MMLX(self):
        res = convert_to_arabic('MMLX')
        self.assertEqual(2060, res)

    def test_MMLXI(self):
        res = convert_to_arabic('MMLXI')
        self.assertEqual(2061, res)

    def test_MMLXII(self):
        res = convert_to_arabic('MMLXII')
        self.assertEqual(2062, res)

    def test_MMLXIII(self):
        res = convert_to_arabic('MMLXIII')
        self.assertEqual(2063, res)

    def test_MMLXIV(self):
        res = convert_to_arabic('MMLXIV')
        self.assertEqual(2064, res)

    def test_MMLXV(self):
        res = convert_to_arabic('MMLXV')
        self.assertEqual(2065, res)

    def test_MMLXVI(self):
        res = convert_to_arabic('MMLXVI')
        self.assertEqual(2066, res)

    def test_MMLXVII(self):
        res = convert_to_arabic('MMLXVII')
        self.assertEqual(2067, res)

    def test_MMLXVIII(self):
        res = convert_to_arabic('MMLXVIII')
        self.assertEqual(2068, res)

    def test_MMLXIX(self):
        res = convert_to_arabic('MMLXIX')
        self.assertEqual(2069, res)

    def test_MMLXX(self):
        res = convert_to_arabic('MMLXX')
        self.assertEqual(2070, res)

    def test_MMLXXI(self):
        res = convert_to_arabic('MMLXXI')
        self.assertEqual(2071, res)

    def test_MMLXXII(self):
        res = convert_to_arabic('MMLXXII')
        self.assertEqual(2072, res)

    def test_MMLXXIII(self):
        res = convert_to_arabic('MMLXXIII')
        self.assertEqual(2073, res)

    def test_MMLXXIV(self):
        res = convert_to_arabic('MMLXXIV')
        self.assertEqual(2074, res)

    def test_MMLXXV(self):
        res = convert_to_arabic('MMLXXV')
        self.assertEqual(2075, res)

    def test_MMLXXVI(self):
        res = convert_to_arabic('MMLXXVI')
        self.assertEqual(2076, res)

    def test_MMLXXVII(self):
        res = convert_to_arabic('MMLXXVII')
        self.assertEqual(2077, res)

    def test_MMLXXVIII(self):
        res = convert_to_arabic('MMLXXVIII')
        self.assertEqual(2078, res)

    def test_MMLXXIX(self):
        res = convert_to_arabic('MMLXXIX')
        self.assertEqual(2079, res)

    def test_MMLXXX(self):
        res = convert_to_arabic('MMLXXX')
        self.assertEqual(2080, res)

    def test_MMLXXXI(self):
        res = convert_to_arabic('MMLXXXI')
        self.assertEqual(2081, res)

    def test_MMLXXXII(self):
        res = convert_to_arabic('MMLXXXII')
        self.assertEqual(2082, res)

    def test_MMLXXXIII(self):
        res = convert_to_arabic('MMLXXXIII')
        self.assertEqual(2083, res)

    def test_MMLXXXIV(self):
        res = convert_to_arabic('MMLXXXIV')
        self.assertEqual(2084, res)

    def test_MMLXXXV(self):
        res = convert_to_arabic('MMLXXXV')
        self.assertEqual(2085, res)

    def test_MMLXXXVI(self):
        res = convert_to_arabic('MMLXXXVI')
        self.assertEqual(2086, res)

    def test_MMLXXXVII(self):
        res = convert_to_arabic('MMLXXXVII')
        self.assertEqual(2087, res)

    def test_MMLXXXVIII(self):
        res = convert_to_arabic('MMLXXXVIII')
        self.assertEqual(2088, res)

    def test_MMLXXXIX(self):
        res = convert_to_arabic('MMLXXXIX')
        self.assertEqual(2089, res)

    def test_MMXC(self):
        res = convert_to_arabic('MMXC')
        self.assertEqual(2090, res)

    def test_MMXCI(self):
        res = convert_to_arabic('MMXCI')
        self.assertEqual(2091, res)

    def test_MMXCII(self):
        res = convert_to_arabic('MMXCII')
        self.assertEqual(2092, res)

    def test_MMXCIII(self):
        res = convert_to_arabic('MMXCIII')
        self.assertEqual(2093, res)

    def test_MMXCIV(self):
        res = convert_to_arabic('MMXCIV')
        self.assertEqual(2094, res)

    def test_MMXCV(self):
        res = convert_to_arabic('MMXCV')
        self.assertEqual(2095, res)

    def test_MMXCVI(self):
        res = convert_to_arabic('MMXCVI')
        self.assertEqual(2096, res)

    def test_MMXCVII(self):
        res = convert_to_arabic('MMXCVII')
        self.assertEqual(2097, res)

    def test_MMXCVIII(self):
        res = convert_to_arabic('MMXCVIII')
        self.assertEqual(2098, res)

    def test_MMXCIX(self):
        res = convert_to_arabic('MMXCIX')
        self.assertEqual(2099, res)

    def test_MMC(self):
        res = convert_to_arabic('MMC')
        self.assertEqual(2100, res)

    def test_MMCI(self):
        res = convert_to_arabic('MMCI')
        self.assertEqual(2101, res)

    def test_MMCII(self):
        res = convert_to_arabic('MMCII')
        self.assertEqual(2102, res)

    def test_MMCIII(self):
        res = convert_to_arabic('MMCIII')
        self.assertEqual(2103, res)

    def test_MMCIV(self):
        res = convert_to_arabic('MMCIV')
        self.assertEqual(2104, res)

    def test_MMCV(self):
        res = convert_to_arabic('MMCV')
        self.assertEqual(2105, res)

    def test_MMCVI(self):
        res = convert_to_arabic('MMCVI')
        self.assertEqual(2106, res)

    def test_MMCVII(self):
        res = convert_to_arabic('MMCVII')
        self.assertEqual(2107, res)

    def test_MMCVIII(self):
        res = convert_to_arabic('MMCVIII')
        self.assertEqual(2108, res)

    def test_MMCIX(self):
        res = convert_to_arabic('MMCIX')
        self.assertEqual(2109, res)

    def test_MMCX(self):
        res = convert_to_arabic('MMCX')
        self.assertEqual(2110, res)

    def test_MMCXI(self):
        res = convert_to_arabic('MMCXI')
        self.assertEqual(2111, res)

    def test_MMCXII(self):
        res = convert_to_arabic('MMCXII')
        self.assertEqual(2112, res)

    def test_MMCXIII(self):
        res = convert_to_arabic('MMCXIII')
        self.assertEqual(2113, res)

    def test_MMCXIV(self):
        res = convert_to_arabic('MMCXIV')
        self.assertEqual(2114, res)

    def test_MMCXV(self):
        res = convert_to_arabic('MMCXV')
        self.assertEqual(2115, res)

    def test_MMCXVI(self):
        res = convert_to_arabic('MMCXVI')
        self.assertEqual(2116, res)

    def test_MMCXVII(self):
        res = convert_to_arabic('MMCXVII')
        self.assertEqual(2117, res)

    def test_MMCXVIII(self):
        res = convert_to_arabic('MMCXVIII')
        self.assertEqual(2118, res)

    def test_MMCXIX(self):
        res = convert_to_arabic('MMCXIX')
        self.assertEqual(2119, res)

    def test_MMCXX(self):
        res = convert_to_arabic('MMCXX')
        self.assertEqual(2120, res)

    def test_MMCXXI(self):
        res = convert_to_arabic('MMCXXI')
        self.assertEqual(2121, res)

    def test_MMCXXII(self):
        res = convert_to_arabic('MMCXXII')
        self.assertEqual(2122, res)

    def test_MMCXXIII(self):
        res = convert_to_arabic('MMCXXIII')
        self.assertEqual(2123, res)

    def test_MMCXXIV(self):
        res = convert_to_arabic('MMCXXIV')
        self.assertEqual(2124, res)

    def test_MMCXXV(self):
        res = convert_to_arabic('MMCXXV')
        self.assertEqual(2125, res)

    def test_MMCXXVI(self):
        res = convert_to_arabic('MMCXXVI')
        self.assertEqual(2126, res)

    def test_MMCXXVII(self):
        res = convert_to_arabic('MMCXXVII')
        self.assertEqual(2127, res)

    def test_MMCXXVIII(self):
        res = convert_to_arabic('MMCXXVIII')
        self.assertEqual(2128, res)

    def test_MMCXXIX(self):
        res = convert_to_arabic('MMCXXIX')
        self.assertEqual(2129, res)

    def test_MMCXXX(self):
        res = convert_to_arabic('MMCXXX')
        self.assertEqual(2130, res)

    def test_MMCXXXI(self):
        res = convert_to_arabic('MMCXXXI')
        self.assertEqual(2131, res)

    def test_MMCXXXII(self):
        res = convert_to_arabic('MMCXXXII')
        self.assertEqual(2132, res)

    def test_MMCXXXIII(self):
        res = convert_to_arabic('MMCXXXIII')
        self.assertEqual(2133, res)

    def test_MMCXXXIV(self):
        res = convert_to_arabic('MMCXXXIV')
        self.assertEqual(2134, res)

    def test_MMCXXXV(self):
        res = convert_to_arabic('MMCXXXV')
        self.assertEqual(2135, res)

    def test_MMCXXXVI(self):
        res = convert_to_arabic('MMCXXXVI')
        self.assertEqual(2136, res)

    def test_MMCXXXVII(self):
        res = convert_to_arabic('MMCXXXVII')
        self.assertEqual(2137, res)

    def test_MMCXXXVIII(self):
        res = convert_to_arabic('MMCXXXVIII')
        self.assertEqual(2138, res)

    def test_MMCXXXIX(self):
        res = convert_to_arabic('MMCXXXIX')
        self.assertEqual(2139, res)

    def test_MMCXL(self):
        res = convert_to_arabic('MMCXL')
        self.assertEqual(2140, res)

    def test_MMCXLI(self):
        res = convert_to_arabic('MMCXLI')
        self.assertEqual(2141, res)

    def test_MMCXLII(self):
        res = convert_to_arabic('MMCXLII')
        self.assertEqual(2142, res)

    def test_MMCXLIII(self):
        res = convert_to_arabic('MMCXLIII')
        self.assertEqual(2143, res)

    def test_MMCXLIV(self):
        res = convert_to_arabic('MMCXLIV')
        self.assertEqual(2144, res)

    def test_MMCXLV(self):
        res = convert_to_arabic('MMCXLV')
        self.assertEqual(2145, res)

    def test_MMCXLVI(self):
        res = convert_to_arabic('MMCXLVI')
        self.assertEqual(2146, res)

    def test_MMCXLVII(self):
        res = convert_to_arabic('MMCXLVII')
        self.assertEqual(2147, res)

    def test_MMCXLVIII(self):
        res = convert_to_arabic('MMCXLVIII')
        self.assertEqual(2148, res)

    def test_MMCXLIX(self):
        res = convert_to_arabic('MMCXLIX')
        self.assertEqual(2149, res)

    def test_MMCL(self):
        res = convert_to_arabic('MMCL')
        self.assertEqual(2150, res)

    def test_MMCLI(self):
        res = convert_to_arabic('MMCLI')
        self.assertEqual(2151, res)

    def test_MMCLII(self):
        res = convert_to_arabic('MMCLII')
        self.assertEqual(2152, res)

    def test_MMCLIII(self):
        res = convert_to_arabic('MMCLIII')
        self.assertEqual(2153, res)

    def test_MMCLIV(self):
        res = convert_to_arabic('MMCLIV')
        self.assertEqual(2154, res)

    def test_MMCLV(self):
        res = convert_to_arabic('MMCLV')
        self.assertEqual(2155, res)

    def test_MMCLVI(self):
        res = convert_to_arabic('MMCLVI')
        self.assertEqual(2156, res)

    def test_MMCLVII(self):
        res = convert_to_arabic('MMCLVII')
        self.assertEqual(2157, res)

    def test_MMCLVIII(self):
        res = convert_to_arabic('MMCLVIII')
        self.assertEqual(2158, res)

    def test_MMCLIX(self):
        res = convert_to_arabic('MMCLIX')
        self.assertEqual(2159, res)

    def test_MMCLX(self):
        res = convert_to_arabic('MMCLX')
        self.assertEqual(2160, res)

    def test_MMCLXI(self):
        res = convert_to_arabic('MMCLXI')
        self.assertEqual(2161, res)

    def test_MMCLXII(self):
        res = convert_to_arabic('MMCLXII')
        self.assertEqual(2162, res)

    def test_MMCLXIII(self):
        res = convert_to_arabic('MMCLXIII')
        self.assertEqual(2163, res)

    def test_MMCLXIV(self):
        res = convert_to_arabic('MMCLXIV')
        self.assertEqual(2164, res)

    def test_MMCLXV(self):
        res = convert_to_arabic('MMCLXV')
        self.assertEqual(2165, res)

    def test_MMCLXVI(self):
        res = convert_to_arabic('MMCLXVI')
        self.assertEqual(2166, res)

    def test_MMCLXVII(self):
        res = convert_to_arabic('MMCLXVII')
        self.assertEqual(2167, res)

    def test_MMCLXVIII(self):
        res = convert_to_arabic('MMCLXVIII')
        self.assertEqual(2168, res)

    def test_MMCLXIX(self):
        res = convert_to_arabic('MMCLXIX')
        self.assertEqual(2169, res)

    def test_MMCLXX(self):
        res = convert_to_arabic('MMCLXX')
        self.assertEqual(2170, res)

    def test_MMCLXXI(self):
        res = convert_to_arabic('MMCLXXI')
        self.assertEqual(2171, res)

    def test_MMCLXXII(self):
        res = convert_to_arabic('MMCLXXII')
        self.assertEqual(2172, res)

    def test_MMCLXXIII(self):
        res = convert_to_arabic('MMCLXXIII')
        self.assertEqual(2173, res)

    def test_MMCLXXIV(self):
        res = convert_to_arabic('MMCLXXIV')
        self.assertEqual(2174, res)

    def test_MMCLXXV(self):
        res = convert_to_arabic('MMCLXXV')
        self.assertEqual(2175, res)

    def test_MMCLXXVI(self):
        res = convert_to_arabic('MMCLXXVI')
        self.assertEqual(2176, res)

    def test_MMCLXXVII(self):
        res = convert_to_arabic('MMCLXXVII')
        self.assertEqual(2177, res)

    def test_MMCLXXVIII(self):
        res = convert_to_arabic('MMCLXXVIII')
        self.assertEqual(2178, res)

    def test_MMCLXXIX(self):
        res = convert_to_arabic('MMCLXXIX')
        self.assertEqual(2179, res)

    def test_MMCLXXX(self):
        res = convert_to_arabic('MMCLXXX')
        self.assertEqual(2180, res)

    def test_MMCLXXXI(self):
        res = convert_to_arabic('MMCLXXXI')
        self.assertEqual(2181, res)

    def test_MMCLXXXII(self):
        res = convert_to_arabic('MMCLXXXII')
        self.assertEqual(2182, res)

    def test_MMCLXXXIII(self):
        res = convert_to_arabic('MMCLXXXIII')
        self.assertEqual(2183, res)

    def test_MMCLXXXIV(self):
        res = convert_to_arabic('MMCLXXXIV')
        self.assertEqual(2184, res)

    def test_MMCLXXXV(self):
        res = convert_to_arabic('MMCLXXXV')
        self.assertEqual(2185, res)

    def test_MMCLXXXVI(self):
        res = convert_to_arabic('MMCLXXXVI')
        self.assertEqual(2186, res)

    def test_MMCLXXXVII(self):
        res = convert_to_arabic('MMCLXXXVII')
        self.assertEqual(2187, res)

    def test_MMCLXXXVIII(self):
        res = convert_to_arabic('MMCLXXXVIII')
        self.assertEqual(2188, res)

    def test_MMCLXXXIX(self):
        res = convert_to_arabic('MMCLXXXIX')
        self.assertEqual(2189, res)

    def test_MMCXC(self):
        res = convert_to_arabic('MMCXC')
        self.assertEqual(2190, res)

    def test_MMCXCI(self):
        res = convert_to_arabic('MMCXCI')
        self.assertEqual(2191, res)

    def test_MMCXCII(self):
        res = convert_to_arabic('MMCXCII')
        self.assertEqual(2192, res)

    def test_MMCXCIII(self):
        res = convert_to_arabic('MMCXCIII')
        self.assertEqual(2193, res)

    def test_MMCXCIV(self):
        res = convert_to_arabic('MMCXCIV')
        self.assertEqual(2194, res)

    def test_MMCXCV(self):
        res = convert_to_arabic('MMCXCV')
        self.assertEqual(2195, res)

    def test_MMCXCVI(self):
        res = convert_to_arabic('MMCXCVI')
        self.assertEqual(2196, res)

    def test_MMCXCVII(self):
        res = convert_to_arabic('MMCXCVII')
        self.assertEqual(2197, res)

    def test_MMCXCVIII(self):
        res = convert_to_arabic('MMCXCVIII')
        self.assertEqual(2198, res)

    def test_MMCXCIX(self):
        res = convert_to_arabic('MMCXCIX')
        self.assertEqual(2199, res)

    def test_MMCC(self):
        res = convert_to_arabic('MMCC')
        self.assertEqual(2200, res)

    def test_MMCCI(self):
        res = convert_to_arabic('MMCCI')
        self.assertEqual(2201, res)

    def test_MMCCII(self):
        res = convert_to_arabic('MMCCII')
        self.assertEqual(2202, res)

    def test_MMCCIII(self):
        res = convert_to_arabic('MMCCIII')
        self.assertEqual(2203, res)

    def test_MMCCIV(self):
        res = convert_to_arabic('MMCCIV')
        self.assertEqual(2204, res)

    def test_MMCCV(self):
        res = convert_to_arabic('MMCCV')
        self.assertEqual(2205, res)

    def test_MMCCVI(self):
        res = convert_to_arabic('MMCCVI')
        self.assertEqual(2206, res)

    def test_MMCCVII(self):
        res = convert_to_arabic('MMCCVII')
        self.assertEqual(2207, res)

    def test_MMCCVIII(self):
        res = convert_to_arabic('MMCCVIII')
        self.assertEqual(2208, res)

    def test_MMCCIX(self):
        res = convert_to_arabic('MMCCIX')
        self.assertEqual(2209, res)

    def test_MMCCX(self):
        res = convert_to_arabic('MMCCX')
        self.assertEqual(2210, res)

    def test_MMCCXI(self):
        res = convert_to_arabic('MMCCXI')
        self.assertEqual(2211, res)

    def test_MMCCXII(self):
        res = convert_to_arabic('MMCCXII')
        self.assertEqual(2212, res)

    def test_MMCCXIII(self):
        res = convert_to_arabic('MMCCXIII')
        self.assertEqual(2213, res)

    def test_MMCCXIV(self):
        res = convert_to_arabic('MMCCXIV')
        self.assertEqual(2214, res)

    def test_MMCCXV(self):
        res = convert_to_arabic('MMCCXV')
        self.assertEqual(2215, res)

    def test_MMCCXVI(self):
        res = convert_to_arabic('MMCCXVI')
        self.assertEqual(2216, res)

    def test_MMCCXVII(self):
        res = convert_to_arabic('MMCCXVII')
        self.assertEqual(2217, res)

    def test_MMCCXVIII(self):
        res = convert_to_arabic('MMCCXVIII')
        self.assertEqual(2218, res)

    def test_MMCCXIX(self):
        res = convert_to_arabic('MMCCXIX')
        self.assertEqual(2219, res)

    def test_MMCCXX(self):
        res = convert_to_arabic('MMCCXX')
        self.assertEqual(2220, res)

    def test_MMCCXXI(self):
        res = convert_to_arabic('MMCCXXI')
        self.assertEqual(2221, res)

    def test_MMCCXXII(self):
        res = convert_to_arabic('MMCCXXII')
        self.assertEqual(2222, res)

    def test_MMCCXXIII(self):
        res = convert_to_arabic('MMCCXXIII')
        self.assertEqual(2223, res)

    def test_MMCCXXIV(self):
        res = convert_to_arabic('MMCCXXIV')
        self.assertEqual(2224, res)

    def test_MMCCXXV(self):
        res = convert_to_arabic('MMCCXXV')
        self.assertEqual(2225, res)

    def test_MMCCXXVI(self):
        res = convert_to_arabic('MMCCXXVI')
        self.assertEqual(2226, res)

    def test_MMCCXXVII(self):
        res = convert_to_arabic('MMCCXXVII')
        self.assertEqual(2227, res)

    def test_MMCCXXVIII(self):
        res = convert_to_arabic('MMCCXXVIII')
        self.assertEqual(2228, res)

    def test_MMCCXXIX(self):
        res = convert_to_arabic('MMCCXXIX')
        self.assertEqual(2229, res)

    def test_MMCCXXX(self):
        res = convert_to_arabic('MMCCXXX')
        self.assertEqual(2230, res)

    def test_MMCCXXXI(self):
        res = convert_to_arabic('MMCCXXXI')
        self.assertEqual(2231, res)

    def test_MMCCXXXII(self):
        res = convert_to_arabic('MMCCXXXII')
        self.assertEqual(2232, res)

    def test_MMCCXXXIII(self):
        res = convert_to_arabic('MMCCXXXIII')
        self.assertEqual(2233, res)

    def test_MMCCXXXIV(self):
        res = convert_to_arabic('MMCCXXXIV')
        self.assertEqual(2234, res)

    def test_MMCCXXXV(self):
        res = convert_to_arabic('MMCCXXXV')
        self.assertEqual(2235, res)

    def test_MMCCXXXVI(self):
        res = convert_to_arabic('MMCCXXXVI')
        self.assertEqual(2236, res)

    def test_MMCCXXXVII(self):
        res = convert_to_arabic('MMCCXXXVII')
        self.assertEqual(2237, res)

    def test_MMCCXXXVIII(self):
        res = convert_to_arabic('MMCCXXXVIII')
        self.assertEqual(2238, res)

    def test_MMCCXXXIX(self):
        res = convert_to_arabic('MMCCXXXIX')
        self.assertEqual(2239, res)

    def test_MMCCXL(self):
        res = convert_to_arabic('MMCCXL')
        self.assertEqual(2240, res)

    def test_MMCCXLI(self):
        res = convert_to_arabic('MMCCXLI')
        self.assertEqual(2241, res)

    def test_MMCCXLII(self):
        res = convert_to_arabic('MMCCXLII')
        self.assertEqual(2242, res)

    def test_MMCCXLIII(self):
        res = convert_to_arabic('MMCCXLIII')
        self.assertEqual(2243, res)

    def test_MMCCXLIV(self):
        res = convert_to_arabic('MMCCXLIV')
        self.assertEqual(2244, res)

    def test_MMCCXLV(self):
        res = convert_to_arabic('MMCCXLV')
        self.assertEqual(2245, res)

    def test_MMCCXLVI(self):
        res = convert_to_arabic('MMCCXLVI')
        self.assertEqual(2246, res)

    def test_MMCCXLVII(self):
        res = convert_to_arabic('MMCCXLVII')
        self.assertEqual(2247, res)

    def test_MMCCXLVIII(self):
        res = convert_to_arabic('MMCCXLVIII')
        self.assertEqual(2248, res)

    def test_MMCCXLIX(self):
        res = convert_to_arabic('MMCCXLIX')
        self.assertEqual(2249, res)

    def test_MMCCL(self):
        res = convert_to_arabic('MMCCL')
        self.assertEqual(2250, res)

    def test_MMCCLI(self):
        res = convert_to_arabic('MMCCLI')
        self.assertEqual(2251, res)

    def test_MMCCLII(self):
        res = convert_to_arabic('MMCCLII')
        self.assertEqual(2252, res)

    def test_MMCCLIII(self):
        res = convert_to_arabic('MMCCLIII')
        self.assertEqual(2253, res)

    def test_MMCCLIV(self):
        res = convert_to_arabic('MMCCLIV')
        self.assertEqual(2254, res)

    def test_MMCCLV(self):
        res = convert_to_arabic('MMCCLV')
        self.assertEqual(2255, res)

    def test_MMCCLVI(self):
        res = convert_to_arabic('MMCCLVI')
        self.assertEqual(2256, res)

    def test_MMCCLVII(self):
        res = convert_to_arabic('MMCCLVII')
        self.assertEqual(2257, res)

    def test_MMCCLVIII(self):
        res = convert_to_arabic('MMCCLVIII')
        self.assertEqual(2258, res)

    def test_MMCCLIX(self):
        res = convert_to_arabic('MMCCLIX')
        self.assertEqual(2259, res)

    def test_MMCCLX(self):
        res = convert_to_arabic('MMCCLX')
        self.assertEqual(2260, res)

    def test_MMCCLXI(self):
        res = convert_to_arabic('MMCCLXI')
        self.assertEqual(2261, res)

    def test_MMCCLXII(self):
        res = convert_to_arabic('MMCCLXII')
        self.assertEqual(2262, res)

    def test_MMCCLXIII(self):
        res = convert_to_arabic('MMCCLXIII')
        self.assertEqual(2263, res)

    def test_MMCCLXIV(self):
        res = convert_to_arabic('MMCCLXIV')
        self.assertEqual(2264, res)

    def test_MMCCLXV(self):
        res = convert_to_arabic('MMCCLXV')
        self.assertEqual(2265, res)

    def test_MMCCLXVI(self):
        res = convert_to_arabic('MMCCLXVI')
        self.assertEqual(2266, res)

    def test_MMCCLXVII(self):
        res = convert_to_arabic('MMCCLXVII')
        self.assertEqual(2267, res)

    def test_MMCCLXVIII(self):
        res = convert_to_arabic('MMCCLXVIII')
        self.assertEqual(2268, res)

    def test_MMCCLXIX(self):
        res = convert_to_arabic('MMCCLXIX')
        self.assertEqual(2269, res)

    def test_MMCCLXX(self):
        res = convert_to_arabic('MMCCLXX')
        self.assertEqual(2270, res)

    def test_MMCCLXXI(self):
        res = convert_to_arabic('MMCCLXXI')
        self.assertEqual(2271, res)

    def test_MMCCLXXII(self):
        res = convert_to_arabic('MMCCLXXII')
        self.assertEqual(2272, res)

    def test_MMCCLXXIII(self):
        res = convert_to_arabic('MMCCLXXIII')
        self.assertEqual(2273, res)

    def test_MMCCLXXIV(self):
        res = convert_to_arabic('MMCCLXXIV')
        self.assertEqual(2274, res)

    def test_MMCCLXXV(self):
        res = convert_to_arabic('MMCCLXXV')
        self.assertEqual(2275, res)

    def test_MMCCLXXVI(self):
        res = convert_to_arabic('MMCCLXXVI')
        self.assertEqual(2276, res)

    def test_MMCCLXXVII(self):
        res = convert_to_arabic('MMCCLXXVII')
        self.assertEqual(2277, res)

    def test_MMCCLXXVIII(self):
        res = convert_to_arabic('MMCCLXXVIII')
        self.assertEqual(2278, res)

    def test_MMCCLXXIX(self):
        res = convert_to_arabic('MMCCLXXIX')
        self.assertEqual(2279, res)

    def test_MMCCLXXX(self):
        res = convert_to_arabic('MMCCLXXX')
        self.assertEqual(2280, res)

    def test_MMCCLXXXI(self):
        res = convert_to_arabic('MMCCLXXXI')
        self.assertEqual(2281, res)

    def test_MMCCLXXXII(self):
        res = convert_to_arabic('MMCCLXXXII')
        self.assertEqual(2282, res)

    def test_MMCCLXXXIII(self):
        res = convert_to_arabic('MMCCLXXXIII')
        self.assertEqual(2283, res)

    def test_MMCCLXXXIV(self):
        res = convert_to_arabic('MMCCLXXXIV')
        self.assertEqual(2284, res)

    def test_MMCCLXXXV(self):
        res = convert_to_arabic('MMCCLXXXV')
        self.assertEqual(2285, res)

    def test_MMCCLXXXVI(self):
        res = convert_to_arabic('MMCCLXXXVI')
        self.assertEqual(2286, res)

    def test_MMCCLXXXVII(self):
        res = convert_to_arabic('MMCCLXXXVII')
        self.assertEqual(2287, res)

    def test_MMCCLXXXVIII(self):
        res = convert_to_arabic('MMCCLXXXVIII')
        self.assertEqual(2288, res)

    def test_MMCCLXXXIX(self):
        res = convert_to_arabic('MMCCLXXXIX')
        self.assertEqual(2289, res)

    def test_MMCCXC(self):
        res = convert_to_arabic('MMCCXC')
        self.assertEqual(2290, res)

    def test_MMCCXCI(self):
        res = convert_to_arabic('MMCCXCI')
        self.assertEqual(2291, res)

    def test_MMCCXCII(self):
        res = convert_to_arabic('MMCCXCII')
        self.assertEqual(2292, res)

    def test_MMCCXCIII(self):
        res = convert_to_arabic('MMCCXCIII')
        self.assertEqual(2293, res)

    def test_MMCCXCIV(self):
        res = convert_to_arabic('MMCCXCIV')
        self.assertEqual(2294, res)

    def test_MMCCXCV(self):
        res = convert_to_arabic('MMCCXCV')
        self.assertEqual(2295, res)

    def test_MMCCXCVI(self):
        res = convert_to_arabic('MMCCXCVI')
        self.assertEqual(2296, res)

    def test_MMCCXCVII(self):
        res = convert_to_arabic('MMCCXCVII')
        self.assertEqual(2297, res)

    def test_MMCCXCVIII(self):
        res = convert_to_arabic('MMCCXCVIII')
        self.assertEqual(2298, res)

    def test_MMCCXCIX(self):
        res = convert_to_arabic('MMCCXCIX')
        self.assertEqual(2299, res)

    def test_MMCCC(self):
        res = convert_to_arabic('MMCCC')
        self.assertEqual(2300, res)

    def test_MMCCCI(self):
        res = convert_to_arabic('MMCCCI')
        self.assertEqual(2301, res)

    def test_MMCCCII(self):
        res = convert_to_arabic('MMCCCII')
        self.assertEqual(2302, res)

    def test_MMCCCIII(self):
        res = convert_to_arabic('MMCCCIII')
        self.assertEqual(2303, res)

    def test_MMCCCIV(self):
        res = convert_to_arabic('MMCCCIV')
        self.assertEqual(2304, res)

    def test_MMCCCV(self):
        res = convert_to_arabic('MMCCCV')
        self.assertEqual(2305, res)

    def test_MMCCCVI(self):
        res = convert_to_arabic('MMCCCVI')
        self.assertEqual(2306, res)

    def test_MMCCCVII(self):
        res = convert_to_arabic('MMCCCVII')
        self.assertEqual(2307, res)

    def test_MMCCCVIII(self):
        res = convert_to_arabic('MMCCCVIII')
        self.assertEqual(2308, res)

    def test_MMCCCIX(self):
        res = convert_to_arabic('MMCCCIX')
        self.assertEqual(2309, res)

    def test_MMCCCX(self):
        res = convert_to_arabic('MMCCCX')
        self.assertEqual(2310, res)

    def test_MMCCCXI(self):
        res = convert_to_arabic('MMCCCXI')
        self.assertEqual(2311, res)

    def test_MMCCCXII(self):
        res = convert_to_arabic('MMCCCXII')
        self.assertEqual(2312, res)

    def test_MMCCCXIII(self):
        res = convert_to_arabic('MMCCCXIII')
        self.assertEqual(2313, res)

    def test_MMCCCXIV(self):
        res = convert_to_arabic('MMCCCXIV')
        self.assertEqual(2314, res)

    def test_MMCCCXV(self):
        res = convert_to_arabic('MMCCCXV')
        self.assertEqual(2315, res)

    def test_MMCCCXVI(self):
        res = convert_to_arabic('MMCCCXVI')
        self.assertEqual(2316, res)

    def test_MMCCCXVII(self):
        res = convert_to_arabic('MMCCCXVII')
        self.assertEqual(2317, res)

    def test_MMCCCXVIII(self):
        res = convert_to_arabic('MMCCCXVIII')
        self.assertEqual(2318, res)

    def test_MMCCCXIX(self):
        res = convert_to_arabic('MMCCCXIX')
        self.assertEqual(2319, res)

    def test_MMCCCXX(self):
        res = convert_to_arabic('MMCCCXX')
        self.assertEqual(2320, res)

    def test_MMCCCXXI(self):
        res = convert_to_arabic('MMCCCXXI')
        self.assertEqual(2321, res)

    def test_MMCCCXXII(self):
        res = convert_to_arabic('MMCCCXXII')
        self.assertEqual(2322, res)

    def test_MMCCCXXIII(self):
        res = convert_to_arabic('MMCCCXXIII')
        self.assertEqual(2323, res)

    def test_MMCCCXXIV(self):
        res = convert_to_arabic('MMCCCXXIV')
        self.assertEqual(2324, res)

    def test_MMCCCXXV(self):
        res = convert_to_arabic('MMCCCXXV')
        self.assertEqual(2325, res)

    def test_MMCCCXXVI(self):
        res = convert_to_arabic('MMCCCXXVI')
        self.assertEqual(2326, res)

    def test_MMCCCXXVII(self):
        res = convert_to_arabic('MMCCCXXVII')
        self.assertEqual(2327, res)

    def test_MMCCCXXVIII(self):
        res = convert_to_arabic('MMCCCXXVIII')
        self.assertEqual(2328, res)

    def test_MMCCCXXIX(self):
        res = convert_to_arabic('MMCCCXXIX')
        self.assertEqual(2329, res)

    def test_MMCCCXXX(self):
        res = convert_to_arabic('MMCCCXXX')
        self.assertEqual(2330, res)

    def test_MMCCCXXXI(self):
        res = convert_to_arabic('MMCCCXXXI')
        self.assertEqual(2331, res)

    def test_MMCCCXXXII(self):
        res = convert_to_arabic('MMCCCXXXII')
        self.assertEqual(2332, res)

    def test_MMCCCXXXIII(self):
        res = convert_to_arabic('MMCCCXXXIII')
        self.assertEqual(2333, res)

    def test_MMCCCXXXIV(self):
        res = convert_to_arabic('MMCCCXXXIV')
        self.assertEqual(2334, res)

    def test_MMCCCXXXV(self):
        res = convert_to_arabic('MMCCCXXXV')
        self.assertEqual(2335, res)

    def test_MMCCCXXXVI(self):
        res = convert_to_arabic('MMCCCXXXVI')
        self.assertEqual(2336, res)

    def test_MMCCCXXXVII(self):
        res = convert_to_arabic('MMCCCXXXVII')
        self.assertEqual(2337, res)

    def test_MMCCCXXXVIII(self):
        res = convert_to_arabic('MMCCCXXXVIII')
        self.assertEqual(2338, res)

    def test_MMCCCXXXIX(self):
        res = convert_to_arabic('MMCCCXXXIX')
        self.assertEqual(2339, res)

    def test_MMCCCXL(self):
        res = convert_to_arabic('MMCCCXL')
        self.assertEqual(2340, res)

    def test_MMCCCXLI(self):
        res = convert_to_arabic('MMCCCXLI')
        self.assertEqual(2341, res)

    def test_MMCCCXLII(self):
        res = convert_to_arabic('MMCCCXLII')
        self.assertEqual(2342, res)

    def test_MMCCCXLIII(self):
        res = convert_to_arabic('MMCCCXLIII')
        self.assertEqual(2343, res)

    def test_MMCCCXLIV(self):
        res = convert_to_arabic('MMCCCXLIV')
        self.assertEqual(2344, res)

    def test_MMCCCXLV(self):
        res = convert_to_arabic('MMCCCXLV')
        self.assertEqual(2345, res)

    def test_MMCCCXLVI(self):
        res = convert_to_arabic('MMCCCXLVI')
        self.assertEqual(2346, res)

    def test_MMCCCXLVII(self):
        res = convert_to_arabic('MMCCCXLVII')
        self.assertEqual(2347, res)

    def test_MMCCCXLVIII(self):
        res = convert_to_arabic('MMCCCXLVIII')
        self.assertEqual(2348, res)

    def test_MMCCCXLIX(self):
        res = convert_to_arabic('MMCCCXLIX')
        self.assertEqual(2349, res)

    def test_MMCCCL(self):
        res = convert_to_arabic('MMCCCL')
        self.assertEqual(2350, res)

    def test_MMCCCLI(self):
        res = convert_to_arabic('MMCCCLI')
        self.assertEqual(2351, res)

    def test_MMCCCLII(self):
        res = convert_to_arabic('MMCCCLII')
        self.assertEqual(2352, res)

    def test_MMCCCLIII(self):
        res = convert_to_arabic('MMCCCLIII')
        self.assertEqual(2353, res)

    def test_MMCCCLIV(self):
        res = convert_to_arabic('MMCCCLIV')
        self.assertEqual(2354, res)

    def test_MMCCCLV(self):
        res = convert_to_arabic('MMCCCLV')
        self.assertEqual(2355, res)

    def test_MMCCCLVI(self):
        res = convert_to_arabic('MMCCCLVI')
        self.assertEqual(2356, res)

    def test_MMCCCLVII(self):
        res = convert_to_arabic('MMCCCLVII')
        self.assertEqual(2357, res)

    def test_MMCCCLVIII(self):
        res = convert_to_arabic('MMCCCLVIII')
        self.assertEqual(2358, res)

    def test_MMCCCLIX(self):
        res = convert_to_arabic('MMCCCLIX')
        self.assertEqual(2359, res)

    def test_MMCCCLX(self):
        res = convert_to_arabic('MMCCCLX')
        self.assertEqual(2360, res)

    def test_MMCCCLXI(self):
        res = convert_to_arabic('MMCCCLXI')
        self.assertEqual(2361, res)

    def test_MMCCCLXII(self):
        res = convert_to_arabic('MMCCCLXII')
        self.assertEqual(2362, res)

    def test_MMCCCLXIII(self):
        res = convert_to_arabic('MMCCCLXIII')
        self.assertEqual(2363, res)

    def test_MMCCCLXIV(self):
        res = convert_to_arabic('MMCCCLXIV')
        self.assertEqual(2364, res)

    def test_MMCCCLXV(self):
        res = convert_to_arabic('MMCCCLXV')
        self.assertEqual(2365, res)

    def test_MMCCCLXVI(self):
        res = convert_to_arabic('MMCCCLXVI')
        self.assertEqual(2366, res)

    def test_MMCCCLXVII(self):
        res = convert_to_arabic('MMCCCLXVII')
        self.assertEqual(2367, res)

    def test_MMCCCLXVIII(self):
        res = convert_to_arabic('MMCCCLXVIII')
        self.assertEqual(2368, res)

    def test_MMCCCLXIX(self):
        res = convert_to_arabic('MMCCCLXIX')
        self.assertEqual(2369, res)

    def test_MMCCCLXX(self):
        res = convert_to_arabic('MMCCCLXX')
        self.assertEqual(2370, res)

    def test_MMCCCLXXI(self):
        res = convert_to_arabic('MMCCCLXXI')
        self.assertEqual(2371, res)

    def test_MMCCCLXXII(self):
        res = convert_to_arabic('MMCCCLXXII')
        self.assertEqual(2372, res)

    def test_MMCCCLXXIII(self):
        res = convert_to_arabic('MMCCCLXXIII')
        self.assertEqual(2373, res)

    def test_MMCCCLXXIV(self):
        res = convert_to_arabic('MMCCCLXXIV')
        self.assertEqual(2374, res)

    def test_MMCCCLXXV(self):
        res = convert_to_arabic('MMCCCLXXV')
        self.assertEqual(2375, res)

    def test_MMCCCLXXVI(self):
        res = convert_to_arabic('MMCCCLXXVI')
        self.assertEqual(2376, res)

    def test_MMCCCLXXVII(self):
        res = convert_to_arabic('MMCCCLXXVII')
        self.assertEqual(2377, res)

    def test_MMCCCLXXVIII(self):
        res = convert_to_arabic('MMCCCLXXVIII')
        self.assertEqual(2378, res)

    def test_MMCCCLXXIX(self):
        res = convert_to_arabic('MMCCCLXXIX')
        self.assertEqual(2379, res)

    def test_MMCCCLXXX(self):
        res = convert_to_arabic('MMCCCLXXX')
        self.assertEqual(2380, res)

    def test_MMCCCLXXXI(self):
        res = convert_to_arabic('MMCCCLXXXI')
        self.assertEqual(2381, res)

    def test_MMCCCLXXXII(self):
        res = convert_to_arabic('MMCCCLXXXII')
        self.assertEqual(2382, res)

    def test_MMCCCLXXXIII(self):
        res = convert_to_arabic('MMCCCLXXXIII')
        self.assertEqual(2383, res)

    def test_MMCCCLXXXIV(self):
        res = convert_to_arabic('MMCCCLXXXIV')
        self.assertEqual(2384, res)

    def test_MMCCCLXXXV(self):
        res = convert_to_arabic('MMCCCLXXXV')
        self.assertEqual(2385, res)

    def test_MMCCCLXXXVI(self):
        res = convert_to_arabic('MMCCCLXXXVI')
        self.assertEqual(2386, res)

    def test_MMCCCLXXXVII(self):
        res = convert_to_arabic('MMCCCLXXXVII')
        self.assertEqual(2387, res)

    def test_MMCCCLXXXVIII(self):
        res = convert_to_arabic('MMCCCLXXXVIII')
        self.assertEqual(2388, res)

    def test_MMCCCLXXXIX(self):
        res = convert_to_arabic('MMCCCLXXXIX')
        self.assertEqual(2389, res)

    def test_MMCCCXC(self):
        res = convert_to_arabic('MMCCCXC')
        self.assertEqual(2390, res)

    def test_MMCCCXCI(self):
        res = convert_to_arabic('MMCCCXCI')
        self.assertEqual(2391, res)

    def test_MMCCCXCII(self):
        res = convert_to_arabic('MMCCCXCII')
        self.assertEqual(2392, res)

    def test_MMCCCXCIII(self):
        res = convert_to_arabic('MMCCCXCIII')
        self.assertEqual(2393, res)

    def test_MMCCCXCIV(self):
        res = convert_to_arabic('MMCCCXCIV')
        self.assertEqual(2394, res)

    def test_MMCCCXCV(self):
        res = convert_to_arabic('MMCCCXCV')
        self.assertEqual(2395, res)

    def test_MMCCCXCVI(self):
        res = convert_to_arabic('MMCCCXCVI')
        self.assertEqual(2396, res)

    def test_MMCCCXCVII(self):
        res = convert_to_arabic('MMCCCXCVII')
        self.assertEqual(2397, res)

    def test_MMCCCXCVIII(self):
        res = convert_to_arabic('MMCCCXCVIII')
        self.assertEqual(2398, res)

    def test_MMCCCXCIX(self):
        res = convert_to_arabic('MMCCCXCIX')
        self.assertEqual(2399, res)

    def test_MMCD(self):
        res = convert_to_arabic('MMCD')
        self.assertEqual(2400, res)

    def test_MMCDI(self):
        res = convert_to_arabic('MMCDI')
        self.assertEqual(2401, res)

    def test_MMCDII(self):
        res = convert_to_arabic('MMCDII')
        self.assertEqual(2402, res)

    def test_MMCDIII(self):
        res = convert_to_arabic('MMCDIII')
        self.assertEqual(2403, res)

    def test_MMCDIV(self):
        res = convert_to_arabic('MMCDIV')
        self.assertEqual(2404, res)

    def test_MMCDV(self):
        res = convert_to_arabic('MMCDV')
        self.assertEqual(2405, res)

    def test_MMCDVI(self):
        res = convert_to_arabic('MMCDVI')
        self.assertEqual(2406, res)

    def test_MMCDVII(self):
        res = convert_to_arabic('MMCDVII')
        self.assertEqual(2407, res)

    def test_MMCDVIII(self):
        res = convert_to_arabic('MMCDVIII')
        self.assertEqual(2408, res)

    def test_MMCDIX(self):
        res = convert_to_arabic('MMCDIX')
        self.assertEqual(2409, res)

    def test_MMCDX(self):
        res = convert_to_arabic('MMCDX')
        self.assertEqual(2410, res)

    def test_MMCDXI(self):
        res = convert_to_arabic('MMCDXI')
        self.assertEqual(2411, res)

    def test_MMCDXII(self):
        res = convert_to_arabic('MMCDXII')
        self.assertEqual(2412, res)

    def test_MMCDXIII(self):
        res = convert_to_arabic('MMCDXIII')
        self.assertEqual(2413, res)

    def test_MMCDXIV(self):
        res = convert_to_arabic('MMCDXIV')
        self.assertEqual(2414, res)

    def test_MMCDXV(self):
        res = convert_to_arabic('MMCDXV')
        self.assertEqual(2415, res)

    def test_MMCDXVI(self):
        res = convert_to_arabic('MMCDXVI')
        self.assertEqual(2416, res)

    def test_MMCDXVII(self):
        res = convert_to_arabic('MMCDXVII')
        self.assertEqual(2417, res)

    def test_MMCDXVIII(self):
        res = convert_to_arabic('MMCDXVIII')
        self.assertEqual(2418, res)

    def test_MMCDXIX(self):
        res = convert_to_arabic('MMCDXIX')
        self.assertEqual(2419, res)

    def test_MMCDXX(self):
        res = convert_to_arabic('MMCDXX')
        self.assertEqual(2420, res)

    def test_MMCDXXI(self):
        res = convert_to_arabic('MMCDXXI')
        self.assertEqual(2421, res)

    def test_MMCDXXII(self):
        res = convert_to_arabic('MMCDXXII')
        self.assertEqual(2422, res)

    def test_MMCDXXIII(self):
        res = convert_to_arabic('MMCDXXIII')
        self.assertEqual(2423, res)

    def test_MMCDXXIV(self):
        res = convert_to_arabic('MMCDXXIV')
        self.assertEqual(2424, res)

    def test_MMCDXXV(self):
        res = convert_to_arabic('MMCDXXV')
        self.assertEqual(2425, res)

    def test_MMCDXXVI(self):
        res = convert_to_arabic('MMCDXXVI')
        self.assertEqual(2426, res)

    def test_MMCDXXVII(self):
        res = convert_to_arabic('MMCDXXVII')
        self.assertEqual(2427, res)

    def test_MMCDXXVIII(self):
        res = convert_to_arabic('MMCDXXVIII')
        self.assertEqual(2428, res)

    def test_MMCDXXIX(self):
        res = convert_to_arabic('MMCDXXIX')
        self.assertEqual(2429, res)

    def test_MMCDXXX(self):
        res = convert_to_arabic('MMCDXXX')
        self.assertEqual(2430, res)

    def test_MMCDXXXI(self):
        res = convert_to_arabic('MMCDXXXI')
        self.assertEqual(2431, res)

    def test_MMCDXXXII(self):
        res = convert_to_arabic('MMCDXXXII')
        self.assertEqual(2432, res)

    def test_MMCDXXXIII(self):
        res = convert_to_arabic('MMCDXXXIII')
        self.assertEqual(2433, res)

    def test_MMCDXXXIV(self):
        res = convert_to_arabic('MMCDXXXIV')
        self.assertEqual(2434, res)

    def test_MMCDXXXV(self):
        res = convert_to_arabic('MMCDXXXV')
        self.assertEqual(2435, res)

    def test_MMCDXXXVI(self):
        res = convert_to_arabic('MMCDXXXVI')
        self.assertEqual(2436, res)

    def test_MMCDXXXVII(self):
        res = convert_to_arabic('MMCDXXXVII')
        self.assertEqual(2437, res)

    def test_MMCDXXXVIII(self):
        res = convert_to_arabic('MMCDXXXVIII')
        self.assertEqual(2438, res)

    def test_MMCDXXXIX(self):
        res = convert_to_arabic('MMCDXXXIX')
        self.assertEqual(2439, res)

    def test_MMCDXL(self):
        res = convert_to_arabic('MMCDXL')
        self.assertEqual(2440, res)

    def test_MMCDXLI(self):
        res = convert_to_arabic('MMCDXLI')
        self.assertEqual(2441, res)

    def test_MMCDXLII(self):
        res = convert_to_arabic('MMCDXLII')
        self.assertEqual(2442, res)

    def test_MMCDXLIII(self):
        res = convert_to_arabic('MMCDXLIII')
        self.assertEqual(2443, res)

    def test_MMCDXLIV(self):
        res = convert_to_arabic('MMCDXLIV')
        self.assertEqual(2444, res)

    def test_MMCDXLV(self):
        res = convert_to_arabic('MMCDXLV')
        self.assertEqual(2445, res)

    def test_MMCDXLVI(self):
        res = convert_to_arabic('MMCDXLVI')
        self.assertEqual(2446, res)

    def test_MMCDXLVII(self):
        res = convert_to_arabic('MMCDXLVII')
        self.assertEqual(2447, res)

    def test_MMCDXLVIII(self):
        res = convert_to_arabic('MMCDXLVIII')
        self.assertEqual(2448, res)

    def test_MMCDXLIX(self):
        res = convert_to_arabic('MMCDXLIX')
        self.assertEqual(2449, res)

    def test_MMCDL(self):
        res = convert_to_arabic('MMCDL')
        self.assertEqual(2450, res)

    def test_MMCDLI(self):
        res = convert_to_arabic('MMCDLI')
        self.assertEqual(2451, res)

    def test_MMCDLII(self):
        res = convert_to_arabic('MMCDLII')
        self.assertEqual(2452, res)

    def test_MMCDLIII(self):
        res = convert_to_arabic('MMCDLIII')
        self.assertEqual(2453, res)

    def test_MMCDLIV(self):
        res = convert_to_arabic('MMCDLIV')
        self.assertEqual(2454, res)

    def test_MMCDLV(self):
        res = convert_to_arabic('MMCDLV')
        self.assertEqual(2455, res)

    def test_MMCDLVI(self):
        res = convert_to_arabic('MMCDLVI')
        self.assertEqual(2456, res)

    def test_MMCDLVII(self):
        res = convert_to_arabic('MMCDLVII')
        self.assertEqual(2457, res)

    def test_MMCDLVIII(self):
        res = convert_to_arabic('MMCDLVIII')
        self.assertEqual(2458, res)

    def test_MMCDLIX(self):
        res = convert_to_arabic('MMCDLIX')
        self.assertEqual(2459, res)

    def test_MMCDLX(self):
        res = convert_to_arabic('MMCDLX')
        self.assertEqual(2460, res)

    def test_MMCDLXI(self):
        res = convert_to_arabic('MMCDLXI')
        self.assertEqual(2461, res)

    def test_MMCDLXII(self):
        res = convert_to_arabic('MMCDLXII')
        self.assertEqual(2462, res)

    def test_MMCDLXIII(self):
        res = convert_to_arabic('MMCDLXIII')
        self.assertEqual(2463, res)

    def test_MMCDLXIV(self):
        res = convert_to_arabic('MMCDLXIV')
        self.assertEqual(2464, res)

    def test_MMCDLXV(self):
        res = convert_to_arabic('MMCDLXV')
        self.assertEqual(2465, res)

    def test_MMCDLXVI(self):
        res = convert_to_arabic('MMCDLXVI')
        self.assertEqual(2466, res)

    def test_MMCDLXVII(self):
        res = convert_to_arabic('MMCDLXVII')
        self.assertEqual(2467, res)

    def test_MMCDLXVIII(self):
        res = convert_to_arabic('MMCDLXVIII')
        self.assertEqual(2468, res)

    def test_MMCDLXIX(self):
        res = convert_to_arabic('MMCDLXIX')
        self.assertEqual(2469, res)

    def test_MMCDLXX(self):
        res = convert_to_arabic('MMCDLXX')
        self.assertEqual(2470, res)

    def test_MMCDLXXI(self):
        res = convert_to_arabic('MMCDLXXI')
        self.assertEqual(2471, res)

    def test_MMCDLXXII(self):
        res = convert_to_arabic('MMCDLXXII')
        self.assertEqual(2472, res)

    def test_MMCDLXXIII(self):
        res = convert_to_arabic('MMCDLXXIII')
        self.assertEqual(2473, res)

    def test_MMCDLXXIV(self):
        res = convert_to_arabic('MMCDLXXIV')
        self.assertEqual(2474, res)

    def test_MMCDLXXV(self):
        res = convert_to_arabic('MMCDLXXV')
        self.assertEqual(2475, res)

    def test_MMCDLXXVI(self):
        res = convert_to_arabic('MMCDLXXVI')
        self.assertEqual(2476, res)

    def test_MMCDLXXVII(self):
        res = convert_to_arabic('MMCDLXXVII')
        self.assertEqual(2477, res)

    def test_MMCDLXXVIII(self):
        res = convert_to_arabic('MMCDLXXVIII')
        self.assertEqual(2478, res)

    def test_MMCDLXXIX(self):
        res = convert_to_arabic('MMCDLXXIX')
        self.assertEqual(2479, res)

    def test_MMCDLXXX(self):
        res = convert_to_arabic('MMCDLXXX')
        self.assertEqual(2480, res)

    def test_MMCDLXXXI(self):
        res = convert_to_arabic('MMCDLXXXI')
        self.assertEqual(2481, res)

    def test_MMCDLXXXII(self):
        res = convert_to_arabic('MMCDLXXXII')
        self.assertEqual(2482, res)

    def test_MMCDLXXXIII(self):
        res = convert_to_arabic('MMCDLXXXIII')
        self.assertEqual(2483, res)

    def test_MMCDLXXXIV(self):
        res = convert_to_arabic('MMCDLXXXIV')
        self.assertEqual(2484, res)

    def test_MMCDLXXXV(self):
        res = convert_to_arabic('MMCDLXXXV')
        self.assertEqual(2485, res)

    def test_MMCDLXXXVI(self):
        res = convert_to_arabic('MMCDLXXXVI')
        self.assertEqual(2486, res)

    def test_MMCDLXXXVII(self):
        res = convert_to_arabic('MMCDLXXXVII')
        self.assertEqual(2487, res)

    def test_MMCDLXXXVIII(self):
        res = convert_to_arabic('MMCDLXXXVIII')
        self.assertEqual(2488, res)

    def test_MMCDLXXXIX(self):
        res = convert_to_arabic('MMCDLXXXIX')
        self.assertEqual(2489, res)

    def test_MMCDXC(self):
        res = convert_to_arabic('MMCDXC')
        self.assertEqual(2490, res)

    def test_MMCDXCI(self):
        res = convert_to_arabic('MMCDXCI')
        self.assertEqual(2491, res)

    def test_MMCDXCII(self):
        res = convert_to_arabic('MMCDXCII')
        self.assertEqual(2492, res)

    def test_MMCDXCIII(self):
        res = convert_to_arabic('MMCDXCIII')
        self.assertEqual(2493, res)

    def test_MMCDXCIV(self):
        res = convert_to_arabic('MMCDXCIV')
        self.assertEqual(2494, res)

    def test_MMCDXCV(self):
        res = convert_to_arabic('MMCDXCV')
        self.assertEqual(2495, res)

    def test_MMCDXCVI(self):
        res = convert_to_arabic('MMCDXCVI')
        self.assertEqual(2496, res)

    def test_MMCDXCVII(self):
        res = convert_to_arabic('MMCDXCVII')
        self.assertEqual(2497, res)

    def test_MMCDXCVIII(self):
        res = convert_to_arabic('MMCDXCVIII')
        self.assertEqual(2498, res)

    def test_MMCDXCIX(self):
        res = convert_to_arabic('MMCDXCIX')
        self.assertEqual(2499, res)

    def test_MMD(self):
        res = convert_to_arabic('MMD')
        self.assertEqual(2500, res)

    def test_MMDI(self):
        res = convert_to_arabic('MMDI')
        self.assertEqual(2501, res)

    def test_MMDII(self):
        res = convert_to_arabic('MMDII')
        self.assertEqual(2502, res)

    def test_MMDIII(self):
        res = convert_to_arabic('MMDIII')
        self.assertEqual(2503, res)

    def test_MMDIV(self):
        res = convert_to_arabic('MMDIV')
        self.assertEqual(2504, res)

    def test_MMDV(self):
        res = convert_to_arabic('MMDV')
        self.assertEqual(2505, res)

    def test_MMDVI(self):
        res = convert_to_arabic('MMDVI')
        self.assertEqual(2506, res)

    def test_MMDVII(self):
        res = convert_to_arabic('MMDVII')
        self.assertEqual(2507, res)

    def test_MMDVIII(self):
        res = convert_to_arabic('MMDVIII')
        self.assertEqual(2508, res)

    def test_MMDIX(self):
        res = convert_to_arabic('MMDIX')
        self.assertEqual(2509, res)

    def test_MMDX(self):
        res = convert_to_arabic('MMDX')
        self.assertEqual(2510, res)

    def test_MMDXI(self):
        res = convert_to_arabic('MMDXI')
        self.assertEqual(2511, res)

    def test_MMDXII(self):
        res = convert_to_arabic('MMDXII')
        self.assertEqual(2512, res)

    def test_MMDXIII(self):
        res = convert_to_arabic('MMDXIII')
        self.assertEqual(2513, res)

    def test_MMDXIV(self):
        res = convert_to_arabic('MMDXIV')
        self.assertEqual(2514, res)

    def test_MMDXV(self):
        res = convert_to_arabic('MMDXV')
        self.assertEqual(2515, res)

    def test_MMDXVI(self):
        res = convert_to_arabic('MMDXVI')
        self.assertEqual(2516, res)

    def test_MMDXVII(self):
        res = convert_to_arabic('MMDXVII')
        self.assertEqual(2517, res)

    def test_MMDXVIII(self):
        res = convert_to_arabic('MMDXVIII')
        self.assertEqual(2518, res)

    def test_MMDXIX(self):
        res = convert_to_arabic('MMDXIX')
        self.assertEqual(2519, res)

    def test_MMDXX(self):
        res = convert_to_arabic('MMDXX')
        self.assertEqual(2520, res)

    def test_MMDXXI(self):
        res = convert_to_arabic('MMDXXI')
        self.assertEqual(2521, res)

    def test_MMDXXII(self):
        res = convert_to_arabic('MMDXXII')
        self.assertEqual(2522, res)

    def test_MMDXXIII(self):
        res = convert_to_arabic('MMDXXIII')
        self.assertEqual(2523, res)

    def test_MMDXXIV(self):
        res = convert_to_arabic('MMDXXIV')
        self.assertEqual(2524, res)

    def test_MMDXXV(self):
        res = convert_to_arabic('MMDXXV')
        self.assertEqual(2525, res)

    def test_MMDXXVI(self):
        res = convert_to_arabic('MMDXXVI')
        self.assertEqual(2526, res)

    def test_MMDXXVII(self):
        res = convert_to_arabic('MMDXXVII')
        self.assertEqual(2527, res)

    def test_MMDXXVIII(self):
        res = convert_to_arabic('MMDXXVIII')
        self.assertEqual(2528, res)

    def test_MMDXXIX(self):
        res = convert_to_arabic('MMDXXIX')
        self.assertEqual(2529, res)

    def test_MMDXXX(self):
        res = convert_to_arabic('MMDXXX')
        self.assertEqual(2530, res)

    def test_MMDXXXI(self):
        res = convert_to_arabic('MMDXXXI')
        self.assertEqual(2531, res)

    def test_MMDXXXII(self):
        res = convert_to_arabic('MMDXXXII')
        self.assertEqual(2532, res)

    def test_MMDXXXIII(self):
        res = convert_to_arabic('MMDXXXIII')
        self.assertEqual(2533, res)

    def test_MMDXXXIV(self):
        res = convert_to_arabic('MMDXXXIV')
        self.assertEqual(2534, res)

    def test_MMDXXXV(self):
        res = convert_to_arabic('MMDXXXV')
        self.assertEqual(2535, res)

    def test_MMDXXXVI(self):
        res = convert_to_arabic('MMDXXXVI')
        self.assertEqual(2536, res)

    def test_MMDXXXVII(self):
        res = convert_to_arabic('MMDXXXVII')
        self.assertEqual(2537, res)

    def test_MMDXXXVIII(self):
        res = convert_to_arabic('MMDXXXVIII')
        self.assertEqual(2538, res)

    def test_MMDXXXIX(self):
        res = convert_to_arabic('MMDXXXIX')
        self.assertEqual(2539, res)

    def test_MMDXL(self):
        res = convert_to_arabic('MMDXL')
        self.assertEqual(2540, res)

    def test_MMDXLI(self):
        res = convert_to_arabic('MMDXLI')
        self.assertEqual(2541, res)

    def test_MMDXLII(self):
        res = convert_to_arabic('MMDXLII')
        self.assertEqual(2542, res)

    def test_MMDXLIII(self):
        res = convert_to_arabic('MMDXLIII')
        self.assertEqual(2543, res)

    def test_MMDXLIV(self):
        res = convert_to_arabic('MMDXLIV')
        self.assertEqual(2544, res)

    def test_MMDXLV(self):
        res = convert_to_arabic('MMDXLV')
        self.assertEqual(2545, res)

    def test_MMDXLVI(self):
        res = convert_to_arabic('MMDXLVI')
        self.assertEqual(2546, res)

    def test_MMDXLVII(self):
        res = convert_to_arabic('MMDXLVII')
        self.assertEqual(2547, res)

    def test_MMDXLVIII(self):
        res = convert_to_arabic('MMDXLVIII')
        self.assertEqual(2548, res)

    def test_MMDXLIX(self):
        res = convert_to_arabic('MMDXLIX')
        self.assertEqual(2549, res)

    def test_MMDL(self):
        res = convert_to_arabic('MMDL')
        self.assertEqual(2550, res)

    def test_MMDLI(self):
        res = convert_to_arabic('MMDLI')
        self.assertEqual(2551, res)

    def test_MMDLII(self):
        res = convert_to_arabic('MMDLII')
        self.assertEqual(2552, res)

    def test_MMDLIII(self):
        res = convert_to_arabic('MMDLIII')
        self.assertEqual(2553, res)

    def test_MMDLIV(self):
        res = convert_to_arabic('MMDLIV')
        self.assertEqual(2554, res)

    def test_MMDLV(self):
        res = convert_to_arabic('MMDLV')
        self.assertEqual(2555, res)

    def test_MMDLVI(self):
        res = convert_to_arabic('MMDLVI')
        self.assertEqual(2556, res)

    def test_MMDLVII(self):
        res = convert_to_arabic('MMDLVII')
        self.assertEqual(2557, res)

    def test_MMDLVIII(self):
        res = convert_to_arabic('MMDLVIII')
        self.assertEqual(2558, res)

    def test_MMDLIX(self):
        res = convert_to_arabic('MMDLIX')
        self.assertEqual(2559, res)

    def test_MMDLX(self):
        res = convert_to_arabic('MMDLX')
        self.assertEqual(2560, res)

    def test_MMDLXI(self):
        res = convert_to_arabic('MMDLXI')
        self.assertEqual(2561, res)

    def test_MMDLXII(self):
        res = convert_to_arabic('MMDLXII')
        self.assertEqual(2562, res)

    def test_MMDLXIII(self):
        res = convert_to_arabic('MMDLXIII')
        self.assertEqual(2563, res)

    def test_MMDLXIV(self):
        res = convert_to_arabic('MMDLXIV')
        self.assertEqual(2564, res)

    def test_MMDLXV(self):
        res = convert_to_arabic('MMDLXV')
        self.assertEqual(2565, res)

    def test_MMDLXVI(self):
        res = convert_to_arabic('MMDLXVI')
        self.assertEqual(2566, res)

    def test_MMDLXVII(self):
        res = convert_to_arabic('MMDLXVII')
        self.assertEqual(2567, res)

    def test_MMDLXVIII(self):
        res = convert_to_arabic('MMDLXVIII')
        self.assertEqual(2568, res)

    def test_MMDLXIX(self):
        res = convert_to_arabic('MMDLXIX')
        self.assertEqual(2569, res)

    def test_MMDLXX(self):
        res = convert_to_arabic('MMDLXX')
        self.assertEqual(2570, res)

    def test_MMDLXXI(self):
        res = convert_to_arabic('MMDLXXI')
        self.assertEqual(2571, res)

    def test_MMDLXXII(self):
        res = convert_to_arabic('MMDLXXII')
        self.assertEqual(2572, res)

    def test_MMDLXXIII(self):
        res = convert_to_arabic('MMDLXXIII')
        self.assertEqual(2573, res)

    def test_MMDLXXIV(self):
        res = convert_to_arabic('MMDLXXIV')
        self.assertEqual(2574, res)

    def test_MMDLXXV(self):
        res = convert_to_arabic('MMDLXXV')
        self.assertEqual(2575, res)

    def test_MMDLXXVI(self):
        res = convert_to_arabic('MMDLXXVI')
        self.assertEqual(2576, res)

    def test_MMDLXXVII(self):
        res = convert_to_arabic('MMDLXXVII')
        self.assertEqual(2577, res)

    def test_MMDLXXVIII(self):
        res = convert_to_arabic('MMDLXXVIII')
        self.assertEqual(2578, res)

    def test_MMDLXXIX(self):
        res = convert_to_arabic('MMDLXXIX')
        self.assertEqual(2579, res)

    def test_MMDLXXX(self):
        res = convert_to_arabic('MMDLXXX')
        self.assertEqual(2580, res)

    def test_MMDLXXXI(self):
        res = convert_to_arabic('MMDLXXXI')
        self.assertEqual(2581, res)

    def test_MMDLXXXII(self):
        res = convert_to_arabic('MMDLXXXII')
        self.assertEqual(2582, res)

    def test_MMDLXXXIII(self):
        res = convert_to_arabic('MMDLXXXIII')
        self.assertEqual(2583, res)

    def test_MMDLXXXIV(self):
        res = convert_to_arabic('MMDLXXXIV')
        self.assertEqual(2584, res)

    def test_MMDLXXXV(self):
        res = convert_to_arabic('MMDLXXXV')
        self.assertEqual(2585, res)

    def test_MMDLXXXVI(self):
        res = convert_to_arabic('MMDLXXXVI')
        self.assertEqual(2586, res)

    def test_MMDLXXXVII(self):
        res = convert_to_arabic('MMDLXXXVII')
        self.assertEqual(2587, res)

    def test_MMDLXXXVIII(self):
        res = convert_to_arabic('MMDLXXXVIII')
        self.assertEqual(2588, res)

    def test_MMDLXXXIX(self):
        res = convert_to_arabic('MMDLXXXIX')
        self.assertEqual(2589, res)

    def test_MMDXC(self):
        res = convert_to_arabic('MMDXC')
        self.assertEqual(2590, res)

    def test_MMDXCI(self):
        res = convert_to_arabic('MMDXCI')
        self.assertEqual(2591, res)

    def test_MMDXCII(self):
        res = convert_to_arabic('MMDXCII')
        self.assertEqual(2592, res)

    def test_MMDXCIII(self):
        res = convert_to_arabic('MMDXCIII')
        self.assertEqual(2593, res)

    def test_MMDXCIV(self):
        res = convert_to_arabic('MMDXCIV')
        self.assertEqual(2594, res)

    def test_MMDXCV(self):
        res = convert_to_arabic('MMDXCV')
        self.assertEqual(2595, res)

    def test_MMDXCVI(self):
        res = convert_to_arabic('MMDXCVI')
        self.assertEqual(2596, res)

    def test_MMDXCVII(self):
        res = convert_to_arabic('MMDXCVII')
        self.assertEqual(2597, res)

    def test_MMDXCVIII(self):
        res = convert_to_arabic('MMDXCVIII')
        self.assertEqual(2598, res)

    def test_MMDXCIX(self):
        res = convert_to_arabic('MMDXCIX')
        self.assertEqual(2599, res)

    def test_MMDC(self):
        res = convert_to_arabic('MMDC')
        self.assertEqual(2600, res)

    def test_MMDCI(self):
        res = convert_to_arabic('MMDCI')
        self.assertEqual(2601, res)

    def test_MMDCII(self):
        res = convert_to_arabic('MMDCII')
        self.assertEqual(2602, res)

    def test_MMDCIII(self):
        res = convert_to_arabic('MMDCIII')
        self.assertEqual(2603, res)

    def test_MMDCIV(self):
        res = convert_to_arabic('MMDCIV')
        self.assertEqual(2604, res)

    def test_MMDCV(self):
        res = convert_to_arabic('MMDCV')
        self.assertEqual(2605, res)

    def test_MMDCVI(self):
        res = convert_to_arabic('MMDCVI')
        self.assertEqual(2606, res)

    def test_MMDCVII(self):
        res = convert_to_arabic('MMDCVII')
        self.assertEqual(2607, res)

    def test_MMDCVIII(self):
        res = convert_to_arabic('MMDCVIII')
        self.assertEqual(2608, res)

    def test_MMDCIX(self):
        res = convert_to_arabic('MMDCIX')
        self.assertEqual(2609, res)

    def test_MMDCX(self):
        res = convert_to_arabic('MMDCX')
        self.assertEqual(2610, res)

    def test_MMDCXI(self):
        res = convert_to_arabic('MMDCXI')
        self.assertEqual(2611, res)

    def test_MMDCXII(self):
        res = convert_to_arabic('MMDCXII')
        self.assertEqual(2612, res)

    def test_MMDCXIII(self):
        res = convert_to_arabic('MMDCXIII')
        self.assertEqual(2613, res)

    def test_MMDCXIV(self):
        res = convert_to_arabic('MMDCXIV')
        self.assertEqual(2614, res)

    def test_MMDCXV(self):
        res = convert_to_arabic('MMDCXV')
        self.assertEqual(2615, res)

    def test_MMDCXVI(self):
        res = convert_to_arabic('MMDCXVI')
        self.assertEqual(2616, res)

    def test_MMDCXVII(self):
        res = convert_to_arabic('MMDCXVII')
        self.assertEqual(2617, res)

    def test_MMDCXVIII(self):
        res = convert_to_arabic('MMDCXVIII')
        self.assertEqual(2618, res)

    def test_MMDCXIX(self):
        res = convert_to_arabic('MMDCXIX')
        self.assertEqual(2619, res)

    def test_MMDCXX(self):
        res = convert_to_arabic('MMDCXX')
        self.assertEqual(2620, res)

    def test_MMDCXXI(self):
        res = convert_to_arabic('MMDCXXI')
        self.assertEqual(2621, res)

    def test_MMDCXXII(self):
        res = convert_to_arabic('MMDCXXII')
        self.assertEqual(2622, res)

    def test_MMDCXXIII(self):
        res = convert_to_arabic('MMDCXXIII')
        self.assertEqual(2623, res)

    def test_MMDCXXIV(self):
        res = convert_to_arabic('MMDCXXIV')
        self.assertEqual(2624, res)

    def test_MMDCXXV(self):
        res = convert_to_arabic('MMDCXXV')
        self.assertEqual(2625, res)

    def test_MMDCXXVI(self):
        res = convert_to_arabic('MMDCXXVI')
        self.assertEqual(2626, res)

    def test_MMDCXXVII(self):
        res = convert_to_arabic('MMDCXXVII')
        self.assertEqual(2627, res)

    def test_MMDCXXVIII(self):
        res = convert_to_arabic('MMDCXXVIII')
        self.assertEqual(2628, res)

    def test_MMDCXXIX(self):
        res = convert_to_arabic('MMDCXXIX')
        self.assertEqual(2629, res)

    def test_MMDCXXX(self):
        res = convert_to_arabic('MMDCXXX')
        self.assertEqual(2630, res)

    def test_MMDCXXXI(self):
        res = convert_to_arabic('MMDCXXXI')
        self.assertEqual(2631, res)

    def test_MMDCXXXII(self):
        res = convert_to_arabic('MMDCXXXII')
        self.assertEqual(2632, res)

    def test_MMDCXXXIII(self):
        res = convert_to_arabic('MMDCXXXIII')
        self.assertEqual(2633, res)

    def test_MMDCXXXIV(self):
        res = convert_to_arabic('MMDCXXXIV')
        self.assertEqual(2634, res)

    def test_MMDCXXXV(self):
        res = convert_to_arabic('MMDCXXXV')
        self.assertEqual(2635, res)

    def test_MMDCXXXVI(self):
        res = convert_to_arabic('MMDCXXXVI')
        self.assertEqual(2636, res)

    def test_MMDCXXXVII(self):
        res = convert_to_arabic('MMDCXXXVII')
        self.assertEqual(2637, res)

    def test_MMDCXXXVIII(self):
        res = convert_to_arabic('MMDCXXXVIII')
        self.assertEqual(2638, res)

    def test_MMDCXXXIX(self):
        res = convert_to_arabic('MMDCXXXIX')
        self.assertEqual(2639, res)

    def test_MMDCXL(self):
        res = convert_to_arabic('MMDCXL')
        self.assertEqual(2640, res)

    def test_MMDCXLI(self):
        res = convert_to_arabic('MMDCXLI')
        self.assertEqual(2641, res)

    def test_MMDCXLII(self):
        res = convert_to_arabic('MMDCXLII')
        self.assertEqual(2642, res)

    def test_MMDCXLIII(self):
        res = convert_to_arabic('MMDCXLIII')
        self.assertEqual(2643, res)

    def test_MMDCXLIV(self):
        res = convert_to_arabic('MMDCXLIV')
        self.assertEqual(2644, res)

    def test_MMDCXLV(self):
        res = convert_to_arabic('MMDCXLV')
        self.assertEqual(2645, res)

    def test_MMDCXLVI(self):
        res = convert_to_arabic('MMDCXLVI')
        self.assertEqual(2646, res)

    def test_MMDCXLVII(self):
        res = convert_to_arabic('MMDCXLVII')
        self.assertEqual(2647, res)

    def test_MMDCXLVIII(self):
        res = convert_to_arabic('MMDCXLVIII')
        self.assertEqual(2648, res)

    def test_MMDCXLIX(self):
        res = convert_to_arabic('MMDCXLIX')
        self.assertEqual(2649, res)

    def test_MMDCL(self):
        res = convert_to_arabic('MMDCL')
        self.assertEqual(2650, res)

    def test_MMDCLI(self):
        res = convert_to_arabic('MMDCLI')
        self.assertEqual(2651, res)

    def test_MMDCLII(self):
        res = convert_to_arabic('MMDCLII')
        self.assertEqual(2652, res)

    def test_MMDCLIII(self):
        res = convert_to_arabic('MMDCLIII')
        self.assertEqual(2653, res)

    def test_MMDCLIV(self):
        res = convert_to_arabic('MMDCLIV')
        self.assertEqual(2654, res)

    def test_MMDCLV(self):
        res = convert_to_arabic('MMDCLV')
        self.assertEqual(2655, res)

    def test_MMDCLVI(self):
        res = convert_to_arabic('MMDCLVI')
        self.assertEqual(2656, res)

    def test_MMDCLVII(self):
        res = convert_to_arabic('MMDCLVII')
        self.assertEqual(2657, res)

    def test_MMDCLVIII(self):
        res = convert_to_arabic('MMDCLVIII')
        self.assertEqual(2658, res)

    def test_MMDCLIX(self):
        res = convert_to_arabic('MMDCLIX')
        self.assertEqual(2659, res)

    def test_MMDCLX(self):
        res = convert_to_arabic('MMDCLX')
        self.assertEqual(2660, res)

    def test_MMDCLXI(self):
        res = convert_to_arabic('MMDCLXI')
        self.assertEqual(2661, res)

    def test_MMDCLXII(self):
        res = convert_to_arabic('MMDCLXII')
        self.assertEqual(2662, res)

    def test_MMDCLXIII(self):
        res = convert_to_arabic('MMDCLXIII')
        self.assertEqual(2663, res)

    def test_MMDCLXIV(self):
        res = convert_to_arabic('MMDCLXIV')
        self.assertEqual(2664, res)

    def test_MMDCLXV(self):
        res = convert_to_arabic('MMDCLXV')
        self.assertEqual(2665, res)

    def test_MMDCLXVI(self):
        res = convert_to_arabic('MMDCLXVI')
        self.assertEqual(2666, res)

    def test_MMDCLXVII(self):
        res = convert_to_arabic('MMDCLXVII')
        self.assertEqual(2667, res)

    def test_MMDCLXVIII(self):
        res = convert_to_arabic('MMDCLXVIII')
        self.assertEqual(2668, res)

    def test_MMDCLXIX(self):
        res = convert_to_arabic('MMDCLXIX')
        self.assertEqual(2669, res)

    def test_MMDCLXX(self):
        res = convert_to_arabic('MMDCLXX')
        self.assertEqual(2670, res)

    def test_MMDCLXXI(self):
        res = convert_to_arabic('MMDCLXXI')
        self.assertEqual(2671, res)

    def test_MMDCLXXII(self):
        res = convert_to_arabic('MMDCLXXII')
        self.assertEqual(2672, res)

    def test_MMDCLXXIII(self):
        res = convert_to_arabic('MMDCLXXIII')
        self.assertEqual(2673, res)

    def test_MMDCLXXIV(self):
        res = convert_to_arabic('MMDCLXXIV')
        self.assertEqual(2674, res)

    def test_MMDCLXXV(self):
        res = convert_to_arabic('MMDCLXXV')
        self.assertEqual(2675, res)

    def test_MMDCLXXVI(self):
        res = convert_to_arabic('MMDCLXXVI')
        self.assertEqual(2676, res)

    def test_MMDCLXXVII(self):
        res = convert_to_arabic('MMDCLXXVII')
        self.assertEqual(2677, res)

    def test_MMDCLXXVIII(self):
        res = convert_to_arabic('MMDCLXXVIII')
        self.assertEqual(2678, res)

    def test_MMDCLXXIX(self):
        res = convert_to_arabic('MMDCLXXIX')
        self.assertEqual(2679, res)

    def test_MMDCLXXX(self):
        res = convert_to_arabic('MMDCLXXX')
        self.assertEqual(2680, res)

    def test_MMDCLXXXI(self):
        res = convert_to_arabic('MMDCLXXXI')
        self.assertEqual(2681, res)

    def test_MMDCLXXXII(self):
        res = convert_to_arabic('MMDCLXXXII')
        self.assertEqual(2682, res)

    def test_MMDCLXXXIII(self):
        res = convert_to_arabic('MMDCLXXXIII')
        self.assertEqual(2683, res)

    def test_MMDCLXXXIV(self):
        res = convert_to_arabic('MMDCLXXXIV')
        self.assertEqual(2684, res)

    def test_MMDCLXXXV(self):
        res = convert_to_arabic('MMDCLXXXV')
        self.assertEqual(2685, res)

    def test_MMDCLXXXVI(self):
        res = convert_to_arabic('MMDCLXXXVI')
        self.assertEqual(2686, res)

    def test_MMDCLXXXVII(self):
        res = convert_to_arabic('MMDCLXXXVII')
        self.assertEqual(2687, res)

    def test_MMDCLXXXVIII(self):
        res = convert_to_arabic('MMDCLXXXVIII')
        self.assertEqual(2688, res)

    def test_MMDCLXXXIX(self):
        res = convert_to_arabic('MMDCLXXXIX')
        self.assertEqual(2689, res)

    def test_MMDCXC(self):
        res = convert_to_arabic('MMDCXC')
        self.assertEqual(2690, res)

    def test_MMDCXCI(self):
        res = convert_to_arabic('MMDCXCI')
        self.assertEqual(2691, res)

    def test_MMDCXCII(self):
        res = convert_to_arabic('MMDCXCII')
        self.assertEqual(2692, res)

    def test_MMDCXCIII(self):
        res = convert_to_arabic('MMDCXCIII')
        self.assertEqual(2693, res)

    def test_MMDCXCIV(self):
        res = convert_to_arabic('MMDCXCIV')
        self.assertEqual(2694, res)

    def test_MMDCXCV(self):
        res = convert_to_arabic('MMDCXCV')
        self.assertEqual(2695, res)

    def test_MMDCXCVI(self):
        res = convert_to_arabic('MMDCXCVI')
        self.assertEqual(2696, res)

    def test_MMDCXCVII(self):
        res = convert_to_arabic('MMDCXCVII')
        self.assertEqual(2697, res)

    def test_MMDCXCVIII(self):
        res = convert_to_arabic('MMDCXCVIII')
        self.assertEqual(2698, res)

    def test_MMDCXCIX(self):
        res = convert_to_arabic('MMDCXCIX')
        self.assertEqual(2699, res)

    def test_MMDCC(self):
        res = convert_to_arabic('MMDCC')
        self.assertEqual(2700, res)

    def test_MMDCCI(self):
        res = convert_to_arabic('MMDCCI')
        self.assertEqual(2701, res)

    def test_MMDCCII(self):
        res = convert_to_arabic('MMDCCII')
        self.assertEqual(2702, res)

    def test_MMDCCIII(self):
        res = convert_to_arabic('MMDCCIII')
        self.assertEqual(2703, res)

    def test_MMDCCIV(self):
        res = convert_to_arabic('MMDCCIV')
        self.assertEqual(2704, res)

    def test_MMDCCV(self):
        res = convert_to_arabic('MMDCCV')
        self.assertEqual(2705, res)

    def test_MMDCCVI(self):
        res = convert_to_arabic('MMDCCVI')
        self.assertEqual(2706, res)

    def test_MMDCCVII(self):
        res = convert_to_arabic('MMDCCVII')
        self.assertEqual(2707, res)

    def test_MMDCCVIII(self):
        res = convert_to_arabic('MMDCCVIII')
        self.assertEqual(2708, res)

    def test_MMDCCIX(self):
        res = convert_to_arabic('MMDCCIX')
        self.assertEqual(2709, res)

    def test_MMDCCX(self):
        res = convert_to_arabic('MMDCCX')
        self.assertEqual(2710, res)

    def test_MMDCCXI(self):
        res = convert_to_arabic('MMDCCXI')
        self.assertEqual(2711, res)

    def test_MMDCCXII(self):
        res = convert_to_arabic('MMDCCXII')
        self.assertEqual(2712, res)

    def test_MMDCCXIII(self):
        res = convert_to_arabic('MMDCCXIII')
        self.assertEqual(2713, res)

    def test_MMDCCXIV(self):
        res = convert_to_arabic('MMDCCXIV')
        self.assertEqual(2714, res)

    def test_MMDCCXV(self):
        res = convert_to_arabic('MMDCCXV')
        self.assertEqual(2715, res)

    def test_MMDCCXVI(self):
        res = convert_to_arabic('MMDCCXVI')
        self.assertEqual(2716, res)

    def test_MMDCCXVII(self):
        res = convert_to_arabic('MMDCCXVII')
        self.assertEqual(2717, res)

    def test_MMDCCXVIII(self):
        res = convert_to_arabic('MMDCCXVIII')
        self.assertEqual(2718, res)

    def test_MMDCCXIX(self):
        res = convert_to_arabic('MMDCCXIX')
        self.assertEqual(2719, res)

    def test_MMDCCXX(self):
        res = convert_to_arabic('MMDCCXX')
        self.assertEqual(2720, res)

    def test_MMDCCXXI(self):
        res = convert_to_arabic('MMDCCXXI')
        self.assertEqual(2721, res)

    def test_MMDCCXXII(self):
        res = convert_to_arabic('MMDCCXXII')
        self.assertEqual(2722, res)

    def test_MMDCCXXIII(self):
        res = convert_to_arabic('MMDCCXXIII')
        self.assertEqual(2723, res)

    def test_MMDCCXXIV(self):
        res = convert_to_arabic('MMDCCXXIV')
        self.assertEqual(2724, res)

    def test_MMDCCXXV(self):
        res = convert_to_arabic('MMDCCXXV')
        self.assertEqual(2725, res)

    def test_MMDCCXXVI(self):
        res = convert_to_arabic('MMDCCXXVI')
        self.assertEqual(2726, res)

    def test_MMDCCXXVII(self):
        res = convert_to_arabic('MMDCCXXVII')
        self.assertEqual(2727, res)

    def test_MMDCCXXVIII(self):
        res = convert_to_arabic('MMDCCXXVIII')
        self.assertEqual(2728, res)

    def test_MMDCCXXIX(self):
        res = convert_to_arabic('MMDCCXXIX')
        self.assertEqual(2729, res)

    def test_MMDCCXXX(self):
        res = convert_to_arabic('MMDCCXXX')
        self.assertEqual(2730, res)

    def test_MMDCCXXXI(self):
        res = convert_to_arabic('MMDCCXXXI')
        self.assertEqual(2731, res)

    def test_MMDCCXXXII(self):
        res = convert_to_arabic('MMDCCXXXII')
        self.assertEqual(2732, res)

    def test_MMDCCXXXIII(self):
        res = convert_to_arabic('MMDCCXXXIII')
        self.assertEqual(2733, res)

    def test_MMDCCXXXIV(self):
        res = convert_to_arabic('MMDCCXXXIV')
        self.assertEqual(2734, res)

    def test_MMDCCXXXV(self):
        res = convert_to_arabic('MMDCCXXXV')
        self.assertEqual(2735, res)

    def test_MMDCCXXXVI(self):
        res = convert_to_arabic('MMDCCXXXVI')
        self.assertEqual(2736, res)

    def test_MMDCCXXXVII(self):
        res = convert_to_arabic('MMDCCXXXVII')
        self.assertEqual(2737, res)

    def test_MMDCCXXXVIII(self):
        res = convert_to_arabic('MMDCCXXXVIII')
        self.assertEqual(2738, res)

    def test_MMDCCXXXIX(self):
        res = convert_to_arabic('MMDCCXXXIX')
        self.assertEqual(2739, res)

    def test_MMDCCXL(self):
        res = convert_to_arabic('MMDCCXL')
        self.assertEqual(2740, res)

    def test_MMDCCXLI(self):
        res = convert_to_arabic('MMDCCXLI')
        self.assertEqual(2741, res)

    def test_MMDCCXLII(self):
        res = convert_to_arabic('MMDCCXLII')
        self.assertEqual(2742, res)

    def test_MMDCCXLIII(self):
        res = convert_to_arabic('MMDCCXLIII')
        self.assertEqual(2743, res)

    def test_MMDCCXLIV(self):
        res = convert_to_arabic('MMDCCXLIV')
        self.assertEqual(2744, res)

    def test_MMDCCXLV(self):
        res = convert_to_arabic('MMDCCXLV')
        self.assertEqual(2745, res)

    def test_MMDCCXLVI(self):
        res = convert_to_arabic('MMDCCXLVI')
        self.assertEqual(2746, res)

    def test_MMDCCXLVII(self):
        res = convert_to_arabic('MMDCCXLVII')
        self.assertEqual(2747, res)

    def test_MMDCCXLVIII(self):
        res = convert_to_arabic('MMDCCXLVIII')
        self.assertEqual(2748, res)

    def test_MMDCCXLIX(self):
        res = convert_to_arabic('MMDCCXLIX')
        self.assertEqual(2749, res)

    def test_MMDCCL(self):
        res = convert_to_arabic('MMDCCL')
        self.assertEqual(2750, res)

    def test_MMDCCLI(self):
        res = convert_to_arabic('MMDCCLI')
        self.assertEqual(2751, res)

    def test_MMDCCLII(self):
        res = convert_to_arabic('MMDCCLII')
        self.assertEqual(2752, res)

    def test_MMDCCLIII(self):
        res = convert_to_arabic('MMDCCLIII')
        self.assertEqual(2753, res)

    def test_MMDCCLIV(self):
        res = convert_to_arabic('MMDCCLIV')
        self.assertEqual(2754, res)

    def test_MMDCCLV(self):
        res = convert_to_arabic('MMDCCLV')
        self.assertEqual(2755, res)

    def test_MMDCCLVI(self):
        res = convert_to_arabic('MMDCCLVI')
        self.assertEqual(2756, res)

    def test_MMDCCLVII(self):
        res = convert_to_arabic('MMDCCLVII')
        self.assertEqual(2757, res)

    def test_MMDCCLVIII(self):
        res = convert_to_arabic('MMDCCLVIII')
        self.assertEqual(2758, res)

    def test_MMDCCLIX(self):
        res = convert_to_arabic('MMDCCLIX')
        self.assertEqual(2759, res)

    def test_MMDCCLX(self):
        res = convert_to_arabic('MMDCCLX')
        self.assertEqual(2760, res)

    def test_MMDCCLXI(self):
        res = convert_to_arabic('MMDCCLXI')
        self.assertEqual(2761, res)

    def test_MMDCCLXII(self):
        res = convert_to_arabic('MMDCCLXII')
        self.assertEqual(2762, res)

    def test_MMDCCLXIII(self):
        res = convert_to_arabic('MMDCCLXIII')
        self.assertEqual(2763, res)

    def test_MMDCCLXIV(self):
        res = convert_to_arabic('MMDCCLXIV')
        self.assertEqual(2764, res)

    def test_MMDCCLXV(self):
        res = convert_to_arabic('MMDCCLXV')
        self.assertEqual(2765, res)

    def test_MMDCCLXVI(self):
        res = convert_to_arabic('MMDCCLXVI')
        self.assertEqual(2766, res)

    def test_MMDCCLXVII(self):
        res = convert_to_arabic('MMDCCLXVII')
        self.assertEqual(2767, res)

    def test_MMDCCLXVIII(self):
        res = convert_to_arabic('MMDCCLXVIII')
        self.assertEqual(2768, res)

    def test_MMDCCLXIX(self):
        res = convert_to_arabic('MMDCCLXIX')
        self.assertEqual(2769, res)

    def test_MMDCCLXX(self):
        res = convert_to_arabic('MMDCCLXX')
        self.assertEqual(2770, res)

    def test_MMDCCLXXI(self):
        res = convert_to_arabic('MMDCCLXXI')
        self.assertEqual(2771, res)

    def test_MMDCCLXXII(self):
        res = convert_to_arabic('MMDCCLXXII')
        self.assertEqual(2772, res)

    def test_MMDCCLXXIII(self):
        res = convert_to_arabic('MMDCCLXXIII')
        self.assertEqual(2773, res)

    def test_MMDCCLXXIV(self):
        res = convert_to_arabic('MMDCCLXXIV')
        self.assertEqual(2774, res)

    def test_MMDCCLXXV(self):
        res = convert_to_arabic('MMDCCLXXV')
        self.assertEqual(2775, res)

    def test_MMDCCLXXVI(self):
        res = convert_to_arabic('MMDCCLXXVI')
        self.assertEqual(2776, res)

    def test_MMDCCLXXVII(self):
        res = convert_to_arabic('MMDCCLXXVII')
        self.assertEqual(2777, res)

    def test_MMDCCLXXVIII(self):
        res = convert_to_arabic('MMDCCLXXVIII')
        self.assertEqual(2778, res)

    def test_MMDCCLXXIX(self):
        res = convert_to_arabic('MMDCCLXXIX')
        self.assertEqual(2779, res)

    def test_MMDCCLXXX(self):
        res = convert_to_arabic('MMDCCLXXX')
        self.assertEqual(2780, res)

    def test_MMDCCLXXXI(self):
        res = convert_to_arabic('MMDCCLXXXI')
        self.assertEqual(2781, res)

    def test_MMDCCLXXXII(self):
        res = convert_to_arabic('MMDCCLXXXII')
        self.assertEqual(2782, res)

    def test_MMDCCLXXXIII(self):
        res = convert_to_arabic('MMDCCLXXXIII')
        self.assertEqual(2783, res)

    def test_MMDCCLXXXIV(self):
        res = convert_to_arabic('MMDCCLXXXIV')
        self.assertEqual(2784, res)

    def test_MMDCCLXXXV(self):
        res = convert_to_arabic('MMDCCLXXXV')
        self.assertEqual(2785, res)

    def test_MMDCCLXXXVI(self):
        res = convert_to_arabic('MMDCCLXXXVI')
        self.assertEqual(2786, res)

    def test_MMDCCLXXXVII(self):
        res = convert_to_arabic('MMDCCLXXXVII')
        self.assertEqual(2787, res)

    def test_MMDCCLXXXVIII(self):
        res = convert_to_arabic('MMDCCLXXXVIII')
        self.assertEqual(2788, res)

    def test_MMDCCLXXXIX(self):
        res = convert_to_arabic('MMDCCLXXXIX')
        self.assertEqual(2789, res)

    def test_MMDCCXC(self):
        res = convert_to_arabic('MMDCCXC')
        self.assertEqual(2790, res)

    def test_MMDCCXCI(self):
        res = convert_to_arabic('MMDCCXCI')
        self.assertEqual(2791, res)

    def test_MMDCCXCII(self):
        res = convert_to_arabic('MMDCCXCII')
        self.assertEqual(2792, res)

    def test_MMDCCXCIII(self):
        res = convert_to_arabic('MMDCCXCIII')
        self.assertEqual(2793, res)

    def test_MMDCCXCIV(self):
        res = convert_to_arabic('MMDCCXCIV')
        self.assertEqual(2794, res)

    def test_MMDCCXCV(self):
        res = convert_to_arabic('MMDCCXCV')
        self.assertEqual(2795, res)

    def test_MMDCCXCVI(self):
        res = convert_to_arabic('MMDCCXCVI')
        self.assertEqual(2796, res)

    def test_MMDCCXCVII(self):
        res = convert_to_arabic('MMDCCXCVII')
        self.assertEqual(2797, res)

    def test_MMDCCXCVIII(self):
        res = convert_to_arabic('MMDCCXCVIII')
        self.assertEqual(2798, res)

    def test_MMDCCXCIX(self):
        res = convert_to_arabic('MMDCCXCIX')
        self.assertEqual(2799, res)

    def test_MMDCCC(self):
        res = convert_to_arabic('MMDCCC')
        self.assertEqual(2800, res)

    def test_MMDCCCI(self):
        res = convert_to_arabic('MMDCCCI')
        self.assertEqual(2801, res)

    def test_MMDCCCII(self):
        res = convert_to_arabic('MMDCCCII')
        self.assertEqual(2802, res)

    def test_MMDCCCIII(self):
        res = convert_to_arabic('MMDCCCIII')
        self.assertEqual(2803, res)

    def test_MMDCCCIV(self):
        res = convert_to_arabic('MMDCCCIV')
        self.assertEqual(2804, res)

    def test_MMDCCCV(self):
        res = convert_to_arabic('MMDCCCV')
        self.assertEqual(2805, res)

    def test_MMDCCCVI(self):
        res = convert_to_arabic('MMDCCCVI')
        self.assertEqual(2806, res)

    def test_MMDCCCVII(self):
        res = convert_to_arabic('MMDCCCVII')
        self.assertEqual(2807, res)

    def test_MMDCCCVIII(self):
        res = convert_to_arabic('MMDCCCVIII')
        self.assertEqual(2808, res)

    def test_MMDCCCIX(self):
        res = convert_to_arabic('MMDCCCIX')
        self.assertEqual(2809, res)

    def test_MMDCCCX(self):
        res = convert_to_arabic('MMDCCCX')
        self.assertEqual(2810, res)

    def test_MMDCCCXI(self):
        res = convert_to_arabic('MMDCCCXI')
        self.assertEqual(2811, res)

    def test_MMDCCCXII(self):
        res = convert_to_arabic('MMDCCCXII')
        self.assertEqual(2812, res)

    def test_MMDCCCXIII(self):
        res = convert_to_arabic('MMDCCCXIII')
        self.assertEqual(2813, res)

    def test_MMDCCCXIV(self):
        res = convert_to_arabic('MMDCCCXIV')
        self.assertEqual(2814, res)

    def test_MMDCCCXV(self):
        res = convert_to_arabic('MMDCCCXV')
        self.assertEqual(2815, res)

    def test_MMDCCCXVI(self):
        res = convert_to_arabic('MMDCCCXVI')
        self.assertEqual(2816, res)

    def test_MMDCCCXVII(self):
        res = convert_to_arabic('MMDCCCXVII')
        self.assertEqual(2817, res)

    def test_MMDCCCXVIII(self):
        res = convert_to_arabic('MMDCCCXVIII')
        self.assertEqual(2818, res)

    def test_MMDCCCXIX(self):
        res = convert_to_arabic('MMDCCCXIX')
        self.assertEqual(2819, res)

    def test_MMDCCCXX(self):
        res = convert_to_arabic('MMDCCCXX')
        self.assertEqual(2820, res)

    def test_MMDCCCXXI(self):
        res = convert_to_arabic('MMDCCCXXI')
        self.assertEqual(2821, res)

    def test_MMDCCCXXII(self):
        res = convert_to_arabic('MMDCCCXXII')
        self.assertEqual(2822, res)

    def test_MMDCCCXXIII(self):
        res = convert_to_arabic('MMDCCCXXIII')
        self.assertEqual(2823, res)

    def test_MMDCCCXXIV(self):
        res = convert_to_arabic('MMDCCCXXIV')
        self.assertEqual(2824, res)

    def test_MMDCCCXXV(self):
        res = convert_to_arabic('MMDCCCXXV')
        self.assertEqual(2825, res)

    def test_MMDCCCXXVI(self):
        res = convert_to_arabic('MMDCCCXXVI')
        self.assertEqual(2826, res)

    def test_MMDCCCXXVII(self):
        res = convert_to_arabic('MMDCCCXXVII')
        self.assertEqual(2827, res)

    def test_MMDCCCXXVIII(self):
        res = convert_to_arabic('MMDCCCXXVIII')
        self.assertEqual(2828, res)

    def test_MMDCCCXXIX(self):
        res = convert_to_arabic('MMDCCCXXIX')
        self.assertEqual(2829, res)

    def test_MMDCCCXXX(self):
        res = convert_to_arabic('MMDCCCXXX')
        self.assertEqual(2830, res)

    def test_MMDCCCXXXI(self):
        res = convert_to_arabic('MMDCCCXXXI')
        self.assertEqual(2831, res)

    def test_MMDCCCXXXII(self):
        res = convert_to_arabic('MMDCCCXXXII')
        self.assertEqual(2832, res)

    def test_MMDCCCXXXIII(self):
        res = convert_to_arabic('MMDCCCXXXIII')
        self.assertEqual(2833, res)

    def test_MMDCCCXXXIV(self):
        res = convert_to_arabic('MMDCCCXXXIV')
        self.assertEqual(2834, res)

    def test_MMDCCCXXXV(self):
        res = convert_to_arabic('MMDCCCXXXV')
        self.assertEqual(2835, res)

    def test_MMDCCCXXXVI(self):
        res = convert_to_arabic('MMDCCCXXXVI')
        self.assertEqual(2836, res)

    def test_MMDCCCXXXVII(self):
        res = convert_to_arabic('MMDCCCXXXVII')
        self.assertEqual(2837, res)

    def test_MMDCCCXXXVIII(self):
        res = convert_to_arabic('MMDCCCXXXVIII')
        self.assertEqual(2838, res)

    def test_MMDCCCXXXIX(self):
        res = convert_to_arabic('MMDCCCXXXIX')
        self.assertEqual(2839, res)

    def test_MMDCCCXL(self):
        res = convert_to_arabic('MMDCCCXL')
        self.assertEqual(2840, res)

    def test_MMDCCCXLI(self):
        res = convert_to_arabic('MMDCCCXLI')
        self.assertEqual(2841, res)

    def test_MMDCCCXLII(self):
        res = convert_to_arabic('MMDCCCXLII')
        self.assertEqual(2842, res)

    def test_MMDCCCXLIII(self):
        res = convert_to_arabic('MMDCCCXLIII')
        self.assertEqual(2843, res)

    def test_MMDCCCXLIV(self):
        res = convert_to_arabic('MMDCCCXLIV')
        self.assertEqual(2844, res)

    def test_MMDCCCXLV(self):
        res = convert_to_arabic('MMDCCCXLV')
        self.assertEqual(2845, res)

    def test_MMDCCCXLVI(self):
        res = convert_to_arabic('MMDCCCXLVI')
        self.assertEqual(2846, res)

    def test_MMDCCCXLVII(self):
        res = convert_to_arabic('MMDCCCXLVII')
        self.assertEqual(2847, res)

    def test_MMDCCCXLVIII(self):
        res = convert_to_arabic('MMDCCCXLVIII')
        self.assertEqual(2848, res)

    def test_MMDCCCXLIX(self):
        res = convert_to_arabic('MMDCCCXLIX')
        self.assertEqual(2849, res)

    def test_MMDCCCL(self):
        res = convert_to_arabic('MMDCCCL')
        self.assertEqual(2850, res)

    def test_MMDCCCLI(self):
        res = convert_to_arabic('MMDCCCLI')
        self.assertEqual(2851, res)

    def test_MMDCCCLII(self):
        res = convert_to_arabic('MMDCCCLII')
        self.assertEqual(2852, res)

    def test_MMDCCCLIII(self):
        res = convert_to_arabic('MMDCCCLIII')
        self.assertEqual(2853, res)

    def test_MMDCCCLIV(self):
        res = convert_to_arabic('MMDCCCLIV')
        self.assertEqual(2854, res)

    def test_MMDCCCLV(self):
        res = convert_to_arabic('MMDCCCLV')
        self.assertEqual(2855, res)

    def test_MMDCCCLVI(self):
        res = convert_to_arabic('MMDCCCLVI')
        self.assertEqual(2856, res)

    def test_MMDCCCLVII(self):
        res = convert_to_arabic('MMDCCCLVII')
        self.assertEqual(2857, res)

    def test_MMDCCCLVIII(self):
        res = convert_to_arabic('MMDCCCLVIII')
        self.assertEqual(2858, res)

    def test_MMDCCCLIX(self):
        res = convert_to_arabic('MMDCCCLIX')
        self.assertEqual(2859, res)

    def test_MMDCCCLX(self):
        res = convert_to_arabic('MMDCCCLX')
        self.assertEqual(2860, res)

    def test_MMDCCCLXI(self):
        res = convert_to_arabic('MMDCCCLXI')
        self.assertEqual(2861, res)

    def test_MMDCCCLXII(self):
        res = convert_to_arabic('MMDCCCLXII')
        self.assertEqual(2862, res)

    def test_MMDCCCLXIII(self):
        res = convert_to_arabic('MMDCCCLXIII')
        self.assertEqual(2863, res)

    def test_MMDCCCLXIV(self):
        res = convert_to_arabic('MMDCCCLXIV')
        self.assertEqual(2864, res)

    def test_MMDCCCLXV(self):
        res = convert_to_arabic('MMDCCCLXV')
        self.assertEqual(2865, res)

    def test_MMDCCCLXVI(self):
        res = convert_to_arabic('MMDCCCLXVI')
        self.assertEqual(2866, res)

    def test_MMDCCCLXVII(self):
        res = convert_to_arabic('MMDCCCLXVII')
        self.assertEqual(2867, res)

    def test_MMDCCCLXVIII(self):
        res = convert_to_arabic('MMDCCCLXVIII')
        self.assertEqual(2868, res)

    def test_MMDCCCLXIX(self):
        res = convert_to_arabic('MMDCCCLXIX')
        self.assertEqual(2869, res)

    def test_MMDCCCLXX(self):
        res = convert_to_arabic('MMDCCCLXX')
        self.assertEqual(2870, res)

    def test_MMDCCCLXXI(self):
        res = convert_to_arabic('MMDCCCLXXI')
        self.assertEqual(2871, res)

    def test_MMDCCCLXXII(self):
        res = convert_to_arabic('MMDCCCLXXII')
        self.assertEqual(2872, res)

    def test_MMDCCCLXXIII(self):
        res = convert_to_arabic('MMDCCCLXXIII')
        self.assertEqual(2873, res)

    def test_MMDCCCLXXIV(self):
        res = convert_to_arabic('MMDCCCLXXIV')
        self.assertEqual(2874, res)

    def test_MMDCCCLXXV(self):
        res = convert_to_arabic('MMDCCCLXXV')
        self.assertEqual(2875, res)

    def test_MMDCCCLXXVI(self):
        res = convert_to_arabic('MMDCCCLXXVI')
        self.assertEqual(2876, res)

    def test_MMDCCCLXXVII(self):
        res = convert_to_arabic('MMDCCCLXXVII')
        self.assertEqual(2877, res)

    def test_MMDCCCLXXVIII(self):
        res = convert_to_arabic('MMDCCCLXXVIII')
        self.assertEqual(2878, res)

    def test_MMDCCCLXXIX(self):
        res = convert_to_arabic('MMDCCCLXXIX')
        self.assertEqual(2879, res)

    def test_MMDCCCLXXX(self):
        res = convert_to_arabic('MMDCCCLXXX')
        self.assertEqual(2880, res)

    def test_MMDCCCLXXXI(self):
        res = convert_to_arabic('MMDCCCLXXXI')
        self.assertEqual(2881, res)

    def test_MMDCCCLXXXII(self):
        res = convert_to_arabic('MMDCCCLXXXII')
        self.assertEqual(2882, res)

    def test_MMDCCCLXXXIII(self):
        res = convert_to_arabic('MMDCCCLXXXIII')
        self.assertEqual(2883, res)

    def test_MMDCCCLXXXIV(self):
        res = convert_to_arabic('MMDCCCLXXXIV')
        self.assertEqual(2884, res)

    def test_MMDCCCLXXXV(self):
        res = convert_to_arabic('MMDCCCLXXXV')
        self.assertEqual(2885, res)

    def test_MMDCCCLXXXVI(self):
        res = convert_to_arabic('MMDCCCLXXXVI')
        self.assertEqual(2886, res)

    def test_MMDCCCLXXXVII(self):
        res = convert_to_arabic('MMDCCCLXXXVII')
        self.assertEqual(2887, res)

    def test_MMDCCCLXXXVIII(self):
        res = convert_to_arabic('MMDCCCLXXXVIII')
        self.assertEqual(2888, res)

    def test_MMDCCCLXXXIX(self):
        res = convert_to_arabic('MMDCCCLXXXIX')
        self.assertEqual(2889, res)

    def test_MMDCCCXC(self):
        res = convert_to_arabic('MMDCCCXC')
        self.assertEqual(2890, res)

    def test_MMDCCCXCI(self):
        res = convert_to_arabic('MMDCCCXCI')
        self.assertEqual(2891, res)

    def test_MMDCCCXCII(self):
        res = convert_to_arabic('MMDCCCXCII')
        self.assertEqual(2892, res)

    def test_MMDCCCXCIII(self):
        res = convert_to_arabic('MMDCCCXCIII')
        self.assertEqual(2893, res)

    def test_MMDCCCXCIV(self):
        res = convert_to_arabic('MMDCCCXCIV')
        self.assertEqual(2894, res)

    def test_MMDCCCXCV(self):
        res = convert_to_arabic('MMDCCCXCV')
        self.assertEqual(2895, res)

    def test_MMDCCCXCVI(self):
        res = convert_to_arabic('MMDCCCXCVI')
        self.assertEqual(2896, res)

    def test_MMDCCCXCVII(self):
        res = convert_to_arabic('MMDCCCXCVII')
        self.assertEqual(2897, res)

    def test_MMDCCCXCVIII(self):
        res = convert_to_arabic('MMDCCCXCVIII')
        self.assertEqual(2898, res)

    def test_MMDCCCXCIX(self):
        res = convert_to_arabic('MMDCCCXCIX')
        self.assertEqual(2899, res)

    def test_MMCM(self):
        res = convert_to_arabic('MMCM')
        self.assertEqual(2900, res)

    def test_MMCMI(self):
        res = convert_to_arabic('MMCMI')
        self.assertEqual(2901, res)

    def test_MMCMII(self):
        res = convert_to_arabic('MMCMII')
        self.assertEqual(2902, res)

    def test_MMCMIII(self):
        res = convert_to_arabic('MMCMIII')
        self.assertEqual(2903, res)

    def test_MMCMIV(self):
        res = convert_to_arabic('MMCMIV')
        self.assertEqual(2904, res)

    def test_MMCMV(self):
        res = convert_to_arabic('MMCMV')
        self.assertEqual(2905, res)

    def test_MMCMVI(self):
        res = convert_to_arabic('MMCMVI')
        self.assertEqual(2906, res)

    def test_MMCMVII(self):
        res = convert_to_arabic('MMCMVII')
        self.assertEqual(2907, res)

    def test_MMCMVIII(self):
        res = convert_to_arabic('MMCMVIII')
        self.assertEqual(2908, res)

    def test_MMCMIX(self):
        res = convert_to_arabic('MMCMIX')
        self.assertEqual(2909, res)

    def test_MMCMX(self):
        res = convert_to_arabic('MMCMX')
        self.assertEqual(2910, res)

    def test_MMCMXI(self):
        res = convert_to_arabic('MMCMXI')
        self.assertEqual(2911, res)

    def test_MMCMXII(self):
        res = convert_to_arabic('MMCMXII')
        self.assertEqual(2912, res)

    def test_MMCMXIII(self):
        res = convert_to_arabic('MMCMXIII')
        self.assertEqual(2913, res)

    def test_MMCMXIV(self):
        res = convert_to_arabic('MMCMXIV')
        self.assertEqual(2914, res)

    def test_MMCMXV(self):
        res = convert_to_arabic('MMCMXV')
        self.assertEqual(2915, res)

    def test_MMCMXVI(self):
        res = convert_to_arabic('MMCMXVI')
        self.assertEqual(2916, res)

    def test_MMCMXVII(self):
        res = convert_to_arabic('MMCMXVII')
        self.assertEqual(2917, res)

    def test_MMCMXVIII(self):
        res = convert_to_arabic('MMCMXVIII')
        self.assertEqual(2918, res)

    def test_MMCMXIX(self):
        res = convert_to_arabic('MMCMXIX')
        self.assertEqual(2919, res)

    def test_MMCMXX(self):
        res = convert_to_arabic('MMCMXX')
        self.assertEqual(2920, res)

    def test_MMCMXXI(self):
        res = convert_to_arabic('MMCMXXI')
        self.assertEqual(2921, res)

    def test_MMCMXXII(self):
        res = convert_to_arabic('MMCMXXII')
        self.assertEqual(2922, res)

    def test_MMCMXXIII(self):
        res = convert_to_arabic('MMCMXXIII')
        self.assertEqual(2923, res)

    def test_MMCMXXIV(self):
        res = convert_to_arabic('MMCMXXIV')
        self.assertEqual(2924, res)

    def test_MMCMXXV(self):
        res = convert_to_arabic('MMCMXXV')
        self.assertEqual(2925, res)

    def test_MMCMXXVI(self):
        res = convert_to_arabic('MMCMXXVI')
        self.assertEqual(2926, res)

    def test_MMCMXXVII(self):
        res = convert_to_arabic('MMCMXXVII')
        self.assertEqual(2927, res)

    def test_MMCMXXVIII(self):
        res = convert_to_arabic('MMCMXXVIII')
        self.assertEqual(2928, res)

    def test_MMCMXXIX(self):
        res = convert_to_arabic('MMCMXXIX')
        self.assertEqual(2929, res)

    def test_MMCMXXX(self):
        res = convert_to_arabic('MMCMXXX')
        self.assertEqual(2930, res)

    def test_MMCMXXXI(self):
        res = convert_to_arabic('MMCMXXXI')
        self.assertEqual(2931, res)

    def test_MMCMXXXII(self):
        res = convert_to_arabic('MMCMXXXII')
        self.assertEqual(2932, res)

    def test_MMCMXXXIII(self):
        res = convert_to_arabic('MMCMXXXIII')
        self.assertEqual(2933, res)

    def test_MMCMXXXIV(self):
        res = convert_to_arabic('MMCMXXXIV')
        self.assertEqual(2934, res)

    def test_MMCMXXXV(self):
        res = convert_to_arabic('MMCMXXXV')
        self.assertEqual(2935, res)

    def test_MMCMXXXVI(self):
        res = convert_to_arabic('MMCMXXXVI')
        self.assertEqual(2936, res)

    def test_MMCMXXXVII(self):
        res = convert_to_arabic('MMCMXXXVII')
        self.assertEqual(2937, res)

    def test_MMCMXXXVIII(self):
        res = convert_to_arabic('MMCMXXXVIII')
        self.assertEqual(2938, res)

    def test_MMCMXXXIX(self):
        res = convert_to_arabic('MMCMXXXIX')
        self.assertEqual(2939, res)

    def test_MMCMXL(self):
        res = convert_to_arabic('MMCMXL')
        self.assertEqual(2940, res)

    def test_MMCMXLI(self):
        res = convert_to_arabic('MMCMXLI')
        self.assertEqual(2941, res)

    def test_MMCMXLII(self):
        res = convert_to_arabic('MMCMXLII')
        self.assertEqual(2942, res)

    def test_MMCMXLIII(self):
        res = convert_to_arabic('MMCMXLIII')
        self.assertEqual(2943, res)

    def test_MMCMXLIV(self):
        res = convert_to_arabic('MMCMXLIV')
        self.assertEqual(2944, res)

    def test_MMCMXLV(self):
        res = convert_to_arabic('MMCMXLV')
        self.assertEqual(2945, res)

    def test_MMCMXLVI(self):
        res = convert_to_arabic('MMCMXLVI')
        self.assertEqual(2946, res)

    def test_MMCMXLVII(self):
        res = convert_to_arabic('MMCMXLVII')
        self.assertEqual(2947, res)

    def test_MMCMXLVIII(self):
        res = convert_to_arabic('MMCMXLVIII')
        self.assertEqual(2948, res)

    def test_MMCMXLIX(self):
        res = convert_to_arabic('MMCMXLIX')
        self.assertEqual(2949, res)

    def test_MMCML(self):
        res = convert_to_arabic('MMCML')
        self.assertEqual(2950, res)

    def test_MMCMLI(self):
        res = convert_to_arabic('MMCMLI')
        self.assertEqual(2951, res)

    def test_MMCMLII(self):
        res = convert_to_arabic('MMCMLII')
        self.assertEqual(2952, res)

    def test_MMCMLIII(self):
        res = convert_to_arabic('MMCMLIII')
        self.assertEqual(2953, res)

    def test_MMCMLIV(self):
        res = convert_to_arabic('MMCMLIV')
        self.assertEqual(2954, res)

    def test_MMCMLV(self):
        res = convert_to_arabic('MMCMLV')
        self.assertEqual(2955, res)

    def test_MMCMLVI(self):
        res = convert_to_arabic('MMCMLVI')
        self.assertEqual(2956, res)

    def test_MMCMLVII(self):
        res = convert_to_arabic('MMCMLVII')
        self.assertEqual(2957, res)

    def test_MMCMLVIII(self):
        res = convert_to_arabic('MMCMLVIII')
        self.assertEqual(2958, res)

    def test_MMCMLIX(self):
        res = convert_to_arabic('MMCMLIX')
        self.assertEqual(2959, res)

    def test_MMCMLX(self):
        res = convert_to_arabic('MMCMLX')
        self.assertEqual(2960, res)

    def test_MMCMLXI(self):
        res = convert_to_arabic('MMCMLXI')
        self.assertEqual(2961, res)

    def test_MMCMLXII(self):
        res = convert_to_arabic('MMCMLXII')
        self.assertEqual(2962, res)

    def test_MMCMLXIII(self):
        res = convert_to_arabic('MMCMLXIII')
        self.assertEqual(2963, res)

    def test_MMCMLXIV(self):
        res = convert_to_arabic('MMCMLXIV')
        self.assertEqual(2964, res)

    def test_MMCMLXV(self):
        res = convert_to_arabic('MMCMLXV')
        self.assertEqual(2965, res)

    def test_MMCMLXVI(self):
        res = convert_to_arabic('MMCMLXVI')
        self.assertEqual(2966, res)

    def test_MMCMLXVII(self):
        res = convert_to_arabic('MMCMLXVII')
        self.assertEqual(2967, res)

    def test_MMCMLXVIII(self):
        res = convert_to_arabic('MMCMLXVIII')
        self.assertEqual(2968, res)

    def test_MMCMLXIX(self):
        res = convert_to_arabic('MMCMLXIX')
        self.assertEqual(2969, res)

    def test_MMCMLXX(self):
        res = convert_to_arabic('MMCMLXX')
        self.assertEqual(2970, res)

    def test_MMCMLXXI(self):
        res = convert_to_arabic('MMCMLXXI')
        self.assertEqual(2971, res)

    def test_MMCMLXXII(self):
        res = convert_to_arabic('MMCMLXXII')
        self.assertEqual(2972, res)

    def test_MMCMLXXIII(self):
        res = convert_to_arabic('MMCMLXXIII')
        self.assertEqual(2973, res)

    def test_MMCMLXXIV(self):
        res = convert_to_arabic('MMCMLXXIV')
        self.assertEqual(2974, res)

    def test_MMCMLXXV(self):
        res = convert_to_arabic('MMCMLXXV')
        self.assertEqual(2975, res)

    def test_MMCMLXXVI(self):
        res = convert_to_arabic('MMCMLXXVI')
        self.assertEqual(2976, res)

    def test_MMCMLXXVII(self):
        res = convert_to_arabic('MMCMLXXVII')
        self.assertEqual(2977, res)

    def test_MMCMLXXVIII(self):
        res = convert_to_arabic('MMCMLXXVIII')
        self.assertEqual(2978, res)

    def test_MMCMLXXIX(self):
        res = convert_to_arabic('MMCMLXXIX')
        self.assertEqual(2979, res)

    def test_MMCMLXXX(self):
        res = convert_to_arabic('MMCMLXXX')
        self.assertEqual(2980, res)

    def test_MMCMLXXXI(self):
        res = convert_to_arabic('MMCMLXXXI')
        self.assertEqual(2981, res)

    def test_MMCMLXXXII(self):
        res = convert_to_arabic('MMCMLXXXII')
        self.assertEqual(2982, res)

    def test_MMCMLXXXIII(self):
        res = convert_to_arabic('MMCMLXXXIII')
        self.assertEqual(2983, res)

    def test_MMCMLXXXIV(self):
        res = convert_to_arabic('MMCMLXXXIV')
        self.assertEqual(2984, res)

    def test_MMCMLXXXV(self):
        res = convert_to_arabic('MMCMLXXXV')
        self.assertEqual(2985, res)

    def test_MMCMLXXXVI(self):
        res = convert_to_arabic('MMCMLXXXVI')
        self.assertEqual(2986, res)

    def test_MMCMLXXXVII(self):
        res = convert_to_arabic('MMCMLXXXVII')
        self.assertEqual(2987, res)

    def test_MMCMLXXXVIII(self):
        res = convert_to_arabic('MMCMLXXXVIII')
        self.assertEqual(2988, res)

    def test_MMCMLXXXIX(self):
        res = convert_to_arabic('MMCMLXXXIX')
        self.assertEqual(2989, res)

    def test_MMCMXC(self):
        res = convert_to_arabic('MMCMXC')
        self.assertEqual(2990, res)

    def test_MMCMXCI(self):
        res = convert_to_arabic('MMCMXCI')
        self.assertEqual(2991, res)

    def test_MMCMXCII(self):
        res = convert_to_arabic('MMCMXCII')
        self.assertEqual(2992, res)

    def test_MMCMXCIII(self):
        res = convert_to_arabic('MMCMXCIII')
        self.assertEqual(2993, res)

    def test_MMCMXCIV(self):
        res = convert_to_arabic('MMCMXCIV')
        self.assertEqual(2994, res)

    def test_MMCMXCV(self):
        res = convert_to_arabic('MMCMXCV')
        self.assertEqual(2995, res)

    def test_MMCMXCVI(self):
        res = convert_to_arabic('MMCMXCVI')
        self.assertEqual(2996, res)

    def test_MMCMXCVII(self):
        res = convert_to_arabic('MMCMXCVII')
        self.assertEqual(2997, res)

    def test_MMCMXCVIII(self):
        res = convert_to_arabic('MMCMXCVIII')
        self.assertEqual(2998, res)

    def test_MMCMXCIX(self):
        res = convert_to_arabic('MMCMXCIX')
        self.assertEqual(2999, res)

    def test_MMM(self):
        res = convert_to_arabic('MMM')
        self.assertEqual(3000, res)

    def test_MMMI(self):
        res = convert_to_arabic('MMMI')
        self.assertEqual(3001, res)

    def test_MMMII(self):
        res = convert_to_arabic('MMMII')
        self.assertEqual(3002, res)

    def test_MMMIII(self):
        res = convert_to_arabic('MMMIII')
        self.assertEqual(3003, res)

    def test_MMMIV(self):
        res = convert_to_arabic('MMMIV')
        self.assertEqual(3004, res)

    def test_MMMV(self):
        res = convert_to_arabic('MMMV')
        self.assertEqual(3005, res)

    def test_MMMVI(self):
        res = convert_to_arabic('MMMVI')
        self.assertEqual(3006, res)

    def test_MMMVII(self):
        res = convert_to_arabic('MMMVII')
        self.assertEqual(3007, res)

    def test_MMMVIII(self):
        res = convert_to_arabic('MMMVIII')
        self.assertEqual(3008, res)

    def test_MMMIX(self):
        res = convert_to_arabic('MMMIX')
        self.assertEqual(3009, res)

    def test_MMMX(self):
        res = convert_to_arabic('MMMX')
        self.assertEqual(3010, res)

    def test_MMMXI(self):
        res = convert_to_arabic('MMMXI')
        self.assertEqual(3011, res)

    def test_MMMXII(self):
        res = convert_to_arabic('MMMXII')
        self.assertEqual(3012, res)

    def test_MMMXIII(self):
        res = convert_to_arabic('MMMXIII')
        self.assertEqual(3013, res)

    def test_MMMXIV(self):
        res = convert_to_arabic('MMMXIV')
        self.assertEqual(3014, res)

    def test_MMMXV(self):
        res = convert_to_arabic('MMMXV')
        self.assertEqual(3015, res)

    def test_MMMXVI(self):
        res = convert_to_arabic('MMMXVI')
        self.assertEqual(3016, res)

    def test_MMMXVII(self):
        res = convert_to_arabic('MMMXVII')
        self.assertEqual(3017, res)

    def test_MMMXVIII(self):
        res = convert_to_arabic('MMMXVIII')
        self.assertEqual(3018, res)

    def test_MMMXIX(self):
        res = convert_to_arabic('MMMXIX')
        self.assertEqual(3019, res)

    def test_MMMXX(self):
        res = convert_to_arabic('MMMXX')
        self.assertEqual(3020, res)

    def test_MMMXXI(self):
        res = convert_to_arabic('MMMXXI')
        self.assertEqual(3021, res)

    def test_MMMXXII(self):
        res = convert_to_arabic('MMMXXII')
        self.assertEqual(3022, res)

    def test_MMMXXIII(self):
        res = convert_to_arabic('MMMXXIII')
        self.assertEqual(3023, res)

    def test_MMMXXIV(self):
        res = convert_to_arabic('MMMXXIV')
        self.assertEqual(3024, res)

    def test_MMMXXV(self):
        res = convert_to_arabic('MMMXXV')
        self.assertEqual(3025, res)

    def test_MMMXXVI(self):
        res = convert_to_arabic('MMMXXVI')
        self.assertEqual(3026, res)

    def test_MMMXXVII(self):
        res = convert_to_arabic('MMMXXVII')
        self.assertEqual(3027, res)

    def test_MMMXXVIII(self):
        res = convert_to_arabic('MMMXXVIII')
        self.assertEqual(3028, res)

    def test_MMMXXIX(self):
        res = convert_to_arabic('MMMXXIX')
        self.assertEqual(3029, res)

    def test_MMMXXX(self):
        res = convert_to_arabic('MMMXXX')
        self.assertEqual(3030, res)

    def test_MMMXXXI(self):
        res = convert_to_arabic('MMMXXXI')
        self.assertEqual(3031, res)

    def test_MMMXXXII(self):
        res = convert_to_arabic('MMMXXXII')
        self.assertEqual(3032, res)

    def test_MMMXXXIII(self):
        res = convert_to_arabic('MMMXXXIII')
        self.assertEqual(3033, res)

    def test_MMMXXXIV(self):
        res = convert_to_arabic('MMMXXXIV')
        self.assertEqual(3034, res)

    def test_MMMXXXV(self):
        res = convert_to_arabic('MMMXXXV')
        self.assertEqual(3035, res)

    def test_MMMXXXVI(self):
        res = convert_to_arabic('MMMXXXVI')
        self.assertEqual(3036, res)

    def test_MMMXXXVII(self):
        res = convert_to_arabic('MMMXXXVII')
        self.assertEqual(3037, res)

    def test_MMMXXXVIII(self):
        res = convert_to_arabic('MMMXXXVIII')
        self.assertEqual(3038, res)

    def test_MMMXXXIX(self):
        res = convert_to_arabic('MMMXXXIX')
        self.assertEqual(3039, res)

    def test_MMMXL(self):
        res = convert_to_arabic('MMMXL')
        self.assertEqual(3040, res)

    def test_MMMXLI(self):
        res = convert_to_arabic('MMMXLI')
        self.assertEqual(3041, res)

    def test_MMMXLII(self):
        res = convert_to_arabic('MMMXLII')
        self.assertEqual(3042, res)

    def test_MMMXLIII(self):
        res = convert_to_arabic('MMMXLIII')
        self.assertEqual(3043, res)

    def test_MMMXLIV(self):
        res = convert_to_arabic('MMMXLIV')
        self.assertEqual(3044, res)

    def test_MMMXLV(self):
        res = convert_to_arabic('MMMXLV')
        self.assertEqual(3045, res)

    def test_MMMXLVI(self):
        res = convert_to_arabic('MMMXLVI')
        self.assertEqual(3046, res)

    def test_MMMXLVII(self):
        res = convert_to_arabic('MMMXLVII')
        self.assertEqual(3047, res)

    def test_MMMXLVIII(self):
        res = convert_to_arabic('MMMXLVIII')
        self.assertEqual(3048, res)

    def test_MMMXLIX(self):
        res = convert_to_arabic('MMMXLIX')
        self.assertEqual(3049, res)

    def test_MMML(self):
        res = convert_to_arabic('MMML')
        self.assertEqual(3050, res)

    def test_MMMLI(self):
        res = convert_to_arabic('MMMLI')
        self.assertEqual(3051, res)

    def test_MMMLII(self):
        res = convert_to_arabic('MMMLII')
        self.assertEqual(3052, res)

    def test_MMMLIII(self):
        res = convert_to_arabic('MMMLIII')
        self.assertEqual(3053, res)

    def test_MMMLIV(self):
        res = convert_to_arabic('MMMLIV')
        self.assertEqual(3054, res)

    def test_MMMLV(self):
        res = convert_to_arabic('MMMLV')
        self.assertEqual(3055, res)

    def test_MMMLVI(self):
        res = convert_to_arabic('MMMLVI')
        self.assertEqual(3056, res)

    def test_MMMLVII(self):
        res = convert_to_arabic('MMMLVII')
        self.assertEqual(3057, res)

    def test_MMMLVIII(self):
        res = convert_to_arabic('MMMLVIII')
        self.assertEqual(3058, res)

    def test_MMMLIX(self):
        res = convert_to_arabic('MMMLIX')
        self.assertEqual(3059, res)

    def test_MMMLX(self):
        res = convert_to_arabic('MMMLX')
        self.assertEqual(3060, res)

    def test_MMMLXI(self):
        res = convert_to_arabic('MMMLXI')
        self.assertEqual(3061, res)

    def test_MMMLXII(self):
        res = convert_to_arabic('MMMLXII')
        self.assertEqual(3062, res)

    def test_MMMLXIII(self):
        res = convert_to_arabic('MMMLXIII')
        self.assertEqual(3063, res)

    def test_MMMLXIV(self):
        res = convert_to_arabic('MMMLXIV')
        self.assertEqual(3064, res)

    def test_MMMLXV(self):
        res = convert_to_arabic('MMMLXV')
        self.assertEqual(3065, res)

    def test_MMMLXVI(self):
        res = convert_to_arabic('MMMLXVI')
        self.assertEqual(3066, res)

    def test_MMMLXVII(self):
        res = convert_to_arabic('MMMLXVII')
        self.assertEqual(3067, res)

    def test_MMMLXVIII(self):
        res = convert_to_arabic('MMMLXVIII')
        self.assertEqual(3068, res)

    def test_MMMLXIX(self):
        res = convert_to_arabic('MMMLXIX')
        self.assertEqual(3069, res)

    def test_MMMLXX(self):
        res = convert_to_arabic('MMMLXX')
        self.assertEqual(3070, res)

    def test_MMMLXXI(self):
        res = convert_to_arabic('MMMLXXI')
        self.assertEqual(3071, res)

    def test_MMMLXXII(self):
        res = convert_to_arabic('MMMLXXII')
        self.assertEqual(3072, res)

    def test_MMMLXXIII(self):
        res = convert_to_arabic('MMMLXXIII')
        self.assertEqual(3073, res)

    def test_MMMLXXIV(self):
        res = convert_to_arabic('MMMLXXIV')
        self.assertEqual(3074, res)

    def test_MMMLXXV(self):
        res = convert_to_arabic('MMMLXXV')
        self.assertEqual(3075, res)

    def test_MMMLXXVI(self):
        res = convert_to_arabic('MMMLXXVI')
        self.assertEqual(3076, res)

    def test_MMMLXXVII(self):
        res = convert_to_arabic('MMMLXXVII')
        self.assertEqual(3077, res)

    def test_MMMLXXVIII(self):
        res = convert_to_arabic('MMMLXXVIII')
        self.assertEqual(3078, res)

    def test_MMMLXXIX(self):
        res = convert_to_arabic('MMMLXXIX')
        self.assertEqual(3079, res)

    def test_MMMLXXX(self):
        res = convert_to_arabic('MMMLXXX')
        self.assertEqual(3080, res)

    def test_MMMLXXXI(self):
        res = convert_to_arabic('MMMLXXXI')
        self.assertEqual(3081, res)

    def test_MMMLXXXII(self):
        res = convert_to_arabic('MMMLXXXII')
        self.assertEqual(3082, res)

    def test_MMMLXXXIII(self):
        res = convert_to_arabic('MMMLXXXIII')
        self.assertEqual(3083, res)

    def test_MMMLXXXIV(self):
        res = convert_to_arabic('MMMLXXXIV')
        self.assertEqual(3084, res)

    def test_MMMLXXXV(self):
        res = convert_to_arabic('MMMLXXXV')
        self.assertEqual(3085, res)

    def test_MMMLXXXVI(self):
        res = convert_to_arabic('MMMLXXXVI')
        self.assertEqual(3086, res)

    def test_MMMLXXXVII(self):
        res = convert_to_arabic('MMMLXXXVII')
        self.assertEqual(3087, res)

    def test_MMMLXXXVIII(self):
        res = convert_to_arabic('MMMLXXXVIII')
        self.assertEqual(3088, res)

    def test_MMMLXXXIX(self):
        res = convert_to_arabic('MMMLXXXIX')
        self.assertEqual(3089, res)

    def test_MMMXC(self):
        res = convert_to_arabic('MMMXC')
        self.assertEqual(3090, res)

    def test_MMMXCI(self):
        res = convert_to_arabic('MMMXCI')
        self.assertEqual(3091, res)

    def test_MMMXCII(self):
        res = convert_to_arabic('MMMXCII')
        self.assertEqual(3092, res)

    def test_MMMXCIII(self):
        res = convert_to_arabic('MMMXCIII')
        self.assertEqual(3093, res)

    def test_MMMXCIV(self):
        res = convert_to_arabic('MMMXCIV')
        self.assertEqual(3094, res)

    def test_MMMXCV(self):
        res = convert_to_arabic('MMMXCV')
        self.assertEqual(3095, res)

    def test_MMMXCVI(self):
        res = convert_to_arabic('MMMXCVI')
        self.assertEqual(3096, res)

    def test_MMMXCVII(self):
        res = convert_to_arabic('MMMXCVII')
        self.assertEqual(3097, res)

    def test_MMMXCVIII(self):
        res = convert_to_arabic('MMMXCVIII')
        self.assertEqual(3098, res)

    def test_MMMXCIX(self):
        res = convert_to_arabic('MMMXCIX')
        self.assertEqual(3099, res)

    def test_MMMC(self):
        res = convert_to_arabic('MMMC')
        self.assertEqual(3100, res)

    def test_MMMCI(self):
        res = convert_to_arabic('MMMCI')
        self.assertEqual(3101, res)

    def test_MMMCII(self):
        res = convert_to_arabic('MMMCII')
        self.assertEqual(3102, res)

    def test_MMMCIII(self):
        res = convert_to_arabic('MMMCIII')
        self.assertEqual(3103, res)

    def test_MMMCIV(self):
        res = convert_to_arabic('MMMCIV')
        self.assertEqual(3104, res)

    def test_MMMCV(self):
        res = convert_to_arabic('MMMCV')
        self.assertEqual(3105, res)

    def test_MMMCVI(self):
        res = convert_to_arabic('MMMCVI')
        self.assertEqual(3106, res)

    def test_MMMCVII(self):
        res = convert_to_arabic('MMMCVII')
        self.assertEqual(3107, res)

    def test_MMMCVIII(self):
        res = convert_to_arabic('MMMCVIII')
        self.assertEqual(3108, res)

    def test_MMMCIX(self):
        res = convert_to_arabic('MMMCIX')
        self.assertEqual(3109, res)

    def test_MMMCX(self):
        res = convert_to_arabic('MMMCX')
        self.assertEqual(3110, res)

    def test_MMMCXI(self):
        res = convert_to_arabic('MMMCXI')
        self.assertEqual(3111, res)

    def test_MMMCXII(self):
        res = convert_to_arabic('MMMCXII')
        self.assertEqual(3112, res)

    def test_MMMCXIII(self):
        res = convert_to_arabic('MMMCXIII')
        self.assertEqual(3113, res)

    def test_MMMCXIV(self):
        res = convert_to_arabic('MMMCXIV')
        self.assertEqual(3114, res)

    def test_MMMCXV(self):
        res = convert_to_arabic('MMMCXV')
        self.assertEqual(3115, res)

    def test_MMMCXVI(self):
        res = convert_to_arabic('MMMCXVI')
        self.assertEqual(3116, res)

    def test_MMMCXVII(self):
        res = convert_to_arabic('MMMCXVII')
        self.assertEqual(3117, res)

    def test_MMMCXVIII(self):
        res = convert_to_arabic('MMMCXVIII')
        self.assertEqual(3118, res)

    def test_MMMCXIX(self):
        res = convert_to_arabic('MMMCXIX')
        self.assertEqual(3119, res)

    def test_MMMCXX(self):
        res = convert_to_arabic('MMMCXX')
        self.assertEqual(3120, res)

    def test_MMMCXXI(self):
        res = convert_to_arabic('MMMCXXI')
        self.assertEqual(3121, res)

    def test_MMMCXXII(self):
        res = convert_to_arabic('MMMCXXII')
        self.assertEqual(3122, res)

    def test_MMMCXXIII(self):
        res = convert_to_arabic('MMMCXXIII')
        self.assertEqual(3123, res)

    def test_MMMCXXIV(self):
        res = convert_to_arabic('MMMCXXIV')
        self.assertEqual(3124, res)

    def test_MMMCXXV(self):
        res = convert_to_arabic('MMMCXXV')
        self.assertEqual(3125, res)

    def test_MMMCXXVI(self):
        res = convert_to_arabic('MMMCXXVI')
        self.assertEqual(3126, res)

    def test_MMMCXXVII(self):
        res = convert_to_arabic('MMMCXXVII')
        self.assertEqual(3127, res)

    def test_MMMCXXVIII(self):
        res = convert_to_arabic('MMMCXXVIII')
        self.assertEqual(3128, res)

    def test_MMMCXXIX(self):
        res = convert_to_arabic('MMMCXXIX')
        self.assertEqual(3129, res)

    def test_MMMCXXX(self):
        res = convert_to_arabic('MMMCXXX')
        self.assertEqual(3130, res)

    def test_MMMCXXXI(self):
        res = convert_to_arabic('MMMCXXXI')
        self.assertEqual(3131, res)

    def test_MMMCXXXII(self):
        res = convert_to_arabic('MMMCXXXII')
        self.assertEqual(3132, res)

    def test_MMMCXXXIII(self):
        res = convert_to_arabic('MMMCXXXIII')
        self.assertEqual(3133, res)

    def test_MMMCXXXIV(self):
        res = convert_to_arabic('MMMCXXXIV')
        self.assertEqual(3134, res)

    def test_MMMCXXXV(self):
        res = convert_to_arabic('MMMCXXXV')
        self.assertEqual(3135, res)

    def test_MMMCXXXVI(self):
        res = convert_to_arabic('MMMCXXXVI')
        self.assertEqual(3136, res)

    def test_MMMCXXXVII(self):
        res = convert_to_arabic('MMMCXXXVII')
        self.assertEqual(3137, res)

    def test_MMMCXXXVIII(self):
        res = convert_to_arabic('MMMCXXXVIII')
        self.assertEqual(3138, res)

    def test_MMMCXXXIX(self):
        res = convert_to_arabic('MMMCXXXIX')
        self.assertEqual(3139, res)

    def test_MMMCXL(self):
        res = convert_to_arabic('MMMCXL')
        self.assertEqual(3140, res)

    def test_MMMCXLI(self):
        res = convert_to_arabic('MMMCXLI')
        self.assertEqual(3141, res)

    def test_MMMCXLII(self):
        res = convert_to_arabic('MMMCXLII')
        self.assertEqual(3142, res)

    def test_MMMCXLIII(self):
        res = convert_to_arabic('MMMCXLIII')
        self.assertEqual(3143, res)

    def test_MMMCXLIV(self):
        res = convert_to_arabic('MMMCXLIV')
        self.assertEqual(3144, res)

    def test_MMMCXLV(self):
        res = convert_to_arabic('MMMCXLV')
        self.assertEqual(3145, res)

    def test_MMMCXLVI(self):
        res = convert_to_arabic('MMMCXLVI')
        self.assertEqual(3146, res)

    def test_MMMCXLVII(self):
        res = convert_to_arabic('MMMCXLVII')
        self.assertEqual(3147, res)

    def test_MMMCXLVIII(self):
        res = convert_to_arabic('MMMCXLVIII')
        self.assertEqual(3148, res)

    def test_MMMCXLIX(self):
        res = convert_to_arabic('MMMCXLIX')
        self.assertEqual(3149, res)

    def test_MMMCL(self):
        res = convert_to_arabic('MMMCL')
        self.assertEqual(3150, res)

    def test_MMMCLI(self):
        res = convert_to_arabic('MMMCLI')
        self.assertEqual(3151, res)

    def test_MMMCLII(self):
        res = convert_to_arabic('MMMCLII')
        self.assertEqual(3152, res)

    def test_MMMCLIII(self):
        res = convert_to_arabic('MMMCLIII')
        self.assertEqual(3153, res)

    def test_MMMCLIV(self):
        res = convert_to_arabic('MMMCLIV')
        self.assertEqual(3154, res)

    def test_MMMCLV(self):
        res = convert_to_arabic('MMMCLV')
        self.assertEqual(3155, res)

    def test_MMMCLVI(self):
        res = convert_to_arabic('MMMCLVI')
        self.assertEqual(3156, res)

    def test_MMMCLVII(self):
        res = convert_to_arabic('MMMCLVII')
        self.assertEqual(3157, res)

    def test_MMMCLVIII(self):
        res = convert_to_arabic('MMMCLVIII')
        self.assertEqual(3158, res)

    def test_MMMCLIX(self):
        res = convert_to_arabic('MMMCLIX')
        self.assertEqual(3159, res)

    def test_MMMCLX(self):
        res = convert_to_arabic('MMMCLX')
        self.assertEqual(3160, res)

    def test_MMMCLXI(self):
        res = convert_to_arabic('MMMCLXI')
        self.assertEqual(3161, res)

    def test_MMMCLXII(self):
        res = convert_to_arabic('MMMCLXII')
        self.assertEqual(3162, res)

    def test_MMMCLXIII(self):
        res = convert_to_arabic('MMMCLXIII')
        self.assertEqual(3163, res)

    def test_MMMCLXIV(self):
        res = convert_to_arabic('MMMCLXIV')
        self.assertEqual(3164, res)

    def test_MMMCLXV(self):
        res = convert_to_arabic('MMMCLXV')
        self.assertEqual(3165, res)

    def test_MMMCLXVI(self):
        res = convert_to_arabic('MMMCLXVI')
        self.assertEqual(3166, res)

    def test_MMMCLXVII(self):
        res = convert_to_arabic('MMMCLXVII')
        self.assertEqual(3167, res)

    def test_MMMCLXVIII(self):
        res = convert_to_arabic('MMMCLXVIII')
        self.assertEqual(3168, res)

    def test_MMMCLXIX(self):
        res = convert_to_arabic('MMMCLXIX')
        self.assertEqual(3169, res)

    def test_MMMCLXX(self):
        res = convert_to_arabic('MMMCLXX')
        self.assertEqual(3170, res)

    def test_MMMCLXXI(self):
        res = convert_to_arabic('MMMCLXXI')
        self.assertEqual(3171, res)

    def test_MMMCLXXII(self):
        res = convert_to_arabic('MMMCLXXII')
        self.assertEqual(3172, res)

    def test_MMMCLXXIII(self):
        res = convert_to_arabic('MMMCLXXIII')
        self.assertEqual(3173, res)

    def test_MMMCLXXIV(self):
        res = convert_to_arabic('MMMCLXXIV')
        self.assertEqual(3174, res)

    def test_MMMCLXXV(self):
        res = convert_to_arabic('MMMCLXXV')
        self.assertEqual(3175, res)

    def test_MMMCLXXVI(self):
        res = convert_to_arabic('MMMCLXXVI')
        self.assertEqual(3176, res)

    def test_MMMCLXXVII(self):
        res = convert_to_arabic('MMMCLXXVII')
        self.assertEqual(3177, res)

    def test_MMMCLXXVIII(self):
        res = convert_to_arabic('MMMCLXXVIII')
        self.assertEqual(3178, res)

    def test_MMMCLXXIX(self):
        res = convert_to_arabic('MMMCLXXIX')
        self.assertEqual(3179, res)

    def test_MMMCLXXX(self):
        res = convert_to_arabic('MMMCLXXX')
        self.assertEqual(3180, res)

    def test_MMMCLXXXI(self):
        res = convert_to_arabic('MMMCLXXXI')
        self.assertEqual(3181, res)

    def test_MMMCLXXXII(self):
        res = convert_to_arabic('MMMCLXXXII')
        self.assertEqual(3182, res)

    def test_MMMCLXXXIII(self):
        res = convert_to_arabic('MMMCLXXXIII')
        self.assertEqual(3183, res)

    def test_MMMCLXXXIV(self):
        res = convert_to_arabic('MMMCLXXXIV')
        self.assertEqual(3184, res)

    def test_MMMCLXXXV(self):
        res = convert_to_arabic('MMMCLXXXV')
        self.assertEqual(3185, res)

    def test_MMMCLXXXVI(self):
        res = convert_to_arabic('MMMCLXXXVI')
        self.assertEqual(3186, res)

    def test_MMMCLXXXVII(self):
        res = convert_to_arabic('MMMCLXXXVII')
        self.assertEqual(3187, res)

    def test_MMMCLXXXVIII(self):
        res = convert_to_arabic('MMMCLXXXVIII')
        self.assertEqual(3188, res)

    def test_MMMCLXXXIX(self):
        res = convert_to_arabic('MMMCLXXXIX')
        self.assertEqual(3189, res)

    def test_MMMCXC(self):
        res = convert_to_arabic('MMMCXC')
        self.assertEqual(3190, res)

    def test_MMMCXCI(self):
        res = convert_to_arabic('MMMCXCI')
        self.assertEqual(3191, res)

    def test_MMMCXCII(self):
        res = convert_to_arabic('MMMCXCII')
        self.assertEqual(3192, res)

    def test_MMMCXCIII(self):
        res = convert_to_arabic('MMMCXCIII')
        self.assertEqual(3193, res)

    def test_MMMCXCIV(self):
        res = convert_to_arabic('MMMCXCIV')
        self.assertEqual(3194, res)

    def test_MMMCXCV(self):
        res = convert_to_arabic('MMMCXCV')
        self.assertEqual(3195, res)

    def test_MMMCXCVI(self):
        res = convert_to_arabic('MMMCXCVI')
        self.assertEqual(3196, res)

    def test_MMMCXCVII(self):
        res = convert_to_arabic('MMMCXCVII')
        self.assertEqual(3197, res)

    def test_MMMCXCVIII(self):
        res = convert_to_arabic('MMMCXCVIII')
        self.assertEqual(3198, res)

    def test_MMMCXCIX(self):
        res = convert_to_arabic('MMMCXCIX')
        self.assertEqual(3199, res)

    def test_MMMCC(self):
        res = convert_to_arabic('MMMCC')
        self.assertEqual(3200, res)

    def test_MMMCCI(self):
        res = convert_to_arabic('MMMCCI')
        self.assertEqual(3201, res)

    def test_MMMCCII(self):
        res = convert_to_arabic('MMMCCII')
        self.assertEqual(3202, res)

    def test_MMMCCIII(self):
        res = convert_to_arabic('MMMCCIII')
        self.assertEqual(3203, res)

    def test_MMMCCIV(self):
        res = convert_to_arabic('MMMCCIV')
        self.assertEqual(3204, res)

    def test_MMMCCV(self):
        res = convert_to_arabic('MMMCCV')
        self.assertEqual(3205, res)

    def test_MMMCCVI(self):
        res = convert_to_arabic('MMMCCVI')
        self.assertEqual(3206, res)

    def test_MMMCCVII(self):
        res = convert_to_arabic('MMMCCVII')
        self.assertEqual(3207, res)

    def test_MMMCCVIII(self):
        res = convert_to_arabic('MMMCCVIII')
        self.assertEqual(3208, res)

    def test_MMMCCIX(self):
        res = convert_to_arabic('MMMCCIX')
        self.assertEqual(3209, res)

    def test_MMMCCX(self):
        res = convert_to_arabic('MMMCCX')
        self.assertEqual(3210, res)

    def test_MMMCCXI(self):
        res = convert_to_arabic('MMMCCXI')
        self.assertEqual(3211, res)

    def test_MMMCCXII(self):
        res = convert_to_arabic('MMMCCXII')
        self.assertEqual(3212, res)

    def test_MMMCCXIII(self):
        res = convert_to_arabic('MMMCCXIII')
        self.assertEqual(3213, res)

    def test_MMMCCXIV(self):
        res = convert_to_arabic('MMMCCXIV')
        self.assertEqual(3214, res)

    def test_MMMCCXV(self):
        res = convert_to_arabic('MMMCCXV')
        self.assertEqual(3215, res)

    def test_MMMCCXVI(self):
        res = convert_to_arabic('MMMCCXVI')
        self.assertEqual(3216, res)

    def test_MMMCCXVII(self):
        res = convert_to_arabic('MMMCCXVII')
        self.assertEqual(3217, res)

    def test_MMMCCXVIII(self):
        res = convert_to_arabic('MMMCCXVIII')
        self.assertEqual(3218, res)

    def test_MMMCCXIX(self):
        res = convert_to_arabic('MMMCCXIX')
        self.assertEqual(3219, res)

    def test_MMMCCXX(self):
        res = convert_to_arabic('MMMCCXX')
        self.assertEqual(3220, res)

    def test_MMMCCXXI(self):
        res = convert_to_arabic('MMMCCXXI')
        self.assertEqual(3221, res)

    def test_MMMCCXXII(self):
        res = convert_to_arabic('MMMCCXXII')
        self.assertEqual(3222, res)

    def test_MMMCCXXIII(self):
        res = convert_to_arabic('MMMCCXXIII')
        self.assertEqual(3223, res)

    def test_MMMCCXXIV(self):
        res = convert_to_arabic('MMMCCXXIV')
        self.assertEqual(3224, res)

    def test_MMMCCXXV(self):
        res = convert_to_arabic('MMMCCXXV')
        self.assertEqual(3225, res)

    def test_MMMCCXXVI(self):
        res = convert_to_arabic('MMMCCXXVI')
        self.assertEqual(3226, res)

    def test_MMMCCXXVII(self):
        res = convert_to_arabic('MMMCCXXVII')
        self.assertEqual(3227, res)

    def test_MMMCCXXVIII(self):
        res = convert_to_arabic('MMMCCXXVIII')
        self.assertEqual(3228, res)

    def test_MMMCCXXIX(self):
        res = convert_to_arabic('MMMCCXXIX')
        self.assertEqual(3229, res)

    def test_MMMCCXXX(self):
        res = convert_to_arabic('MMMCCXXX')
        self.assertEqual(3230, res)

    def test_MMMCCXXXI(self):
        res = convert_to_arabic('MMMCCXXXI')
        self.assertEqual(3231, res)

    def test_MMMCCXXXII(self):
        res = convert_to_arabic('MMMCCXXXII')
        self.assertEqual(3232, res)

    def test_MMMCCXXXIII(self):
        res = convert_to_arabic('MMMCCXXXIII')
        self.assertEqual(3233, res)

    def test_MMMCCXXXIV(self):
        res = convert_to_arabic('MMMCCXXXIV')
        self.assertEqual(3234, res)

    def test_MMMCCXXXV(self):
        res = convert_to_arabic('MMMCCXXXV')
        self.assertEqual(3235, res)

    def test_MMMCCXXXVI(self):
        res = convert_to_arabic('MMMCCXXXVI')
        self.assertEqual(3236, res)

    def test_MMMCCXXXVII(self):
        res = convert_to_arabic('MMMCCXXXVII')
        self.assertEqual(3237, res)

    def test_MMMCCXXXVIII(self):
        res = convert_to_arabic('MMMCCXXXVIII')
        self.assertEqual(3238, res)

    def test_MMMCCXXXIX(self):
        res = convert_to_arabic('MMMCCXXXIX')
        self.assertEqual(3239, res)

    def test_MMMCCXL(self):
        res = convert_to_arabic('MMMCCXL')
        self.assertEqual(3240, res)

    def test_MMMCCXLI(self):
        res = convert_to_arabic('MMMCCXLI')
        self.assertEqual(3241, res)

    def test_MMMCCXLII(self):
        res = convert_to_arabic('MMMCCXLII')
        self.assertEqual(3242, res)

    def test_MMMCCXLIII(self):
        res = convert_to_arabic('MMMCCXLIII')
        self.assertEqual(3243, res)

    def test_MMMCCXLIV(self):
        res = convert_to_arabic('MMMCCXLIV')
        self.assertEqual(3244, res)

    def test_MMMCCXLV(self):
        res = convert_to_arabic('MMMCCXLV')
        self.assertEqual(3245, res)

    def test_MMMCCXLVI(self):
        res = convert_to_arabic('MMMCCXLVI')
        self.assertEqual(3246, res)

    def test_MMMCCXLVII(self):
        res = convert_to_arabic('MMMCCXLVII')
        self.assertEqual(3247, res)

    def test_MMMCCXLVIII(self):
        res = convert_to_arabic('MMMCCXLVIII')
        self.assertEqual(3248, res)

    def test_MMMCCXLIX(self):
        res = convert_to_arabic('MMMCCXLIX')
        self.assertEqual(3249, res)

    def test_MMMCCL(self):
        res = convert_to_arabic('MMMCCL')
        self.assertEqual(3250, res)

    def test_MMMCCLI(self):
        res = convert_to_arabic('MMMCCLI')
        self.assertEqual(3251, res)

    def test_MMMCCLII(self):
        res = convert_to_arabic('MMMCCLII')
        self.assertEqual(3252, res)

    def test_MMMCCLIII(self):
        res = convert_to_arabic('MMMCCLIII')
        self.assertEqual(3253, res)

    def test_MMMCCLIV(self):
        res = convert_to_arabic('MMMCCLIV')
        self.assertEqual(3254, res)

    def test_MMMCCLV(self):
        res = convert_to_arabic('MMMCCLV')
        self.assertEqual(3255, res)

    def test_MMMCCLVI(self):
        res = convert_to_arabic('MMMCCLVI')
        self.assertEqual(3256, res)

    def test_MMMCCLVII(self):
        res = convert_to_arabic('MMMCCLVII')
        self.assertEqual(3257, res)

    def test_MMMCCLVIII(self):
        res = convert_to_arabic('MMMCCLVIII')
        self.assertEqual(3258, res)

    def test_MMMCCLIX(self):
        res = convert_to_arabic('MMMCCLIX')
        self.assertEqual(3259, res)

    def test_MMMCCLX(self):
        res = convert_to_arabic('MMMCCLX')
        self.assertEqual(3260, res)

    def test_MMMCCLXI(self):
        res = convert_to_arabic('MMMCCLXI')
        self.assertEqual(3261, res)

    def test_MMMCCLXII(self):
        res = convert_to_arabic('MMMCCLXII')
        self.assertEqual(3262, res)

    def test_MMMCCLXIII(self):
        res = convert_to_arabic('MMMCCLXIII')
        self.assertEqual(3263, res)

    def test_MMMCCLXIV(self):
        res = convert_to_arabic('MMMCCLXIV')
        self.assertEqual(3264, res)

    def test_MMMCCLXV(self):
        res = convert_to_arabic('MMMCCLXV')
        self.assertEqual(3265, res)

    def test_MMMCCLXVI(self):
        res = convert_to_arabic('MMMCCLXVI')
        self.assertEqual(3266, res)

    def test_MMMCCLXVII(self):
        res = convert_to_arabic('MMMCCLXVII')
        self.assertEqual(3267, res)

    def test_MMMCCLXVIII(self):
        res = convert_to_arabic('MMMCCLXVIII')
        self.assertEqual(3268, res)

    def test_MMMCCLXIX(self):
        res = convert_to_arabic('MMMCCLXIX')
        self.assertEqual(3269, res)

    def test_MMMCCLXX(self):
        res = convert_to_arabic('MMMCCLXX')
        self.assertEqual(3270, res)

    def test_MMMCCLXXI(self):
        res = convert_to_arabic('MMMCCLXXI')
        self.assertEqual(3271, res)

    def test_MMMCCLXXII(self):
        res = convert_to_arabic('MMMCCLXXII')
        self.assertEqual(3272, res)

    def test_MMMCCLXXIII(self):
        res = convert_to_arabic('MMMCCLXXIII')
        self.assertEqual(3273, res)

    def test_MMMCCLXXIV(self):
        res = convert_to_arabic('MMMCCLXXIV')
        self.assertEqual(3274, res)

    def test_MMMCCLXXV(self):
        res = convert_to_arabic('MMMCCLXXV')
        self.assertEqual(3275, res)

    def test_MMMCCLXXVI(self):
        res = convert_to_arabic('MMMCCLXXVI')
        self.assertEqual(3276, res)

    def test_MMMCCLXXVII(self):
        res = convert_to_arabic('MMMCCLXXVII')
        self.assertEqual(3277, res)

    def test_MMMCCLXXVIII(self):
        res = convert_to_arabic('MMMCCLXXVIII')
        self.assertEqual(3278, res)

    def test_MMMCCLXXIX(self):
        res = convert_to_arabic('MMMCCLXXIX')
        self.assertEqual(3279, res)

    def test_MMMCCLXXX(self):
        res = convert_to_arabic('MMMCCLXXX')
        self.assertEqual(3280, res)

    def test_MMMCCLXXXI(self):
        res = convert_to_arabic('MMMCCLXXXI')
        self.assertEqual(3281, res)

    def test_MMMCCLXXXII(self):
        res = convert_to_arabic('MMMCCLXXXII')
        self.assertEqual(3282, res)

    def test_MMMCCLXXXIII(self):
        res = convert_to_arabic('MMMCCLXXXIII')
        self.assertEqual(3283, res)

    def test_MMMCCLXXXIV(self):
        res = convert_to_arabic('MMMCCLXXXIV')
        self.assertEqual(3284, res)

    def test_MMMCCLXXXV(self):
        res = convert_to_arabic('MMMCCLXXXV')
        self.assertEqual(3285, res)

    def test_MMMCCLXXXVI(self):
        res = convert_to_arabic('MMMCCLXXXVI')
        self.assertEqual(3286, res)

    def test_MMMCCLXXXVII(self):
        res = convert_to_arabic('MMMCCLXXXVII')
        self.assertEqual(3287, res)

    def test_MMMCCLXXXVIII(self):
        res = convert_to_arabic('MMMCCLXXXVIII')
        self.assertEqual(3288, res)

    def test_MMMCCLXXXIX(self):
        res = convert_to_arabic('MMMCCLXXXIX')
        self.assertEqual(3289, res)

    def test_MMMCCXC(self):
        res = convert_to_arabic('MMMCCXC')
        self.assertEqual(3290, res)

    def test_MMMCCXCI(self):
        res = convert_to_arabic('MMMCCXCI')
        self.assertEqual(3291, res)

    def test_MMMCCXCII(self):
        res = convert_to_arabic('MMMCCXCII')
        self.assertEqual(3292, res)

    def test_MMMCCXCIII(self):
        res = convert_to_arabic('MMMCCXCIII')
        self.assertEqual(3293, res)

    def test_MMMCCXCIV(self):
        res = convert_to_arabic('MMMCCXCIV')
        self.assertEqual(3294, res)

    def test_MMMCCXCV(self):
        res = convert_to_arabic('MMMCCXCV')
        self.assertEqual(3295, res)

    def test_MMMCCXCVI(self):
        res = convert_to_arabic('MMMCCXCVI')
        self.assertEqual(3296, res)

    def test_MMMCCXCVII(self):
        res = convert_to_arabic('MMMCCXCVII')
        self.assertEqual(3297, res)

    def test_MMMCCXCVIII(self):
        res = convert_to_arabic('MMMCCXCVIII')
        self.assertEqual(3298, res)

    def test_MMMCCXCIX(self):
        res = convert_to_arabic('MMMCCXCIX')
        self.assertEqual(3299, res)

    def test_MMMCCC(self):
        res = convert_to_arabic('MMMCCC')
        self.assertEqual(3300, res)

    def test_MMMCCCI(self):
        res = convert_to_arabic('MMMCCCI')
        self.assertEqual(3301, res)

    def test_MMMCCCII(self):
        res = convert_to_arabic('MMMCCCII')
        self.assertEqual(3302, res)

    def test_MMMCCCIII(self):
        res = convert_to_arabic('MMMCCCIII')
        self.assertEqual(3303, res)

    def test_MMMCCCIV(self):
        res = convert_to_arabic('MMMCCCIV')
        self.assertEqual(3304, res)

    def test_MMMCCCV(self):
        res = convert_to_arabic('MMMCCCV')
        self.assertEqual(3305, res)

    def test_MMMCCCVI(self):
        res = convert_to_arabic('MMMCCCVI')
        self.assertEqual(3306, res)

    def test_MMMCCCVII(self):
        res = convert_to_arabic('MMMCCCVII')
        self.assertEqual(3307, res)

    def test_MMMCCCVIII(self):
        res = convert_to_arabic('MMMCCCVIII')
        self.assertEqual(3308, res)

    def test_MMMCCCIX(self):
        res = convert_to_arabic('MMMCCCIX')
        self.assertEqual(3309, res)

    def test_MMMCCCX(self):
        res = convert_to_arabic('MMMCCCX')
        self.assertEqual(3310, res)

    def test_MMMCCCXI(self):
        res = convert_to_arabic('MMMCCCXI')
        self.assertEqual(3311, res)

    def test_MMMCCCXII(self):
        res = convert_to_arabic('MMMCCCXII')
        self.assertEqual(3312, res)

    def test_MMMCCCXIII(self):
        res = convert_to_arabic('MMMCCCXIII')
        self.assertEqual(3313, res)

    def test_MMMCCCXIV(self):
        res = convert_to_arabic('MMMCCCXIV')
        self.assertEqual(3314, res)

    def test_MMMCCCXV(self):
        res = convert_to_arabic('MMMCCCXV')
        self.assertEqual(3315, res)

    def test_MMMCCCXVI(self):
        res = convert_to_arabic('MMMCCCXVI')
        self.assertEqual(3316, res)

    def test_MMMCCCXVII(self):
        res = convert_to_arabic('MMMCCCXVII')
        self.assertEqual(3317, res)

    def test_MMMCCCXVIII(self):
        res = convert_to_arabic('MMMCCCXVIII')
        self.assertEqual(3318, res)

    def test_MMMCCCXIX(self):
        res = convert_to_arabic('MMMCCCXIX')
        self.assertEqual(3319, res)

    def test_MMMCCCXX(self):
        res = convert_to_arabic('MMMCCCXX')
        self.assertEqual(3320, res)

    def test_MMMCCCXXI(self):
        res = convert_to_arabic('MMMCCCXXI')
        self.assertEqual(3321, res)

    def test_MMMCCCXXII(self):
        res = convert_to_arabic('MMMCCCXXII')
        self.assertEqual(3322, res)

    def test_MMMCCCXXIII(self):
        res = convert_to_arabic('MMMCCCXXIII')
        self.assertEqual(3323, res)

    def test_MMMCCCXXIV(self):
        res = convert_to_arabic('MMMCCCXXIV')
        self.assertEqual(3324, res)

    def test_MMMCCCXXV(self):
        res = convert_to_arabic('MMMCCCXXV')
        self.assertEqual(3325, res)

    def test_MMMCCCXXVI(self):
        res = convert_to_arabic('MMMCCCXXVI')
        self.assertEqual(3326, res)

    def test_MMMCCCXXVII(self):
        res = convert_to_arabic('MMMCCCXXVII')
        self.assertEqual(3327, res)

    def test_MMMCCCXXVIII(self):
        res = convert_to_arabic('MMMCCCXXVIII')
        self.assertEqual(3328, res)

    def test_MMMCCCXXIX(self):
        res = convert_to_arabic('MMMCCCXXIX')
        self.assertEqual(3329, res)

    def test_MMMCCCXXX(self):
        res = convert_to_arabic('MMMCCCXXX')
        self.assertEqual(3330, res)

    def test_MMMCCCXXXI(self):
        res = convert_to_arabic('MMMCCCXXXI')
        self.assertEqual(3331, res)

    def test_MMMCCCXXXII(self):
        res = convert_to_arabic('MMMCCCXXXII')
        self.assertEqual(3332, res)

    def test_MMMCCCXXXIII(self):
        res = convert_to_arabic('MMMCCCXXXIII')
        self.assertEqual(3333, res)

    def test_MMMCCCXXXIV(self):
        res = convert_to_arabic('MMMCCCXXXIV')
        self.assertEqual(3334, res)

    def test_MMMCCCXXXV(self):
        res = convert_to_arabic('MMMCCCXXXV')
        self.assertEqual(3335, res)

    def test_MMMCCCXXXVI(self):
        res = convert_to_arabic('MMMCCCXXXVI')
        self.assertEqual(3336, res)

    def test_MMMCCCXXXVII(self):
        res = convert_to_arabic('MMMCCCXXXVII')
        self.assertEqual(3337, res)

    def test_MMMCCCXXXVIII(self):
        res = convert_to_arabic('MMMCCCXXXVIII')
        self.assertEqual(3338, res)

    def test_MMMCCCXXXIX(self):
        res = convert_to_arabic('MMMCCCXXXIX')
        self.assertEqual(3339, res)

    def test_MMMCCCXL(self):
        res = convert_to_arabic('MMMCCCXL')
        self.assertEqual(3340, res)

    def test_MMMCCCXLI(self):
        res = convert_to_arabic('MMMCCCXLI')
        self.assertEqual(3341, res)

    def test_MMMCCCXLII(self):
        res = convert_to_arabic('MMMCCCXLII')
        self.assertEqual(3342, res)

    def test_MMMCCCXLIII(self):
        res = convert_to_arabic('MMMCCCXLIII')
        self.assertEqual(3343, res)

    def test_MMMCCCXLIV(self):
        res = convert_to_arabic('MMMCCCXLIV')
        self.assertEqual(3344, res)

    def test_MMMCCCXLV(self):
        res = convert_to_arabic('MMMCCCXLV')
        self.assertEqual(3345, res)

    def test_MMMCCCXLVI(self):
        res = convert_to_arabic('MMMCCCXLVI')
        self.assertEqual(3346, res)

    def test_MMMCCCXLVII(self):
        res = convert_to_arabic('MMMCCCXLVII')
        self.assertEqual(3347, res)

    def test_MMMCCCXLVIII(self):
        res = convert_to_arabic('MMMCCCXLVIII')
        self.assertEqual(3348, res)

    def test_MMMCCCXLIX(self):
        res = convert_to_arabic('MMMCCCXLIX')
        self.assertEqual(3349, res)

    def test_MMMCCCL(self):
        res = convert_to_arabic('MMMCCCL')
        self.assertEqual(3350, res)

    def test_MMMCCCLI(self):
        res = convert_to_arabic('MMMCCCLI')
        self.assertEqual(3351, res)

    def test_MMMCCCLII(self):
        res = convert_to_arabic('MMMCCCLII')
        self.assertEqual(3352, res)

    def test_MMMCCCLIII(self):
        res = convert_to_arabic('MMMCCCLIII')
        self.assertEqual(3353, res)

    def test_MMMCCCLIV(self):
        res = convert_to_arabic('MMMCCCLIV')
        self.assertEqual(3354, res)

    def test_MMMCCCLV(self):
        res = convert_to_arabic('MMMCCCLV')
        self.assertEqual(3355, res)

    def test_MMMCCCLVI(self):
        res = convert_to_arabic('MMMCCCLVI')
        self.assertEqual(3356, res)

    def test_MMMCCCLVII(self):
        res = convert_to_arabic('MMMCCCLVII')
        self.assertEqual(3357, res)

    def test_MMMCCCLVIII(self):
        res = convert_to_arabic('MMMCCCLVIII')
        self.assertEqual(3358, res)

    def test_MMMCCCLIX(self):
        res = convert_to_arabic('MMMCCCLIX')
        self.assertEqual(3359, res)

    def test_MMMCCCLX(self):
        res = convert_to_arabic('MMMCCCLX')
        self.assertEqual(3360, res)

    def test_MMMCCCLXI(self):
        res = convert_to_arabic('MMMCCCLXI')
        self.assertEqual(3361, res)

    def test_MMMCCCLXII(self):
        res = convert_to_arabic('MMMCCCLXII')
        self.assertEqual(3362, res)

    def test_MMMCCCLXIII(self):
        res = convert_to_arabic('MMMCCCLXIII')
        self.assertEqual(3363, res)

    def test_MMMCCCLXIV(self):
        res = convert_to_arabic('MMMCCCLXIV')
        self.assertEqual(3364, res)

    def test_MMMCCCLXV(self):
        res = convert_to_arabic('MMMCCCLXV')
        self.assertEqual(3365, res)

    def test_MMMCCCLXVI(self):
        res = convert_to_arabic('MMMCCCLXVI')
        self.assertEqual(3366, res)

    def test_MMMCCCLXVII(self):
        res = convert_to_arabic('MMMCCCLXVII')
        self.assertEqual(3367, res)

    def test_MMMCCCLXVIII(self):
        res = convert_to_arabic('MMMCCCLXVIII')
        self.assertEqual(3368, res)

    def test_MMMCCCLXIX(self):
        res = convert_to_arabic('MMMCCCLXIX')
        self.assertEqual(3369, res)

    def test_MMMCCCLXX(self):
        res = convert_to_arabic('MMMCCCLXX')
        self.assertEqual(3370, res)

    def test_MMMCCCLXXI(self):
        res = convert_to_arabic('MMMCCCLXXI')
        self.assertEqual(3371, res)

    def test_MMMCCCLXXII(self):
        res = convert_to_arabic('MMMCCCLXXII')
        self.assertEqual(3372, res)

    def test_MMMCCCLXXIII(self):
        res = convert_to_arabic('MMMCCCLXXIII')
        self.assertEqual(3373, res)

    def test_MMMCCCLXXIV(self):
        res = convert_to_arabic('MMMCCCLXXIV')
        self.assertEqual(3374, res)

    def test_MMMCCCLXXV(self):
        res = convert_to_arabic('MMMCCCLXXV')
        self.assertEqual(3375, res)

    def test_MMMCCCLXXVI(self):
        res = convert_to_arabic('MMMCCCLXXVI')
        self.assertEqual(3376, res)

    def test_MMMCCCLXXVII(self):
        res = convert_to_arabic('MMMCCCLXXVII')
        self.assertEqual(3377, res)

    def test_MMMCCCLXXVIII(self):
        res = convert_to_arabic('MMMCCCLXXVIII')
        self.assertEqual(3378, res)

    def test_MMMCCCLXXIX(self):
        res = convert_to_arabic('MMMCCCLXXIX')
        self.assertEqual(3379, res)

    def test_MMMCCCLXXX(self):
        res = convert_to_arabic('MMMCCCLXXX')
        self.assertEqual(3380, res)

    def test_MMMCCCLXXXI(self):
        res = convert_to_arabic('MMMCCCLXXXI')
        self.assertEqual(3381, res)

    def test_MMMCCCLXXXII(self):
        res = convert_to_arabic('MMMCCCLXXXII')
        self.assertEqual(3382, res)

    def test_MMMCCCLXXXIII(self):
        res = convert_to_arabic('MMMCCCLXXXIII')
        self.assertEqual(3383, res)

    def test_MMMCCCLXXXIV(self):
        res = convert_to_arabic('MMMCCCLXXXIV')
        self.assertEqual(3384, res)

    def test_MMMCCCLXXXV(self):
        res = convert_to_arabic('MMMCCCLXXXV')
        self.assertEqual(3385, res)

    def test_MMMCCCLXXXVI(self):
        res = convert_to_arabic('MMMCCCLXXXVI')
        self.assertEqual(3386, res)

    def test_MMMCCCLXXXVII(self):
        res = convert_to_arabic('MMMCCCLXXXVII')
        self.assertEqual(3387, res)

    def test_MMMCCCLXXXVIII(self):
        res = convert_to_arabic('MMMCCCLXXXVIII')
        self.assertEqual(3388, res)

    def test_MMMCCCLXXXIX(self):
        res = convert_to_arabic('MMMCCCLXXXIX')
        self.assertEqual(3389, res)

    def test_MMMCCCXC(self):
        res = convert_to_arabic('MMMCCCXC')
        self.assertEqual(3390, res)

    def test_MMMCCCXCI(self):
        res = convert_to_arabic('MMMCCCXCI')
        self.assertEqual(3391, res)

    def test_MMMCCCXCII(self):
        res = convert_to_arabic('MMMCCCXCII')
        self.assertEqual(3392, res)

    def test_MMMCCCXCIII(self):
        res = convert_to_arabic('MMMCCCXCIII')
        self.assertEqual(3393, res)

    def test_MMMCCCXCIV(self):
        res = convert_to_arabic('MMMCCCXCIV')
        self.assertEqual(3394, res)

    def test_MMMCCCXCV(self):
        res = convert_to_arabic('MMMCCCXCV')
        self.assertEqual(3395, res)

    def test_MMMCCCXCVI(self):
        res = convert_to_arabic('MMMCCCXCVI')
        self.assertEqual(3396, res)

    def test_MMMCCCXCVII(self):
        res = convert_to_arabic('MMMCCCXCVII')
        self.assertEqual(3397, res)

    def test_MMMCCCXCVIII(self):
        res = convert_to_arabic('MMMCCCXCVIII')
        self.assertEqual(3398, res)

    def test_MMMCCCXCIX(self):
        res = convert_to_arabic('MMMCCCXCIX')
        self.assertEqual(3399, res)

    def test_MMMCD(self):
        res = convert_to_arabic('MMMCD')
        self.assertEqual(3400, res)

    def test_MMMCDI(self):
        res = convert_to_arabic('MMMCDI')
        self.assertEqual(3401, res)

    def test_MMMCDII(self):
        res = convert_to_arabic('MMMCDII')
        self.assertEqual(3402, res)

    def test_MMMCDIII(self):
        res = convert_to_arabic('MMMCDIII')
        self.assertEqual(3403, res)

    def test_MMMCDIV(self):
        res = convert_to_arabic('MMMCDIV')
        self.assertEqual(3404, res)

    def test_MMMCDV(self):
        res = convert_to_arabic('MMMCDV')
        self.assertEqual(3405, res)

    def test_MMMCDVI(self):
        res = convert_to_arabic('MMMCDVI')
        self.assertEqual(3406, res)

    def test_MMMCDVII(self):
        res = convert_to_arabic('MMMCDVII')
        self.assertEqual(3407, res)

    def test_MMMCDVIII(self):
        res = convert_to_arabic('MMMCDVIII')
        self.assertEqual(3408, res)

    def test_MMMCDIX(self):
        res = convert_to_arabic('MMMCDIX')
        self.assertEqual(3409, res)

    def test_MMMCDX(self):
        res = convert_to_arabic('MMMCDX')
        self.assertEqual(3410, res)

    def test_MMMCDXI(self):
        res = convert_to_arabic('MMMCDXI')
        self.assertEqual(3411, res)

    def test_MMMCDXII(self):
        res = convert_to_arabic('MMMCDXII')
        self.assertEqual(3412, res)

    def test_MMMCDXIII(self):
        res = convert_to_arabic('MMMCDXIII')
        self.assertEqual(3413, res)

    def test_MMMCDXIV(self):
        res = convert_to_arabic('MMMCDXIV')
        self.assertEqual(3414, res)

    def test_MMMCDXV(self):
        res = convert_to_arabic('MMMCDXV')
        self.assertEqual(3415, res)

    def test_MMMCDXVI(self):
        res = convert_to_arabic('MMMCDXVI')
        self.assertEqual(3416, res)

    def test_MMMCDXVII(self):
        res = convert_to_arabic('MMMCDXVII')
        self.assertEqual(3417, res)

    def test_MMMCDXVIII(self):
        res = convert_to_arabic('MMMCDXVIII')
        self.assertEqual(3418, res)

    def test_MMMCDXIX(self):
        res = convert_to_arabic('MMMCDXIX')
        self.assertEqual(3419, res)

    def test_MMMCDXX(self):
        res = convert_to_arabic('MMMCDXX')
        self.assertEqual(3420, res)

    def test_MMMCDXXI(self):
        res = convert_to_arabic('MMMCDXXI')
        self.assertEqual(3421, res)

    def test_MMMCDXXII(self):
        res = convert_to_arabic('MMMCDXXII')
        self.assertEqual(3422, res)

    def test_MMMCDXXIII(self):
        res = convert_to_arabic('MMMCDXXIII')
        self.assertEqual(3423, res)

    def test_MMMCDXXIV(self):
        res = convert_to_arabic('MMMCDXXIV')
        self.assertEqual(3424, res)

    def test_MMMCDXXV(self):
        res = convert_to_arabic('MMMCDXXV')
        self.assertEqual(3425, res)

    def test_MMMCDXXVI(self):
        res = convert_to_arabic('MMMCDXXVI')
        self.assertEqual(3426, res)

    def test_MMMCDXXVII(self):
        res = convert_to_arabic('MMMCDXXVII')
        self.assertEqual(3427, res)

    def test_MMMCDXXVIII(self):
        res = convert_to_arabic('MMMCDXXVIII')
        self.assertEqual(3428, res)

    def test_MMMCDXXIX(self):
        res = convert_to_arabic('MMMCDXXIX')
        self.assertEqual(3429, res)

    def test_MMMCDXXX(self):
        res = convert_to_arabic('MMMCDXXX')
        self.assertEqual(3430, res)

    def test_MMMCDXXXI(self):
        res = convert_to_arabic('MMMCDXXXI')
        self.assertEqual(3431, res)

    def test_MMMCDXXXII(self):
        res = convert_to_arabic('MMMCDXXXII')
        self.assertEqual(3432, res)

    def test_MMMCDXXXIII(self):
        res = convert_to_arabic('MMMCDXXXIII')
        self.assertEqual(3433, res)

    def test_MMMCDXXXIV(self):
        res = convert_to_arabic('MMMCDXXXIV')
        self.assertEqual(3434, res)

    def test_MMMCDXXXV(self):
        res = convert_to_arabic('MMMCDXXXV')
        self.assertEqual(3435, res)

    def test_MMMCDXXXVI(self):
        res = convert_to_arabic('MMMCDXXXVI')
        self.assertEqual(3436, res)

    def test_MMMCDXXXVII(self):
        res = convert_to_arabic('MMMCDXXXVII')
        self.assertEqual(3437, res)

    def test_MMMCDXXXVIII(self):
        res = convert_to_arabic('MMMCDXXXVIII')
        self.assertEqual(3438, res)

    def test_MMMCDXXXIX(self):
        res = convert_to_arabic('MMMCDXXXIX')
        self.assertEqual(3439, res)

    def test_MMMCDXL(self):
        res = convert_to_arabic('MMMCDXL')
        self.assertEqual(3440, res)

    def test_MMMCDXLI(self):
        res = convert_to_arabic('MMMCDXLI')
        self.assertEqual(3441, res)

    def test_MMMCDXLII(self):
        res = convert_to_arabic('MMMCDXLII')
        self.assertEqual(3442, res)

    def test_MMMCDXLIII(self):
        res = convert_to_arabic('MMMCDXLIII')
        self.assertEqual(3443, res)

    def test_MMMCDXLIV(self):
        res = convert_to_arabic('MMMCDXLIV')
        self.assertEqual(3444, res)

    def test_MMMCDXLV(self):
        res = convert_to_arabic('MMMCDXLV')
        self.assertEqual(3445, res)

    def test_MMMCDXLVI(self):
        res = convert_to_arabic('MMMCDXLVI')
        self.assertEqual(3446, res)

    def test_MMMCDXLVII(self):
        res = convert_to_arabic('MMMCDXLVII')
        self.assertEqual(3447, res)

    def test_MMMCDXLVIII(self):
        res = convert_to_arabic('MMMCDXLVIII')
        self.assertEqual(3448, res)

    def test_MMMCDXLIX(self):
        res = convert_to_arabic('MMMCDXLIX')
        self.assertEqual(3449, res)

    def test_MMMCDL(self):
        res = convert_to_arabic('MMMCDL')
        self.assertEqual(3450, res)

    def test_MMMCDLI(self):
        res = convert_to_arabic('MMMCDLI')
        self.assertEqual(3451, res)

    def test_MMMCDLII(self):
        res = convert_to_arabic('MMMCDLII')
        self.assertEqual(3452, res)

    def test_MMMCDLIII(self):
        res = convert_to_arabic('MMMCDLIII')
        self.assertEqual(3453, res)

    def test_MMMCDLIV(self):
        res = convert_to_arabic('MMMCDLIV')
        self.assertEqual(3454, res)

    def test_MMMCDLV(self):
        res = convert_to_arabic('MMMCDLV')
        self.assertEqual(3455, res)

    def test_MMMCDLVI(self):
        res = convert_to_arabic('MMMCDLVI')
        self.assertEqual(3456, res)

    def test_MMMCDLVII(self):
        res = convert_to_arabic('MMMCDLVII')
        self.assertEqual(3457, res)

    def test_MMMCDLVIII(self):
        res = convert_to_arabic('MMMCDLVIII')
        self.assertEqual(3458, res)

    def test_MMMCDLIX(self):
        res = convert_to_arabic('MMMCDLIX')
        self.assertEqual(3459, res)

    def test_MMMCDLX(self):
        res = convert_to_arabic('MMMCDLX')
        self.assertEqual(3460, res)

    def test_MMMCDLXI(self):
        res = convert_to_arabic('MMMCDLXI')
        self.assertEqual(3461, res)

    def test_MMMCDLXII(self):
        res = convert_to_arabic('MMMCDLXII')
        self.assertEqual(3462, res)

    def test_MMMCDLXIII(self):
        res = convert_to_arabic('MMMCDLXIII')
        self.assertEqual(3463, res)

    def test_MMMCDLXIV(self):
        res = convert_to_arabic('MMMCDLXIV')
        self.assertEqual(3464, res)

    def test_MMMCDLXV(self):
        res = convert_to_arabic('MMMCDLXV')
        self.assertEqual(3465, res)

    def test_MMMCDLXVI(self):
        res = convert_to_arabic('MMMCDLXVI')
        self.assertEqual(3466, res)

    def test_MMMCDLXVII(self):
        res = convert_to_arabic('MMMCDLXVII')
        self.assertEqual(3467, res)

    def test_MMMCDLXVIII(self):
        res = convert_to_arabic('MMMCDLXVIII')
        self.assertEqual(3468, res)

    def test_MMMCDLXIX(self):
        res = convert_to_arabic('MMMCDLXIX')
        self.assertEqual(3469, res)

    def test_MMMCDLXX(self):
        res = convert_to_arabic('MMMCDLXX')
        self.assertEqual(3470, res)

    def test_MMMCDLXXI(self):
        res = convert_to_arabic('MMMCDLXXI')
        self.assertEqual(3471, res)

    def test_MMMCDLXXII(self):
        res = convert_to_arabic('MMMCDLXXII')
        self.assertEqual(3472, res)

    def test_MMMCDLXXIII(self):
        res = convert_to_arabic('MMMCDLXXIII')
        self.assertEqual(3473, res)

    def test_MMMCDLXXIV(self):
        res = convert_to_arabic('MMMCDLXXIV')
        self.assertEqual(3474, res)

    def test_MMMCDLXXV(self):
        res = convert_to_arabic('MMMCDLXXV')
        self.assertEqual(3475, res)

    def test_MMMCDLXXVI(self):
        res = convert_to_arabic('MMMCDLXXVI')
        self.assertEqual(3476, res)

    def test_MMMCDLXXVII(self):
        res = convert_to_arabic('MMMCDLXXVII')
        self.assertEqual(3477, res)

    def test_MMMCDLXXVIII(self):
        res = convert_to_arabic('MMMCDLXXVIII')
        self.assertEqual(3478, res)

    def test_MMMCDLXXIX(self):
        res = convert_to_arabic('MMMCDLXXIX')
        self.assertEqual(3479, res)

    def test_MMMCDLXXX(self):
        res = convert_to_arabic('MMMCDLXXX')
        self.assertEqual(3480, res)

    def test_MMMCDLXXXI(self):
        res = convert_to_arabic('MMMCDLXXXI')
        self.assertEqual(3481, res)

    def test_MMMCDLXXXII(self):
        res = convert_to_arabic('MMMCDLXXXII')
        self.assertEqual(3482, res)

    def test_MMMCDLXXXIII(self):
        res = convert_to_arabic('MMMCDLXXXIII')
        self.assertEqual(3483, res)

    def test_MMMCDLXXXIV(self):
        res = convert_to_arabic('MMMCDLXXXIV')
        self.assertEqual(3484, res)

    def test_MMMCDLXXXV(self):
        res = convert_to_arabic('MMMCDLXXXV')
        self.assertEqual(3485, res)

    def test_MMMCDLXXXVI(self):
        res = convert_to_arabic('MMMCDLXXXVI')
        self.assertEqual(3486, res)

    def test_MMMCDLXXXVII(self):
        res = convert_to_arabic('MMMCDLXXXVII')
        self.assertEqual(3487, res)

    def test_MMMCDLXXXVIII(self):
        res = convert_to_arabic('MMMCDLXXXVIII')
        self.assertEqual(3488, res)

    def test_MMMCDLXXXIX(self):
        res = convert_to_arabic('MMMCDLXXXIX')
        self.assertEqual(3489, res)

    def test_MMMCDXC(self):
        res = convert_to_arabic('MMMCDXC')
        self.assertEqual(3490, res)

    def test_MMMCDXCI(self):
        res = convert_to_arabic('MMMCDXCI')
        self.assertEqual(3491, res)

    def test_MMMCDXCII(self):
        res = convert_to_arabic('MMMCDXCII')
        self.assertEqual(3492, res)

    def test_MMMCDXCIII(self):
        res = convert_to_arabic('MMMCDXCIII')
        self.assertEqual(3493, res)

    def test_MMMCDXCIV(self):
        res = convert_to_arabic('MMMCDXCIV')
        self.assertEqual(3494, res)

    def test_MMMCDXCV(self):
        res = convert_to_arabic('MMMCDXCV')
        self.assertEqual(3495, res)

    def test_MMMCDXCVI(self):
        res = convert_to_arabic('MMMCDXCVI')
        self.assertEqual(3496, res)

    def test_MMMCDXCVII(self):
        res = convert_to_arabic('MMMCDXCVII')
        self.assertEqual(3497, res)

    def test_MMMCDXCVIII(self):
        res = convert_to_arabic('MMMCDXCVIII')
        self.assertEqual(3498, res)

    def test_MMMCDXCIX(self):
        res = convert_to_arabic('MMMCDXCIX')
        self.assertEqual(3499, res)

    def test_MMMD(self):
        res = convert_to_arabic('MMMD')
        self.assertEqual(3500, res)

    def test_MMMDI(self):
        res = convert_to_arabic('MMMDI')
        self.assertEqual(3501, res)

    def test_MMMDII(self):
        res = convert_to_arabic('MMMDII')
        self.assertEqual(3502, res)

    def test_MMMDIII(self):
        res = convert_to_arabic('MMMDIII')
        self.assertEqual(3503, res)

    def test_MMMDIV(self):
        res = convert_to_arabic('MMMDIV')
        self.assertEqual(3504, res)

    def test_MMMDV(self):
        res = convert_to_arabic('MMMDV')
        self.assertEqual(3505, res)

    def test_MMMDVI(self):
        res = convert_to_arabic('MMMDVI')
        self.assertEqual(3506, res)

    def test_MMMDVII(self):
        res = convert_to_arabic('MMMDVII')
        self.assertEqual(3507, res)

    def test_MMMDVIII(self):
        res = convert_to_arabic('MMMDVIII')
        self.assertEqual(3508, res)

    def test_MMMDIX(self):
        res = convert_to_arabic('MMMDIX')
        self.assertEqual(3509, res)

    def test_MMMDX(self):
        res = convert_to_arabic('MMMDX')
        self.assertEqual(3510, res)

    def test_MMMDXI(self):
        res = convert_to_arabic('MMMDXI')
        self.assertEqual(3511, res)

    def test_MMMDXII(self):
        res = convert_to_arabic('MMMDXII')
        self.assertEqual(3512, res)

    def test_MMMDXIII(self):
        res = convert_to_arabic('MMMDXIII')
        self.assertEqual(3513, res)

    def test_MMMDXIV(self):
        res = convert_to_arabic('MMMDXIV')
        self.assertEqual(3514, res)

    def test_MMMDXV(self):
        res = convert_to_arabic('MMMDXV')
        self.assertEqual(3515, res)

    def test_MMMDXVI(self):
        res = convert_to_arabic('MMMDXVI')
        self.assertEqual(3516, res)

    def test_MMMDXVII(self):
        res = convert_to_arabic('MMMDXVII')
        self.assertEqual(3517, res)

    def test_MMMDXVIII(self):
        res = convert_to_arabic('MMMDXVIII')
        self.assertEqual(3518, res)

    def test_MMMDXIX(self):
        res = convert_to_arabic('MMMDXIX')
        self.assertEqual(3519, res)

    def test_MMMDXX(self):
        res = convert_to_arabic('MMMDXX')
        self.assertEqual(3520, res)

    def test_MMMDXXI(self):
        res = convert_to_arabic('MMMDXXI')
        self.assertEqual(3521, res)

    def test_MMMDXXII(self):
        res = convert_to_arabic('MMMDXXII')
        self.assertEqual(3522, res)

    def test_MMMDXXIII(self):
        res = convert_to_arabic('MMMDXXIII')
        self.assertEqual(3523, res)

    def test_MMMDXXIV(self):
        res = convert_to_arabic('MMMDXXIV')
        self.assertEqual(3524, res)

    def test_MMMDXXV(self):
        res = convert_to_arabic('MMMDXXV')
        self.assertEqual(3525, res)

    def test_MMMDXXVI(self):
        res = convert_to_arabic('MMMDXXVI')
        self.assertEqual(3526, res)

    def test_MMMDXXVII(self):
        res = convert_to_arabic('MMMDXXVII')
        self.assertEqual(3527, res)

    def test_MMMDXXVIII(self):
        res = convert_to_arabic('MMMDXXVIII')
        self.assertEqual(3528, res)

    def test_MMMDXXIX(self):
        res = convert_to_arabic('MMMDXXIX')
        self.assertEqual(3529, res)

    def test_MMMDXXX(self):
        res = convert_to_arabic('MMMDXXX')
        self.assertEqual(3530, res)

    def test_MMMDXXXI(self):
        res = convert_to_arabic('MMMDXXXI')
        self.assertEqual(3531, res)

    def test_MMMDXXXII(self):
        res = convert_to_arabic('MMMDXXXII')
        self.assertEqual(3532, res)

    def test_MMMDXXXIII(self):
        res = convert_to_arabic('MMMDXXXIII')
        self.assertEqual(3533, res)

    def test_MMMDXXXIV(self):
        res = convert_to_arabic('MMMDXXXIV')
        self.assertEqual(3534, res)

    def test_MMMDXXXV(self):
        res = convert_to_arabic('MMMDXXXV')
        self.assertEqual(3535, res)

    def test_MMMDXXXVI(self):
        res = convert_to_arabic('MMMDXXXVI')
        self.assertEqual(3536, res)

    def test_MMMDXXXVII(self):
        res = convert_to_arabic('MMMDXXXVII')
        self.assertEqual(3537, res)

    def test_MMMDXXXVIII(self):
        res = convert_to_arabic('MMMDXXXVIII')
        self.assertEqual(3538, res)

    def test_MMMDXXXIX(self):
        res = convert_to_arabic('MMMDXXXIX')
        self.assertEqual(3539, res)

    def test_MMMDXL(self):
        res = convert_to_arabic('MMMDXL')
        self.assertEqual(3540, res)

    def test_MMMDXLI(self):
        res = convert_to_arabic('MMMDXLI')
        self.assertEqual(3541, res)

    def test_MMMDXLII(self):
        res = convert_to_arabic('MMMDXLII')
        self.assertEqual(3542, res)

    def test_MMMDXLIII(self):
        res = convert_to_arabic('MMMDXLIII')
        self.assertEqual(3543, res)

    def test_MMMDXLIV(self):
        res = convert_to_arabic('MMMDXLIV')
        self.assertEqual(3544, res)

    def test_MMMDXLV(self):
        res = convert_to_arabic('MMMDXLV')
        self.assertEqual(3545, res)

    def test_MMMDXLVI(self):
        res = convert_to_arabic('MMMDXLVI')
        self.assertEqual(3546, res)

    def test_MMMDXLVII(self):
        res = convert_to_arabic('MMMDXLVII')
        self.assertEqual(3547, res)

    def test_MMMDXLVIII(self):
        res = convert_to_arabic('MMMDXLVIII')
        self.assertEqual(3548, res)

    def test_MMMDXLIX(self):
        res = convert_to_arabic('MMMDXLIX')
        self.assertEqual(3549, res)

    def test_MMMDL(self):
        res = convert_to_arabic('MMMDL')
        self.assertEqual(3550, res)

    def test_MMMDLI(self):
        res = convert_to_arabic('MMMDLI')
        self.assertEqual(3551, res)

    def test_MMMDLII(self):
        res = convert_to_arabic('MMMDLII')
        self.assertEqual(3552, res)

    def test_MMMDLIII(self):
        res = convert_to_arabic('MMMDLIII')
        self.assertEqual(3553, res)

    def test_MMMDLIV(self):
        res = convert_to_arabic('MMMDLIV')
        self.assertEqual(3554, res)

    def test_MMMDLV(self):
        res = convert_to_arabic('MMMDLV')
        self.assertEqual(3555, res)

    def test_MMMDLVI(self):
        res = convert_to_arabic('MMMDLVI')
        self.assertEqual(3556, res)

    def test_MMMDLVII(self):
        res = convert_to_arabic('MMMDLVII')
        self.assertEqual(3557, res)

    def test_MMMDLVIII(self):
        res = convert_to_arabic('MMMDLVIII')
        self.assertEqual(3558, res)

    def test_MMMDLIX(self):
        res = convert_to_arabic('MMMDLIX')
        self.assertEqual(3559, res)

    def test_MMMDLX(self):
        res = convert_to_arabic('MMMDLX')
        self.assertEqual(3560, res)

    def test_MMMDLXI(self):
        res = convert_to_arabic('MMMDLXI')
        self.assertEqual(3561, res)

    def test_MMMDLXII(self):
        res = convert_to_arabic('MMMDLXII')
        self.assertEqual(3562, res)

    def test_MMMDLXIII(self):
        res = convert_to_arabic('MMMDLXIII')
        self.assertEqual(3563, res)

    def test_MMMDLXIV(self):
        res = convert_to_arabic('MMMDLXIV')
        self.assertEqual(3564, res)

    def test_MMMDLXV(self):
        res = convert_to_arabic('MMMDLXV')
        self.assertEqual(3565, res)

    def test_MMMDLXVI(self):
        res = convert_to_arabic('MMMDLXVI')
        self.assertEqual(3566, res)

    def test_MMMDLXVII(self):
        res = convert_to_arabic('MMMDLXVII')
        self.assertEqual(3567, res)

    def test_MMMDLXVIII(self):
        res = convert_to_arabic('MMMDLXVIII')
        self.assertEqual(3568, res)

    def test_MMMDLXIX(self):
        res = convert_to_arabic('MMMDLXIX')
        self.assertEqual(3569, res)

    def test_MMMDLXX(self):
        res = convert_to_arabic('MMMDLXX')
        self.assertEqual(3570, res)

    def test_MMMDLXXI(self):
        res = convert_to_arabic('MMMDLXXI')
        self.assertEqual(3571, res)

    def test_MMMDLXXII(self):
        res = convert_to_arabic('MMMDLXXII')
        self.assertEqual(3572, res)

    def test_MMMDLXXIII(self):
        res = convert_to_arabic('MMMDLXXIII')
        self.assertEqual(3573, res)

    def test_MMMDLXXIV(self):
        res = convert_to_arabic('MMMDLXXIV')
        self.assertEqual(3574, res)

    def test_MMMDLXXV(self):
        res = convert_to_arabic('MMMDLXXV')
        self.assertEqual(3575, res)

    def test_MMMDLXXVI(self):
        res = convert_to_arabic('MMMDLXXVI')
        self.assertEqual(3576, res)

    def test_MMMDLXXVII(self):
        res = convert_to_arabic('MMMDLXXVII')
        self.assertEqual(3577, res)

    def test_MMMDLXXVIII(self):
        res = convert_to_arabic('MMMDLXXVIII')
        self.assertEqual(3578, res)

    def test_MMMDLXXIX(self):
        res = convert_to_arabic('MMMDLXXIX')
        self.assertEqual(3579, res)

    def test_MMMDLXXX(self):
        res = convert_to_arabic('MMMDLXXX')
        self.assertEqual(3580, res)

    def test_MMMDLXXXI(self):
        res = convert_to_arabic('MMMDLXXXI')
        self.assertEqual(3581, res)

    def test_MMMDLXXXII(self):
        res = convert_to_arabic('MMMDLXXXII')
        self.assertEqual(3582, res)

    def test_MMMDLXXXIII(self):
        res = convert_to_arabic('MMMDLXXXIII')
        self.assertEqual(3583, res)

    def test_MMMDLXXXIV(self):
        res = convert_to_arabic('MMMDLXXXIV')
        self.assertEqual(3584, res)

    def test_MMMDLXXXV(self):
        res = convert_to_arabic('MMMDLXXXV')
        self.assertEqual(3585, res)

    def test_MMMDLXXXVI(self):
        res = convert_to_arabic('MMMDLXXXVI')
        self.assertEqual(3586, res)

    def test_MMMDLXXXVII(self):
        res = convert_to_arabic('MMMDLXXXVII')
        self.assertEqual(3587, res)

    def test_MMMDLXXXVIII(self):
        res = convert_to_arabic('MMMDLXXXVIII')
        self.assertEqual(3588, res)

    def test_MMMDLXXXIX(self):
        res = convert_to_arabic('MMMDLXXXIX')
        self.assertEqual(3589, res)

    def test_MMMDXC(self):
        res = convert_to_arabic('MMMDXC')
        self.assertEqual(3590, res)

    def test_MMMDXCI(self):
        res = convert_to_arabic('MMMDXCI')
        self.assertEqual(3591, res)

    def test_MMMDXCII(self):
        res = convert_to_arabic('MMMDXCII')
        self.assertEqual(3592, res)

    def test_MMMDXCIII(self):
        res = convert_to_arabic('MMMDXCIII')
        self.assertEqual(3593, res)

    def test_MMMDXCIV(self):
        res = convert_to_arabic('MMMDXCIV')
        self.assertEqual(3594, res)

    def test_MMMDXCV(self):
        res = convert_to_arabic('MMMDXCV')
        self.assertEqual(3595, res)

    def test_MMMDXCVI(self):
        res = convert_to_arabic('MMMDXCVI')
        self.assertEqual(3596, res)

    def test_MMMDXCVII(self):
        res = convert_to_arabic('MMMDXCVII')
        self.assertEqual(3597, res)

    def test_MMMDXCVIII(self):
        res = convert_to_arabic('MMMDXCVIII')
        self.assertEqual(3598, res)

    def test_MMMDXCIX(self):
        res = convert_to_arabic('MMMDXCIX')
        self.assertEqual(3599, res)

    def test_MMMDC(self):
        res = convert_to_arabic('MMMDC')
        self.assertEqual(3600, res)

    def test_MMMDCI(self):
        res = convert_to_arabic('MMMDCI')
        self.assertEqual(3601, res)

    def test_MMMDCII(self):
        res = convert_to_arabic('MMMDCII')
        self.assertEqual(3602, res)

    def test_MMMDCIII(self):
        res = convert_to_arabic('MMMDCIII')
        self.assertEqual(3603, res)

    def test_MMMDCIV(self):
        res = convert_to_arabic('MMMDCIV')
        self.assertEqual(3604, res)

    def test_MMMDCV(self):
        res = convert_to_arabic('MMMDCV')
        self.assertEqual(3605, res)

    def test_MMMDCVI(self):
        res = convert_to_arabic('MMMDCVI')
        self.assertEqual(3606, res)

    def test_MMMDCVII(self):
        res = convert_to_arabic('MMMDCVII')
        self.assertEqual(3607, res)

    def test_MMMDCVIII(self):
        res = convert_to_arabic('MMMDCVIII')
        self.assertEqual(3608, res)

    def test_MMMDCIX(self):
        res = convert_to_arabic('MMMDCIX')
        self.assertEqual(3609, res)

    def test_MMMDCX(self):
        res = convert_to_arabic('MMMDCX')
        self.assertEqual(3610, res)

    def test_MMMDCXI(self):
        res = convert_to_arabic('MMMDCXI')
        self.assertEqual(3611, res)

    def test_MMMDCXII(self):
        res = convert_to_arabic('MMMDCXII')
        self.assertEqual(3612, res)

    def test_MMMDCXIII(self):
        res = convert_to_arabic('MMMDCXIII')
        self.assertEqual(3613, res)

    def test_MMMDCXIV(self):
        res = convert_to_arabic('MMMDCXIV')
        self.assertEqual(3614, res)

    def test_MMMDCXV(self):
        res = convert_to_arabic('MMMDCXV')
        self.assertEqual(3615, res)

    def test_MMMDCXVI(self):
        res = convert_to_arabic('MMMDCXVI')
        self.assertEqual(3616, res)

    def test_MMMDCXVII(self):
        res = convert_to_arabic('MMMDCXVII')
        self.assertEqual(3617, res)

    def test_MMMDCXVIII(self):
        res = convert_to_arabic('MMMDCXVIII')
        self.assertEqual(3618, res)

    def test_MMMDCXIX(self):
        res = convert_to_arabic('MMMDCXIX')
        self.assertEqual(3619, res)

    def test_MMMDCXX(self):
        res = convert_to_arabic('MMMDCXX')
        self.assertEqual(3620, res)

    def test_MMMDCXXI(self):
        res = convert_to_arabic('MMMDCXXI')
        self.assertEqual(3621, res)

    def test_MMMDCXXII(self):
        res = convert_to_arabic('MMMDCXXII')
        self.assertEqual(3622, res)

    def test_MMMDCXXIII(self):
        res = convert_to_arabic('MMMDCXXIII')
        self.assertEqual(3623, res)

    def test_MMMDCXXIV(self):
        res = convert_to_arabic('MMMDCXXIV')
        self.assertEqual(3624, res)

    def test_MMMDCXXV(self):
        res = convert_to_arabic('MMMDCXXV')
        self.assertEqual(3625, res)

    def test_MMMDCXXVI(self):
        res = convert_to_arabic('MMMDCXXVI')
        self.assertEqual(3626, res)

    def test_MMMDCXXVII(self):
        res = convert_to_arabic('MMMDCXXVII')
        self.assertEqual(3627, res)

    def test_MMMDCXXVIII(self):
        res = convert_to_arabic('MMMDCXXVIII')
        self.assertEqual(3628, res)

    def test_MMMDCXXIX(self):
        res = convert_to_arabic('MMMDCXXIX')
        self.assertEqual(3629, res)

    def test_MMMDCXXX(self):
        res = convert_to_arabic('MMMDCXXX')
        self.assertEqual(3630, res)

    def test_MMMDCXXXI(self):
        res = convert_to_arabic('MMMDCXXXI')
        self.assertEqual(3631, res)

    def test_MMMDCXXXII(self):
        res = convert_to_arabic('MMMDCXXXII')
        self.assertEqual(3632, res)

    def test_MMMDCXXXIII(self):
        res = convert_to_arabic('MMMDCXXXIII')
        self.assertEqual(3633, res)

    def test_MMMDCXXXIV(self):
        res = convert_to_arabic('MMMDCXXXIV')
        self.assertEqual(3634, res)

    def test_MMMDCXXXV(self):
        res = convert_to_arabic('MMMDCXXXV')
        self.assertEqual(3635, res)

    def test_MMMDCXXXVI(self):
        res = convert_to_arabic('MMMDCXXXVI')
        self.assertEqual(3636, res)

    def test_MMMDCXXXVII(self):
        res = convert_to_arabic('MMMDCXXXVII')
        self.assertEqual(3637, res)

    def test_MMMDCXXXVIII(self):
        res = convert_to_arabic('MMMDCXXXVIII')
        self.assertEqual(3638, res)

    def test_MMMDCXXXIX(self):
        res = convert_to_arabic('MMMDCXXXIX')
        self.assertEqual(3639, res)

    def test_MMMDCXL(self):
        res = convert_to_arabic('MMMDCXL')
        self.assertEqual(3640, res)

    def test_MMMDCXLI(self):
        res = convert_to_arabic('MMMDCXLI')
        self.assertEqual(3641, res)

    def test_MMMDCXLII(self):
        res = convert_to_arabic('MMMDCXLII')
        self.assertEqual(3642, res)

    def test_MMMDCXLIII(self):
        res = convert_to_arabic('MMMDCXLIII')
        self.assertEqual(3643, res)

    def test_MMMDCXLIV(self):
        res = convert_to_arabic('MMMDCXLIV')
        self.assertEqual(3644, res)

    def test_MMMDCXLV(self):
        res = convert_to_arabic('MMMDCXLV')
        self.assertEqual(3645, res)

    def test_MMMDCXLVI(self):
        res = convert_to_arabic('MMMDCXLVI')
        self.assertEqual(3646, res)

    def test_MMMDCXLVII(self):
        res = convert_to_arabic('MMMDCXLVII')
        self.assertEqual(3647, res)

    def test_MMMDCXLVIII(self):
        res = convert_to_arabic('MMMDCXLVIII')
        self.assertEqual(3648, res)

    def test_MMMDCXLIX(self):
        res = convert_to_arabic('MMMDCXLIX')
        self.assertEqual(3649, res)

    def test_MMMDCL(self):
        res = convert_to_arabic('MMMDCL')
        self.assertEqual(3650, res)

    def test_MMMDCLI(self):
        res = convert_to_arabic('MMMDCLI')
        self.assertEqual(3651, res)

    def test_MMMDCLII(self):
        res = convert_to_arabic('MMMDCLII')
        self.assertEqual(3652, res)

    def test_MMMDCLIII(self):
        res = convert_to_arabic('MMMDCLIII')
        self.assertEqual(3653, res)

    def test_MMMDCLIV(self):
        res = convert_to_arabic('MMMDCLIV')
        self.assertEqual(3654, res)

    def test_MMMDCLV(self):
        res = convert_to_arabic('MMMDCLV')
        self.assertEqual(3655, res)

    def test_MMMDCLVI(self):
        res = convert_to_arabic('MMMDCLVI')
        self.assertEqual(3656, res)

    def test_MMMDCLVII(self):
        res = convert_to_arabic('MMMDCLVII')
        self.assertEqual(3657, res)

    def test_MMMDCLVIII(self):
        res = convert_to_arabic('MMMDCLVIII')
        self.assertEqual(3658, res)

    def test_MMMDCLIX(self):
        res = convert_to_arabic('MMMDCLIX')
        self.assertEqual(3659, res)

    def test_MMMDCLX(self):
        res = convert_to_arabic('MMMDCLX')
        self.assertEqual(3660, res)

    def test_MMMDCLXI(self):
        res = convert_to_arabic('MMMDCLXI')
        self.assertEqual(3661, res)

    def test_MMMDCLXII(self):
        res = convert_to_arabic('MMMDCLXII')
        self.assertEqual(3662, res)

    def test_MMMDCLXIII(self):
        res = convert_to_arabic('MMMDCLXIII')
        self.assertEqual(3663, res)

    def test_MMMDCLXIV(self):
        res = convert_to_arabic('MMMDCLXIV')
        self.assertEqual(3664, res)

    def test_MMMDCLXV(self):
        res = convert_to_arabic('MMMDCLXV')
        self.assertEqual(3665, res)

    def test_MMMDCLXVI(self):
        res = convert_to_arabic('MMMDCLXVI')
        self.assertEqual(3666, res)

    def test_MMMDCLXVII(self):
        res = convert_to_arabic('MMMDCLXVII')
        self.assertEqual(3667, res)

    def test_MMMDCLXVIII(self):
        res = convert_to_arabic('MMMDCLXVIII')
        self.assertEqual(3668, res)

    def test_MMMDCLXIX(self):
        res = convert_to_arabic('MMMDCLXIX')
        self.assertEqual(3669, res)

    def test_MMMDCLXX(self):
        res = convert_to_arabic('MMMDCLXX')
        self.assertEqual(3670, res)

    def test_MMMDCLXXI(self):
        res = convert_to_arabic('MMMDCLXXI')
        self.assertEqual(3671, res)

    def test_MMMDCLXXII(self):
        res = convert_to_arabic('MMMDCLXXII')
        self.assertEqual(3672, res)

    def test_MMMDCLXXIII(self):
        res = convert_to_arabic('MMMDCLXXIII')
        self.assertEqual(3673, res)

    def test_MMMDCLXXIV(self):
        res = convert_to_arabic('MMMDCLXXIV')
        self.assertEqual(3674, res)

    def test_MMMDCLXXV(self):
        res = convert_to_arabic('MMMDCLXXV')
        self.assertEqual(3675, res)

    def test_MMMDCLXXVI(self):
        res = convert_to_arabic('MMMDCLXXVI')
        self.assertEqual(3676, res)

    def test_MMMDCLXXVII(self):
        res = convert_to_arabic('MMMDCLXXVII')
        self.assertEqual(3677, res)

    def test_MMMDCLXXVIII(self):
        res = convert_to_arabic('MMMDCLXXVIII')
        self.assertEqual(3678, res)

    def test_MMMDCLXXIX(self):
        res = convert_to_arabic('MMMDCLXXIX')
        self.assertEqual(3679, res)

    def test_MMMDCLXXX(self):
        res = convert_to_arabic('MMMDCLXXX')
        self.assertEqual(3680, res)

    def test_MMMDCLXXXI(self):
        res = convert_to_arabic('MMMDCLXXXI')
        self.assertEqual(3681, res)

    def test_MMMDCLXXXII(self):
        res = convert_to_arabic('MMMDCLXXXII')
        self.assertEqual(3682, res)

    def test_MMMDCLXXXIII(self):
        res = convert_to_arabic('MMMDCLXXXIII')
        self.assertEqual(3683, res)

    def test_MMMDCLXXXIV(self):
        res = convert_to_arabic('MMMDCLXXXIV')
        self.assertEqual(3684, res)

    def test_MMMDCLXXXV(self):
        res = convert_to_arabic('MMMDCLXXXV')
        self.assertEqual(3685, res)

    def test_MMMDCLXXXVI(self):
        res = convert_to_arabic('MMMDCLXXXVI')
        self.assertEqual(3686, res)

    def test_MMMDCLXXXVII(self):
        res = convert_to_arabic('MMMDCLXXXVII')
        self.assertEqual(3687, res)

    def test_MMMDCLXXXVIII(self):
        res = convert_to_arabic('MMMDCLXXXVIII')
        self.assertEqual(3688, res)

    def test_MMMDCLXXXIX(self):
        res = convert_to_arabic('MMMDCLXXXIX')
        self.assertEqual(3689, res)

    def test_MMMDCXC(self):
        res = convert_to_arabic('MMMDCXC')
        self.assertEqual(3690, res)

    def test_MMMDCXCI(self):
        res = convert_to_arabic('MMMDCXCI')
        self.assertEqual(3691, res)

    def test_MMMDCXCII(self):
        res = convert_to_arabic('MMMDCXCII')
        self.assertEqual(3692, res)

    def test_MMMDCXCIII(self):
        res = convert_to_arabic('MMMDCXCIII')
        self.assertEqual(3693, res)

    def test_MMMDCXCIV(self):
        res = convert_to_arabic('MMMDCXCIV')
        self.assertEqual(3694, res)

    def test_MMMDCXCV(self):
        res = convert_to_arabic('MMMDCXCV')
        self.assertEqual(3695, res)

    def test_MMMDCXCVI(self):
        res = convert_to_arabic('MMMDCXCVI')
        self.assertEqual(3696, res)

    def test_MMMDCXCVII(self):
        res = convert_to_arabic('MMMDCXCVII')
        self.assertEqual(3697, res)

    def test_MMMDCXCVIII(self):
        res = convert_to_arabic('MMMDCXCVIII')
        self.assertEqual(3698, res)

    def test_MMMDCXCIX(self):
        res = convert_to_arabic('MMMDCXCIX')
        self.assertEqual(3699, res)

    def test_MMMDCC(self):
        res = convert_to_arabic('MMMDCC')
        self.assertEqual(3700, res)

    def test_MMMDCCI(self):
        res = convert_to_arabic('MMMDCCI')
        self.assertEqual(3701, res)

    def test_MMMDCCII(self):
        res = convert_to_arabic('MMMDCCII')
        self.assertEqual(3702, res)

    def test_MMMDCCIII(self):
        res = convert_to_arabic('MMMDCCIII')
        self.assertEqual(3703, res)

    def test_MMMDCCIV(self):
        res = convert_to_arabic('MMMDCCIV')
        self.assertEqual(3704, res)

    def test_MMMDCCV(self):
        res = convert_to_arabic('MMMDCCV')
        self.assertEqual(3705, res)

    def test_MMMDCCVI(self):
        res = convert_to_arabic('MMMDCCVI')
        self.assertEqual(3706, res)

    def test_MMMDCCVII(self):
        res = convert_to_arabic('MMMDCCVII')
        self.assertEqual(3707, res)

    def test_MMMDCCVIII(self):
        res = convert_to_arabic('MMMDCCVIII')
        self.assertEqual(3708, res)

    def test_MMMDCCIX(self):
        res = convert_to_arabic('MMMDCCIX')
        self.assertEqual(3709, res)

    def test_MMMDCCX(self):
        res = convert_to_arabic('MMMDCCX')
        self.assertEqual(3710, res)

    def test_MMMDCCXI(self):
        res = convert_to_arabic('MMMDCCXI')
        self.assertEqual(3711, res)

    def test_MMMDCCXII(self):
        res = convert_to_arabic('MMMDCCXII')
        self.assertEqual(3712, res)

    def test_MMMDCCXIII(self):
        res = convert_to_arabic('MMMDCCXIII')
        self.assertEqual(3713, res)

    def test_MMMDCCXIV(self):
        res = convert_to_arabic('MMMDCCXIV')
        self.assertEqual(3714, res)

    def test_MMMDCCXV(self):
        res = convert_to_arabic('MMMDCCXV')
        self.assertEqual(3715, res)

    def test_MMMDCCXVI(self):
        res = convert_to_arabic('MMMDCCXVI')
        self.assertEqual(3716, res)

    def test_MMMDCCXVII(self):
        res = convert_to_arabic('MMMDCCXVII')
        self.assertEqual(3717, res)

    def test_MMMDCCXVIII(self):
        res = convert_to_arabic('MMMDCCXVIII')
        self.assertEqual(3718, res)

    def test_MMMDCCXIX(self):
        res = convert_to_arabic('MMMDCCXIX')
        self.assertEqual(3719, res)

    def test_MMMDCCXX(self):
        res = convert_to_arabic('MMMDCCXX')
        self.assertEqual(3720, res)

    def test_MMMDCCXXI(self):
        res = convert_to_arabic('MMMDCCXXI')
        self.assertEqual(3721, res)

    def test_MMMDCCXXII(self):
        res = convert_to_arabic('MMMDCCXXII')
        self.assertEqual(3722, res)

    def test_MMMDCCXXIII(self):
        res = convert_to_arabic('MMMDCCXXIII')
        self.assertEqual(3723, res)

    def test_MMMDCCXXIV(self):
        res = convert_to_arabic('MMMDCCXXIV')
        self.assertEqual(3724, res)

    def test_MMMDCCXXV(self):
        res = convert_to_arabic('MMMDCCXXV')
        self.assertEqual(3725, res)

    def test_MMMDCCXXVI(self):
        res = convert_to_arabic('MMMDCCXXVI')
        self.assertEqual(3726, res)

    def test_MMMDCCXXVII(self):
        res = convert_to_arabic('MMMDCCXXVII')
        self.assertEqual(3727, res)

    def test_MMMDCCXXVIII(self):
        res = convert_to_arabic('MMMDCCXXVIII')
        self.assertEqual(3728, res)

    def test_MMMDCCXXIX(self):
        res = convert_to_arabic('MMMDCCXXIX')
        self.assertEqual(3729, res)

    def test_MMMDCCXXX(self):
        res = convert_to_arabic('MMMDCCXXX')
        self.assertEqual(3730, res)

    def test_MMMDCCXXXI(self):
        res = convert_to_arabic('MMMDCCXXXI')
        self.assertEqual(3731, res)

    def test_MMMDCCXXXII(self):
        res = convert_to_arabic('MMMDCCXXXII')
        self.assertEqual(3732, res)

    def test_MMMDCCXXXIII(self):
        res = convert_to_arabic('MMMDCCXXXIII')
        self.assertEqual(3733, res)

    def test_MMMDCCXXXIV(self):
        res = convert_to_arabic('MMMDCCXXXIV')
        self.assertEqual(3734, res)

    def test_MMMDCCXXXV(self):
        res = convert_to_arabic('MMMDCCXXXV')
        self.assertEqual(3735, res)

    def test_MMMDCCXXXVI(self):
        res = convert_to_arabic('MMMDCCXXXVI')
        self.assertEqual(3736, res)

    def test_MMMDCCXXXVII(self):
        res = convert_to_arabic('MMMDCCXXXVII')
        self.assertEqual(3737, res)

    def test_MMMDCCXXXVIII(self):
        res = convert_to_arabic('MMMDCCXXXVIII')
        self.assertEqual(3738, res)

    def test_MMMDCCXXXIX(self):
        res = convert_to_arabic('MMMDCCXXXIX')
        self.assertEqual(3739, res)

    def test_MMMDCCXL(self):
        res = convert_to_arabic('MMMDCCXL')
        self.assertEqual(3740, res)

    def test_MMMDCCXLI(self):
        res = convert_to_arabic('MMMDCCXLI')
        self.assertEqual(3741, res)

    def test_MMMDCCXLII(self):
        res = convert_to_arabic('MMMDCCXLII')
        self.assertEqual(3742, res)

    def test_MMMDCCXLIII(self):
        res = convert_to_arabic('MMMDCCXLIII')
        self.assertEqual(3743, res)

    def test_MMMDCCXLIV(self):
        res = convert_to_arabic('MMMDCCXLIV')
        self.assertEqual(3744, res)

    def test_MMMDCCXLV(self):
        res = convert_to_arabic('MMMDCCXLV')
        self.assertEqual(3745, res)

    def test_MMMDCCXLVI(self):
        res = convert_to_arabic('MMMDCCXLVI')
        self.assertEqual(3746, res)

    def test_MMMDCCXLVII(self):
        res = convert_to_arabic('MMMDCCXLVII')
        self.assertEqual(3747, res)

    def test_MMMDCCXLVIII(self):
        res = convert_to_arabic('MMMDCCXLVIII')
        self.assertEqual(3748, res)

    def test_MMMDCCXLIX(self):
        res = convert_to_arabic('MMMDCCXLIX')
        self.assertEqual(3749, res)

    def test_MMMDCCL(self):
        res = convert_to_arabic('MMMDCCL')
        self.assertEqual(3750, res)

    def test_MMMDCCLI(self):
        res = convert_to_arabic('MMMDCCLI')
        self.assertEqual(3751, res)

    def test_MMMDCCLII(self):
        res = convert_to_arabic('MMMDCCLII')
        self.assertEqual(3752, res)

    def test_MMMDCCLIII(self):
        res = convert_to_arabic('MMMDCCLIII')
        self.assertEqual(3753, res)

    def test_MMMDCCLIV(self):
        res = convert_to_arabic('MMMDCCLIV')
        self.assertEqual(3754, res)

    def test_MMMDCCLV(self):
        res = convert_to_arabic('MMMDCCLV')
        self.assertEqual(3755, res)

    def test_MMMDCCLVI(self):
        res = convert_to_arabic('MMMDCCLVI')
        self.assertEqual(3756, res)

    def test_MMMDCCLVII(self):
        res = convert_to_arabic('MMMDCCLVII')
        self.assertEqual(3757, res)

    def test_MMMDCCLVIII(self):
        res = convert_to_arabic('MMMDCCLVIII')
        self.assertEqual(3758, res)

    def test_MMMDCCLIX(self):
        res = convert_to_arabic('MMMDCCLIX')
        self.assertEqual(3759, res)

    def test_MMMDCCLX(self):
        res = convert_to_arabic('MMMDCCLX')
        self.assertEqual(3760, res)

    def test_MMMDCCLXI(self):
        res = convert_to_arabic('MMMDCCLXI')
        self.assertEqual(3761, res)

    def test_MMMDCCLXII(self):
        res = convert_to_arabic('MMMDCCLXII')
        self.assertEqual(3762, res)

    def test_MMMDCCLXIII(self):
        res = convert_to_arabic('MMMDCCLXIII')
        self.assertEqual(3763, res)

    def test_MMMDCCLXIV(self):
        res = convert_to_arabic('MMMDCCLXIV')
        self.assertEqual(3764, res)

    def test_MMMDCCLXV(self):
        res = convert_to_arabic('MMMDCCLXV')
        self.assertEqual(3765, res)

    def test_MMMDCCLXVI(self):
        res = convert_to_arabic('MMMDCCLXVI')
        self.assertEqual(3766, res)

    def test_MMMDCCLXVII(self):
        res = convert_to_arabic('MMMDCCLXVII')
        self.assertEqual(3767, res)

    def test_MMMDCCLXVIII(self):
        res = convert_to_arabic('MMMDCCLXVIII')
        self.assertEqual(3768, res)

    def test_MMMDCCLXIX(self):
        res = convert_to_arabic('MMMDCCLXIX')
        self.assertEqual(3769, res)

    def test_MMMDCCLXX(self):
        res = convert_to_arabic('MMMDCCLXX')
        self.assertEqual(3770, res)

    def test_MMMDCCLXXI(self):
        res = convert_to_arabic('MMMDCCLXXI')
        self.assertEqual(3771, res)

    def test_MMMDCCLXXII(self):
        res = convert_to_arabic('MMMDCCLXXII')
        self.assertEqual(3772, res)

    def test_MMMDCCLXXIII(self):
        res = convert_to_arabic('MMMDCCLXXIII')
        self.assertEqual(3773, res)

    def test_MMMDCCLXXIV(self):
        res = convert_to_arabic('MMMDCCLXXIV')
        self.assertEqual(3774, res)

    def test_MMMDCCLXXV(self):
        res = convert_to_arabic('MMMDCCLXXV')
        self.assertEqual(3775, res)

    def test_MMMDCCLXXVI(self):
        res = convert_to_arabic('MMMDCCLXXVI')
        self.assertEqual(3776, res)

    def test_MMMDCCLXXVII(self):
        res = convert_to_arabic('MMMDCCLXXVII')
        self.assertEqual(3777, res)

    def test_MMMDCCLXXVIII(self):
        res = convert_to_arabic('MMMDCCLXXVIII')
        self.assertEqual(3778, res)

    def test_MMMDCCLXXIX(self):
        res = convert_to_arabic('MMMDCCLXXIX')
        self.assertEqual(3779, res)

    def test_MMMDCCLXXX(self):
        res = convert_to_arabic('MMMDCCLXXX')
        self.assertEqual(3780, res)

    def test_MMMDCCLXXXI(self):
        res = convert_to_arabic('MMMDCCLXXXI')
        self.assertEqual(3781, res)

    def test_MMMDCCLXXXII(self):
        res = convert_to_arabic('MMMDCCLXXXII')
        self.assertEqual(3782, res)

    def test_MMMDCCLXXXIII(self):
        res = convert_to_arabic('MMMDCCLXXXIII')
        self.assertEqual(3783, res)

    def test_MMMDCCLXXXIV(self):
        res = convert_to_arabic('MMMDCCLXXXIV')
        self.assertEqual(3784, res)

    def test_MMMDCCLXXXV(self):
        res = convert_to_arabic('MMMDCCLXXXV')
        self.assertEqual(3785, res)

    def test_MMMDCCLXXXVI(self):
        res = convert_to_arabic('MMMDCCLXXXVI')
        self.assertEqual(3786, res)

    def test_MMMDCCLXXXVII(self):
        res = convert_to_arabic('MMMDCCLXXXVII')
        self.assertEqual(3787, res)

    def test_MMMDCCLXXXVIII(self):
        res = convert_to_arabic('MMMDCCLXXXVIII')
        self.assertEqual(3788, res)

    def test_MMMDCCLXXXIX(self):
        res = convert_to_arabic('MMMDCCLXXXIX')
        self.assertEqual(3789, res)

    def test_MMMDCCXC(self):
        res = convert_to_arabic('MMMDCCXC')
        self.assertEqual(3790, res)

    def test_MMMDCCXCI(self):
        res = convert_to_arabic('MMMDCCXCI')
        self.assertEqual(3791, res)

    def test_MMMDCCXCII(self):
        res = convert_to_arabic('MMMDCCXCII')
        self.assertEqual(3792, res)

    def test_MMMDCCXCIII(self):
        res = convert_to_arabic('MMMDCCXCIII')
        self.assertEqual(3793, res)

    def test_MMMDCCXCIV(self):
        res = convert_to_arabic('MMMDCCXCIV')
        self.assertEqual(3794, res)

    def test_MMMDCCXCV(self):
        res = convert_to_arabic('MMMDCCXCV')
        self.assertEqual(3795, res)

    def test_MMMDCCXCVI(self):
        res = convert_to_arabic('MMMDCCXCVI')
        self.assertEqual(3796, res)

    def test_MMMDCCXCVII(self):
        res = convert_to_arabic('MMMDCCXCVII')
        self.assertEqual(3797, res)

    def test_MMMDCCXCVIII(self):
        res = convert_to_arabic('MMMDCCXCVIII')
        self.assertEqual(3798, res)

    def test_MMMDCCXCIX(self):
        res = convert_to_arabic('MMMDCCXCIX')
        self.assertEqual(3799, res)

    def test_MMMDCCC(self):
        res = convert_to_arabic('MMMDCCC')
        self.assertEqual(3800, res)

    def test_MMMDCCCI(self):
        res = convert_to_arabic('MMMDCCCI')
        self.assertEqual(3801, res)

    def test_MMMDCCCII(self):
        res = convert_to_arabic('MMMDCCCII')
        self.assertEqual(3802, res)

    def test_MMMDCCCIII(self):
        res = convert_to_arabic('MMMDCCCIII')
        self.assertEqual(3803, res)

    def test_MMMDCCCIV(self):
        res = convert_to_arabic('MMMDCCCIV')
        self.assertEqual(3804, res)

    def test_MMMDCCCV(self):
        res = convert_to_arabic('MMMDCCCV')
        self.assertEqual(3805, res)

    def test_MMMDCCCVI(self):
        res = convert_to_arabic('MMMDCCCVI')
        self.assertEqual(3806, res)

    def test_MMMDCCCVII(self):
        res = convert_to_arabic('MMMDCCCVII')
        self.assertEqual(3807, res)

    def test_MMMDCCCVIII(self):
        res = convert_to_arabic('MMMDCCCVIII')
        self.assertEqual(3808, res)

    def test_MMMDCCCIX(self):
        res = convert_to_arabic('MMMDCCCIX')
        self.assertEqual(3809, res)

    def test_MMMDCCCX(self):
        res = convert_to_arabic('MMMDCCCX')
        self.assertEqual(3810, res)

    def test_MMMDCCCXI(self):
        res = convert_to_arabic('MMMDCCCXI')
        self.assertEqual(3811, res)

    def test_MMMDCCCXII(self):
        res = convert_to_arabic('MMMDCCCXII')
        self.assertEqual(3812, res)

    def test_MMMDCCCXIII(self):
        res = convert_to_arabic('MMMDCCCXIII')
        self.assertEqual(3813, res)

    def test_MMMDCCCXIV(self):
        res = convert_to_arabic('MMMDCCCXIV')
        self.assertEqual(3814, res)

    def test_MMMDCCCXV(self):
        res = convert_to_arabic('MMMDCCCXV')
        self.assertEqual(3815, res)

    def test_MMMDCCCXVI(self):
        res = convert_to_arabic('MMMDCCCXVI')
        self.assertEqual(3816, res)

    def test_MMMDCCCXVII(self):
        res = convert_to_arabic('MMMDCCCXVII')
        self.assertEqual(3817, res)

    def test_MMMDCCCXVIII(self):
        res = convert_to_arabic('MMMDCCCXVIII')
        self.assertEqual(3818, res)

    def test_MMMDCCCXIX(self):
        res = convert_to_arabic('MMMDCCCXIX')
        self.assertEqual(3819, res)

    def test_MMMDCCCXX(self):
        res = convert_to_arabic('MMMDCCCXX')
        self.assertEqual(3820, res)

    def test_MMMDCCCXXI(self):
        res = convert_to_arabic('MMMDCCCXXI')
        self.assertEqual(3821, res)

    def test_MMMDCCCXXII(self):
        res = convert_to_arabic('MMMDCCCXXII')
        self.assertEqual(3822, res)

    def test_MMMDCCCXXIII(self):
        res = convert_to_arabic('MMMDCCCXXIII')
        self.assertEqual(3823, res)

    def test_MMMDCCCXXIV(self):
        res = convert_to_arabic('MMMDCCCXXIV')
        self.assertEqual(3824, res)

    def test_MMMDCCCXXV(self):
        res = convert_to_arabic('MMMDCCCXXV')
        self.assertEqual(3825, res)

    def test_MMMDCCCXXVI(self):
        res = convert_to_arabic('MMMDCCCXXVI')
        self.assertEqual(3826, res)

    def test_MMMDCCCXXVII(self):
        res = convert_to_arabic('MMMDCCCXXVII')
        self.assertEqual(3827, res)

    def test_MMMDCCCXXVIII(self):
        res = convert_to_arabic('MMMDCCCXXVIII')
        self.assertEqual(3828, res)

    def test_MMMDCCCXXIX(self):
        res = convert_to_arabic('MMMDCCCXXIX')
        self.assertEqual(3829, res)

    def test_MMMDCCCXXX(self):
        res = convert_to_arabic('MMMDCCCXXX')
        self.assertEqual(3830, res)

    def test_MMMDCCCXXXI(self):
        res = convert_to_arabic('MMMDCCCXXXI')
        self.assertEqual(3831, res)

    def test_MMMDCCCXXXII(self):
        res = convert_to_arabic('MMMDCCCXXXII')
        self.assertEqual(3832, res)

    def test_MMMDCCCXXXIII(self):
        res = convert_to_arabic('MMMDCCCXXXIII')
        self.assertEqual(3833, res)

    def test_MMMDCCCXXXIV(self):
        res = convert_to_arabic('MMMDCCCXXXIV')
        self.assertEqual(3834, res)

    def test_MMMDCCCXXXV(self):
        res = convert_to_arabic('MMMDCCCXXXV')
        self.assertEqual(3835, res)

    def test_MMMDCCCXXXVI(self):
        res = convert_to_arabic('MMMDCCCXXXVI')
        self.assertEqual(3836, res)

    def test_MMMDCCCXXXVII(self):
        res = convert_to_arabic('MMMDCCCXXXVII')
        self.assertEqual(3837, res)

    def test_MMMDCCCXXXVIII(self):
        res = convert_to_arabic('MMMDCCCXXXVIII')
        self.assertEqual(3838, res)

    def test_MMMDCCCXXXIX(self):
        res = convert_to_arabic('MMMDCCCXXXIX')
        self.assertEqual(3839, res)

    def test_MMMDCCCXL(self):
        res = convert_to_arabic('MMMDCCCXL')
        self.assertEqual(3840, res)

    def test_MMMDCCCXLI(self):
        res = convert_to_arabic('MMMDCCCXLI')
        self.assertEqual(3841, res)

    def test_MMMDCCCXLII(self):
        res = convert_to_arabic('MMMDCCCXLII')
        self.assertEqual(3842, res)

    def test_MMMDCCCXLIII(self):
        res = convert_to_arabic('MMMDCCCXLIII')
        self.assertEqual(3843, res)

    def test_MMMDCCCXLIV(self):
        res = convert_to_arabic('MMMDCCCXLIV')
        self.assertEqual(3844, res)

    def test_MMMDCCCXLV(self):
        res = convert_to_arabic('MMMDCCCXLV')
        self.assertEqual(3845, res)

    def test_MMMDCCCXLVI(self):
        res = convert_to_arabic('MMMDCCCXLVI')
        self.assertEqual(3846, res)

    def test_MMMDCCCXLVII(self):
        res = convert_to_arabic('MMMDCCCXLVII')
        self.assertEqual(3847, res)

    def test_MMMDCCCXLVIII(self):
        res = convert_to_arabic('MMMDCCCXLVIII')
        self.assertEqual(3848, res)

    def test_MMMDCCCXLIX(self):
        res = convert_to_arabic('MMMDCCCXLIX')
        self.assertEqual(3849, res)

    def test_MMMDCCCL(self):
        res = convert_to_arabic('MMMDCCCL')
        self.assertEqual(3850, res)

    def test_MMMDCCCLI(self):
        res = convert_to_arabic('MMMDCCCLI')
        self.assertEqual(3851, res)

    def test_MMMDCCCLII(self):
        res = convert_to_arabic('MMMDCCCLII')
        self.assertEqual(3852, res)

    def test_MMMDCCCLIII(self):
        res = convert_to_arabic('MMMDCCCLIII')
        self.assertEqual(3853, res)

    def test_MMMDCCCLIV(self):
        res = convert_to_arabic('MMMDCCCLIV')
        self.assertEqual(3854, res)

    def test_MMMDCCCLV(self):
        res = convert_to_arabic('MMMDCCCLV')
        self.assertEqual(3855, res)

    def test_MMMDCCCLVI(self):
        res = convert_to_arabic('MMMDCCCLVI')
        self.assertEqual(3856, res)

    def test_MMMDCCCLVII(self):
        res = convert_to_arabic('MMMDCCCLVII')
        self.assertEqual(3857, res)

    def test_MMMDCCCLVIII(self):
        res = convert_to_arabic('MMMDCCCLVIII')
        self.assertEqual(3858, res)

    def test_MMMDCCCLIX(self):
        res = convert_to_arabic('MMMDCCCLIX')
        self.assertEqual(3859, res)

    def test_MMMDCCCLX(self):
        res = convert_to_arabic('MMMDCCCLX')
        self.assertEqual(3860, res)

    def test_MMMDCCCLXI(self):
        res = convert_to_arabic('MMMDCCCLXI')
        self.assertEqual(3861, res)

    def test_MMMDCCCLXII(self):
        res = convert_to_arabic('MMMDCCCLXII')
        self.assertEqual(3862, res)

    def test_MMMDCCCLXIII(self):
        res = convert_to_arabic('MMMDCCCLXIII')
        self.assertEqual(3863, res)

    def test_MMMDCCCLXIV(self):
        res = convert_to_arabic('MMMDCCCLXIV')
        self.assertEqual(3864, res)

    def test_MMMDCCCLXV(self):
        res = convert_to_arabic('MMMDCCCLXV')
        self.assertEqual(3865, res)

    def test_MMMDCCCLXVI(self):
        res = convert_to_arabic('MMMDCCCLXVI')
        self.assertEqual(3866, res)

    def test_MMMDCCCLXVII(self):
        res = convert_to_arabic('MMMDCCCLXVII')
        self.assertEqual(3867, res)

    def test_MMMDCCCLXVIII(self):
        res = convert_to_arabic('MMMDCCCLXVIII')
        self.assertEqual(3868, res)

    def test_MMMDCCCLXIX(self):
        res = convert_to_arabic('MMMDCCCLXIX')
        self.assertEqual(3869, res)

    def test_MMMDCCCLXX(self):
        res = convert_to_arabic('MMMDCCCLXX')
        self.assertEqual(3870, res)

    def test_MMMDCCCLXXI(self):
        res = convert_to_arabic('MMMDCCCLXXI')
        self.assertEqual(3871, res)

    def test_MMMDCCCLXXII(self):
        res = convert_to_arabic('MMMDCCCLXXII')
        self.assertEqual(3872, res)

    def test_MMMDCCCLXXIII(self):
        res = convert_to_arabic('MMMDCCCLXXIII')
        self.assertEqual(3873, res)

    def test_MMMDCCCLXXIV(self):
        res = convert_to_arabic('MMMDCCCLXXIV')
        self.assertEqual(3874, res)

    def test_MMMDCCCLXXV(self):
        res = convert_to_arabic('MMMDCCCLXXV')
        self.assertEqual(3875, res)

    def test_MMMDCCCLXXVI(self):
        res = convert_to_arabic('MMMDCCCLXXVI')
        self.assertEqual(3876, res)

    def test_MMMDCCCLXXVII(self):
        res = convert_to_arabic('MMMDCCCLXXVII')
        self.assertEqual(3877, res)

    def test_MMMDCCCLXXVIII(self):
        res = convert_to_arabic('MMMDCCCLXXVIII')
        self.assertEqual(3878, res)

    def test_MMMDCCCLXXIX(self):
        res = convert_to_arabic('MMMDCCCLXXIX')
        self.assertEqual(3879, res)

    def test_MMMDCCCLXXX(self):
        res = convert_to_arabic('MMMDCCCLXXX')
        self.assertEqual(3880, res)

    def test_MMMDCCCLXXXI(self):
        res = convert_to_arabic('MMMDCCCLXXXI')
        self.assertEqual(3881, res)

    def test_MMMDCCCLXXXII(self):
        res = convert_to_arabic('MMMDCCCLXXXII')
        self.assertEqual(3882, res)

    def test_MMMDCCCLXXXIII(self):
        res = convert_to_arabic('MMMDCCCLXXXIII')
        self.assertEqual(3883, res)

    def test_MMMDCCCLXXXIV(self):
        res = convert_to_arabic('MMMDCCCLXXXIV')
        self.assertEqual(3884, res)

    def test_MMMDCCCLXXXV(self):
        res = convert_to_arabic('MMMDCCCLXXXV')
        self.assertEqual(3885, res)

    def test_MMMDCCCLXXXVI(self):
        res = convert_to_arabic('MMMDCCCLXXXVI')
        self.assertEqual(3886, res)

    def test_MMMDCCCLXXXVII(self):
        res = convert_to_arabic('MMMDCCCLXXXVII')
        self.assertEqual(3887, res)

    def test_MMMDCCCLXXXVIII(self):
        res = convert_to_arabic('MMMDCCCLXXXVIII')
        self.assertEqual(3888, res)

    def test_MMMDCCCLXXXIX(self):
        res = convert_to_arabic('MMMDCCCLXXXIX')
        self.assertEqual(3889, res)

    def test_MMMDCCCXC(self):
        res = convert_to_arabic('MMMDCCCXC')
        self.assertEqual(3890, res)

    def test_MMMDCCCXCI(self):
        res = convert_to_arabic('MMMDCCCXCI')
        self.assertEqual(3891, res)

    def test_MMMDCCCXCII(self):
        res = convert_to_arabic('MMMDCCCXCII')
        self.assertEqual(3892, res)

    def test_MMMDCCCXCIII(self):
        res = convert_to_arabic('MMMDCCCXCIII')
        self.assertEqual(3893, res)

    def test_MMMDCCCXCIV(self):
        res = convert_to_arabic('MMMDCCCXCIV')
        self.assertEqual(3894, res)

    def test_MMMDCCCXCV(self):
        res = convert_to_arabic('MMMDCCCXCV')
        self.assertEqual(3895, res)

    def test_MMMDCCCXCVI(self):
        res = convert_to_arabic('MMMDCCCXCVI')
        self.assertEqual(3896, res)

    def test_MMMDCCCXCVII(self):
        res = convert_to_arabic('MMMDCCCXCVII')
        self.assertEqual(3897, res)

    def test_MMMDCCCXCVIII(self):
        res = convert_to_arabic('MMMDCCCXCVIII')
        self.assertEqual(3898, res)

    def test_MMMDCCCXCIX(self):
        res = convert_to_arabic('MMMDCCCXCIX')
        self.assertEqual(3899, res)

    def test_MMMCM(self):
        res = convert_to_arabic('MMMCM')
        self.assertEqual(3900, res)

    def test_MMMCMI(self):
        res = convert_to_arabic('MMMCMI')
        self.assertEqual(3901, res)

    def test_MMMCMII(self):
        res = convert_to_arabic('MMMCMII')
        self.assertEqual(3902, res)

    def test_MMMCMIII(self):
        res = convert_to_arabic('MMMCMIII')
        self.assertEqual(3903, res)

    def test_MMMCMIV(self):
        res = convert_to_arabic('MMMCMIV')
        self.assertEqual(3904, res)

    def test_MMMCMV(self):
        res = convert_to_arabic('MMMCMV')
        self.assertEqual(3905, res)

    def test_MMMCMVI(self):
        res = convert_to_arabic('MMMCMVI')
        self.assertEqual(3906, res)

    def test_MMMCMVII(self):
        res = convert_to_arabic('MMMCMVII')
        self.assertEqual(3907, res)

    def test_MMMCMVIII(self):
        res = convert_to_arabic('MMMCMVIII')
        self.assertEqual(3908, res)

    def test_MMMCMIX(self):
        res = convert_to_arabic('MMMCMIX')
        self.assertEqual(3909, res)

    def test_MMMCMX(self):
        res = convert_to_arabic('MMMCMX')
        self.assertEqual(3910, res)

    def test_MMMCMXI(self):
        res = convert_to_arabic('MMMCMXI')
        self.assertEqual(3911, res)

    def test_MMMCMXII(self):
        res = convert_to_arabic('MMMCMXII')
        self.assertEqual(3912, res)

    def test_MMMCMXIII(self):
        res = convert_to_arabic('MMMCMXIII')
        self.assertEqual(3913, res)

    def test_MMMCMXIV(self):
        res = convert_to_arabic('MMMCMXIV')
        self.assertEqual(3914, res)

    def test_MMMCMXV(self):
        res = convert_to_arabic('MMMCMXV')
        self.assertEqual(3915, res)

    def test_MMMCMXVI(self):
        res = convert_to_arabic('MMMCMXVI')
        self.assertEqual(3916, res)

    def test_MMMCMXVII(self):
        res = convert_to_arabic('MMMCMXVII')
        self.assertEqual(3917, res)

    def test_MMMCMXVIII(self):
        res = convert_to_arabic('MMMCMXVIII')
        self.assertEqual(3918, res)

    def test_MMMCMXIX(self):
        res = convert_to_arabic('MMMCMXIX')
        self.assertEqual(3919, res)

    def test_MMMCMXX(self):
        res = convert_to_arabic('MMMCMXX')
        self.assertEqual(3920, res)

    def test_MMMCMXXI(self):
        res = convert_to_arabic('MMMCMXXI')
        self.assertEqual(3921, res)

    def test_MMMCMXXII(self):
        res = convert_to_arabic('MMMCMXXII')
        self.assertEqual(3922, res)

    def test_MMMCMXXIII(self):
        res = convert_to_arabic('MMMCMXXIII')
        self.assertEqual(3923, res)

    def test_MMMCMXXIV(self):
        res = convert_to_arabic('MMMCMXXIV')
        self.assertEqual(3924, res)

    def test_MMMCMXXV(self):
        res = convert_to_arabic('MMMCMXXV')
        self.assertEqual(3925, res)

    def test_MMMCMXXVI(self):
        res = convert_to_arabic('MMMCMXXVI')
        self.assertEqual(3926, res)

    def test_MMMCMXXVII(self):
        res = convert_to_arabic('MMMCMXXVII')
        self.assertEqual(3927, res)

    def test_MMMCMXXVIII(self):
        res = convert_to_arabic('MMMCMXXVIII')
        self.assertEqual(3928, res)

    def test_MMMCMXXIX(self):
        res = convert_to_arabic('MMMCMXXIX')
        self.assertEqual(3929, res)

    def test_MMMCMXXX(self):
        res = convert_to_arabic('MMMCMXXX')
        self.assertEqual(3930, res)

    def test_MMMCMXXXI(self):
        res = convert_to_arabic('MMMCMXXXI')
        self.assertEqual(3931, res)

    def test_MMMCMXXXII(self):
        res = convert_to_arabic('MMMCMXXXII')
        self.assertEqual(3932, res)

    def test_MMMCMXXXIII(self):
        res = convert_to_arabic('MMMCMXXXIII')
        self.assertEqual(3933, res)

    def test_MMMCMXXXIV(self):
        res = convert_to_arabic('MMMCMXXXIV')
        self.assertEqual(3934, res)

    def test_MMMCMXXXV(self):
        res = convert_to_arabic('MMMCMXXXV')
        self.assertEqual(3935, res)

    def test_MMMCMXXXVI(self):
        res = convert_to_arabic('MMMCMXXXVI')
        self.assertEqual(3936, res)

    def test_MMMCMXXXVII(self):
        res = convert_to_arabic('MMMCMXXXVII')
        self.assertEqual(3937, res)

    def test_MMMCMXXXVIII(self):
        res = convert_to_arabic('MMMCMXXXVIII')
        self.assertEqual(3938, res)

    def test_MMMCMXXXIX(self):
        res = convert_to_arabic('MMMCMXXXIX')
        self.assertEqual(3939, res)

    def test_MMMCMXL(self):
        res = convert_to_arabic('MMMCMXL')
        self.assertEqual(3940, res)

    def test_MMMCMXLI(self):
        res = convert_to_arabic('MMMCMXLI')
        self.assertEqual(3941, res)

    def test_MMMCMXLII(self):
        res = convert_to_arabic('MMMCMXLII')
        self.assertEqual(3942, res)

    def test_MMMCMXLIII(self):
        res = convert_to_arabic('MMMCMXLIII')
        self.assertEqual(3943, res)

    def test_MMMCMXLIV(self):
        res = convert_to_arabic('MMMCMXLIV')
        self.assertEqual(3944, res)

    def test_MMMCMXLV(self):
        res = convert_to_arabic('MMMCMXLV')
        self.assertEqual(3945, res)

    def test_MMMCMXLVI(self):
        res = convert_to_arabic('MMMCMXLVI')
        self.assertEqual(3946, res)

    def test_MMMCMXLVII(self):
        res = convert_to_arabic('MMMCMXLVII')
        self.assertEqual(3947, res)

    def test_MMMCMXLVIII(self):
        res = convert_to_arabic('MMMCMXLVIII')
        self.assertEqual(3948, res)

    def test_MMMCMXLIX(self):
        res = convert_to_arabic('MMMCMXLIX')
        self.assertEqual(3949, res)

    def test_MMMCML(self):
        res = convert_to_arabic('MMMCML')
        self.assertEqual(3950, res)

    def test_MMMCMLI(self):
        res = convert_to_arabic('MMMCMLI')
        self.assertEqual(3951, res)

    def test_MMMCMLII(self):
        res = convert_to_arabic('MMMCMLII')
        self.assertEqual(3952, res)

    def test_MMMCMLIII(self):
        res = convert_to_arabic('MMMCMLIII')
        self.assertEqual(3953, res)

    def test_MMMCMLIV(self):
        res = convert_to_arabic('MMMCMLIV')
        self.assertEqual(3954, res)

    def test_MMMCMLV(self):
        res = convert_to_arabic('MMMCMLV')
        self.assertEqual(3955, res)

    def test_MMMCMLVI(self):
        res = convert_to_arabic('MMMCMLVI')
        self.assertEqual(3956, res)

    def test_MMMCMLVII(self):
        res = convert_to_arabic('MMMCMLVII')
        self.assertEqual(3957, res)

    def test_MMMCMLVIII(self):
        res = convert_to_arabic('MMMCMLVIII')
        self.assertEqual(3958, res)

    def test_MMMCMLIX(self):
        res = convert_to_arabic('MMMCMLIX')
        self.assertEqual(3959, res)

    def test_MMMCMLX(self):
        res = convert_to_arabic('MMMCMLX')
        self.assertEqual(3960, res)

    def test_MMMCMLXI(self):
        res = convert_to_arabic('MMMCMLXI')
        self.assertEqual(3961, res)

    def test_MMMCMLXII(self):
        res = convert_to_arabic('MMMCMLXII')
        self.assertEqual(3962, res)

    def test_MMMCMLXIII(self):
        res = convert_to_arabic('MMMCMLXIII')
        self.assertEqual(3963, res)

    def test_MMMCMLXIV(self):
        res = convert_to_arabic('MMMCMLXIV')
        self.assertEqual(3964, res)

    def test_MMMCMLXV(self):
        res = convert_to_arabic('MMMCMLXV')
        self.assertEqual(3965, res)

    def test_MMMCMLXVI(self):
        res = convert_to_arabic('MMMCMLXVI')
        self.assertEqual(3966, res)

    def test_MMMCMLXVII(self):
        res = convert_to_arabic('MMMCMLXVII')
        self.assertEqual(3967, res)

    def test_MMMCMLXVIII(self):
        res = convert_to_arabic('MMMCMLXVIII')
        self.assertEqual(3968, res)

    def test_MMMCMLXIX(self):
        res = convert_to_arabic('MMMCMLXIX')
        self.assertEqual(3969, res)

    def test_MMMCMLXX(self):
        res = convert_to_arabic('MMMCMLXX')
        self.assertEqual(3970, res)

    def test_MMMCMLXXI(self):
        res = convert_to_arabic('MMMCMLXXI')
        self.assertEqual(3971, res)

    def test_MMMCMLXXII(self):
        res = convert_to_arabic('MMMCMLXXII')
        self.assertEqual(3972, res)

    def test_MMMCMLXXIII(self):
        res = convert_to_arabic('MMMCMLXXIII')
        self.assertEqual(3973, res)

    def test_MMMCMLXXIV(self):
        res = convert_to_arabic('MMMCMLXXIV')
        self.assertEqual(3974, res)

    def test_MMMCMLXXV(self):
        res = convert_to_arabic('MMMCMLXXV')
        self.assertEqual(3975, res)

    def test_MMMCMLXXVI(self):
        res = convert_to_arabic('MMMCMLXXVI')
        self.assertEqual(3976, res)

    def test_MMMCMLXXVII(self):
        res = convert_to_arabic('MMMCMLXXVII')
        self.assertEqual(3977, res)

    def test_MMMCMLXXVIII(self):
        res = convert_to_arabic('MMMCMLXXVIII')
        self.assertEqual(3978, res)

    def test_MMMCMLXXIX(self):
        res = convert_to_arabic('MMMCMLXXIX')
        self.assertEqual(3979, res)

    def test_MMMCMLXXX(self):
        res = convert_to_arabic('MMMCMLXXX')
        self.assertEqual(3980, res)

    def test_MMMCMLXXXI(self):
        res = convert_to_arabic('MMMCMLXXXI')
        self.assertEqual(3981, res)

    def test_MMMCMLXXXII(self):
        res = convert_to_arabic('MMMCMLXXXII')
        self.assertEqual(3982, res)

    def test_MMMCMLXXXIII(self):
        res = convert_to_arabic('MMMCMLXXXIII')
        self.assertEqual(3983, res)

    def test_MMMCMLXXXIV(self):
        res = convert_to_arabic('MMMCMLXXXIV')
        self.assertEqual(3984, res)

    def test_MMMCMLXXXV(self):
        res = convert_to_arabic('MMMCMLXXXV')
        self.assertEqual(3985, res)

    def test_MMMCMLXXXVI(self):
        res = convert_to_arabic('MMMCMLXXXVI')
        self.assertEqual(3986, res)

    def test_MMMCMLXXXVII(self):
        res = convert_to_arabic('MMMCMLXXXVII')
        self.assertEqual(3987, res)

    def test_MMMCMLXXXVIII(self):
        res = convert_to_arabic('MMMCMLXXXVIII')
        self.assertEqual(3988, res)

    def test_MMMCMLXXXIX(self):
        res = convert_to_arabic('MMMCMLXXXIX')
        self.assertEqual(3989, res)

    def test_MMMCMXC(self):
        res = convert_to_arabic('MMMCMXC')
        self.assertEqual(3990, res)

    def test_MMMCMXCI(self):
        res = convert_to_arabic('MMMCMXCI')
        self.assertEqual(3991, res)

    def test_MMMCMXCII(self):
        res = convert_to_arabic('MMMCMXCII')
        self.assertEqual(3992, res)

    def test_MMMCMXCIII(self):
        res = convert_to_arabic('MMMCMXCIII')
        self.assertEqual(3993, res)

    def test_MMMCMXCIV(self):
        res = convert_to_arabic('MMMCMXCIV')
        self.assertEqual(3994, res)

    def test_MMMCMXCV(self):
        res = convert_to_arabic('MMMCMXCV')
        self.assertEqual(3995, res)

    def test_MMMCMXCVI(self):
        res = convert_to_arabic('MMMCMXCVI')
        self.assertEqual(3996, res)

    def test_MMMCMXCVII(self):
        res = convert_to_arabic('MMMCMXCVII')
        self.assertEqual(3997, res)

    def test_MMMCMXCVIII(self):
        res = convert_to_arabic('MMMCMXCVIII')
        self.assertEqual(3998, res)

    def test_MMMCMXCIX(self):
        res = convert_to_arabic('MMMCMXCIX')
        self.assertEqual(3999, res)

    def test_MMMM(self):
        res = convert_to_arabic('MMMM')
        self.assertEqual(4000, res)

    def test_MMMMI(self):
        res = convert_to_arabic('MMMMI')
        self.assertEqual(4001, res)

    def test_MMMMII(self):
        res = convert_to_arabic('MMMMII')
        self.assertEqual(4002, res)

    def test_MMMMIII(self):
        res = convert_to_arabic('MMMMIII')
        self.assertEqual(4003, res)

    def test_MMMMIV(self):
        res = convert_to_arabic('MMMMIV')
        self.assertEqual(4004, res)

    def test_MMMMV(self):
        res = convert_to_arabic('MMMMV')
        self.assertEqual(4005, res)

    def test_MMMMVI(self):
        res = convert_to_arabic('MMMMVI')
        self.assertEqual(4006, res)

    def test_MMMMVII(self):
        res = convert_to_arabic('MMMMVII')
        self.assertEqual(4007, res)

    def test_MMMMVIII(self):
        res = convert_to_arabic('MMMMVIII')
        self.assertEqual(4008, res)

    def test_MMMMIX(self):
        res = convert_to_arabic('MMMMIX')
        self.assertEqual(4009, res)

    def test_MMMMX(self):
        res = convert_to_arabic('MMMMX')
        self.assertEqual(4010, res)

    def test_MMMMXI(self):
        res = convert_to_arabic('MMMMXI')
        self.assertEqual(4011, res)

    def test_MMMMXII(self):
        res = convert_to_arabic('MMMMXII')
        self.assertEqual(4012, res)

    def test_MMMMXIII(self):
        res = convert_to_arabic('MMMMXIII')
        self.assertEqual(4013, res)

    def test_MMMMXIV(self):
        res = convert_to_arabic('MMMMXIV')
        self.assertEqual(4014, res)

    def test_MMMMXV(self):
        res = convert_to_arabic('MMMMXV')
        self.assertEqual(4015, res)

    def test_MMMMXVI(self):
        res = convert_to_arabic('MMMMXVI')
        self.assertEqual(4016, res)

    def test_MMMMXVII(self):
        res = convert_to_arabic('MMMMXVII')
        self.assertEqual(4017, res)

    def test_MMMMXVIII(self):
        res = convert_to_arabic('MMMMXVIII')
        self.assertEqual(4018, res)

    def test_MMMMXIX(self):
        res = convert_to_arabic('MMMMXIX')
        self.assertEqual(4019, res)

    def test_MMMMXX(self):
        res = convert_to_arabic('MMMMXX')
        self.assertEqual(4020, res)

    def test_MMMMXXI(self):
        res = convert_to_arabic('MMMMXXI')
        self.assertEqual(4021, res)

    def test_MMMMXXII(self):
        res = convert_to_arabic('MMMMXXII')
        self.assertEqual(4022, res)

    def test_MMMMXXIII(self):
        res = convert_to_arabic('MMMMXXIII')
        self.assertEqual(4023, res)

    def test_MMMMXXIV(self):
        res = convert_to_arabic('MMMMXXIV')
        self.assertEqual(4024, res)

    def test_MMMMXXV(self):
        res = convert_to_arabic('MMMMXXV')
        self.assertEqual(4025, res)

    def test_MMMMXXVI(self):
        res = convert_to_arabic('MMMMXXVI')
        self.assertEqual(4026, res)

    def test_MMMMXXVII(self):
        res = convert_to_arabic('MMMMXXVII')
        self.assertEqual(4027, res)

    def test_MMMMXXVIII(self):
        res = convert_to_arabic('MMMMXXVIII')
        self.assertEqual(4028, res)

    def test_MMMMXXIX(self):
        res = convert_to_arabic('MMMMXXIX')
        self.assertEqual(4029, res)

    def test_MMMMXXX(self):
        res = convert_to_arabic('MMMMXXX')
        self.assertEqual(4030, res)

    def test_MMMMXXXI(self):
        res = convert_to_arabic('MMMMXXXI')
        self.assertEqual(4031, res)

    def test_MMMMXXXII(self):
        res = convert_to_arabic('MMMMXXXII')
        self.assertEqual(4032, res)

    def test_MMMMXXXIII(self):
        res = convert_to_arabic('MMMMXXXIII')
        self.assertEqual(4033, res)

    def test_MMMMXXXIV(self):
        res = convert_to_arabic('MMMMXXXIV')
        self.assertEqual(4034, res)

    def test_MMMMXXXV(self):
        res = convert_to_arabic('MMMMXXXV')
        self.assertEqual(4035, res)

    def test_MMMMXXXVI(self):
        res = convert_to_arabic('MMMMXXXVI')
        self.assertEqual(4036, res)

    def test_MMMMXXXVII(self):
        res = convert_to_arabic('MMMMXXXVII')
        self.assertEqual(4037, res)

    def test_MMMMXXXVIII(self):
        res = convert_to_arabic('MMMMXXXVIII')
        self.assertEqual(4038, res)

    def test_MMMMXXXIX(self):
        res = convert_to_arabic('MMMMXXXIX')
        self.assertEqual(4039, res)

    def test_MMMMXL(self):
        res = convert_to_arabic('MMMMXL')
        self.assertEqual(4040, res)

    def test_MMMMXLI(self):
        res = convert_to_arabic('MMMMXLI')
        self.assertEqual(4041, res)

    def test_MMMMXLII(self):
        res = convert_to_arabic('MMMMXLII')
        self.assertEqual(4042, res)

    def test_MMMMXLIII(self):
        res = convert_to_arabic('MMMMXLIII')
        self.assertEqual(4043, res)

    def test_MMMMXLIV(self):
        res = convert_to_arabic('MMMMXLIV')
        self.assertEqual(4044, res)

    def test_MMMMXLV(self):
        res = convert_to_arabic('MMMMXLV')
        self.assertEqual(4045, res)

    def test_MMMMXLVI(self):
        res = convert_to_arabic('MMMMXLVI')
        self.assertEqual(4046, res)

    def test_MMMMXLVII(self):
        res = convert_to_arabic('MMMMXLVII')
        self.assertEqual(4047, res)

    def test_MMMMXLVIII(self):
        res = convert_to_arabic('MMMMXLVIII')
        self.assertEqual(4048, res)

    def test_MMMMXLIX(self):
        res = convert_to_arabic('MMMMXLIX')
        self.assertEqual(4049, res)

    def test_MMMML(self):
        res = convert_to_arabic('MMMML')
        self.assertEqual(4050, res)

    def test_MMMMLI(self):
        res = convert_to_arabic('MMMMLI')
        self.assertEqual(4051, res)

    def test_MMMMLII(self):
        res = convert_to_arabic('MMMMLII')
        self.assertEqual(4052, res)

    def test_MMMMLIII(self):
        res = convert_to_arabic('MMMMLIII')
        self.assertEqual(4053, res)

    def test_MMMMLIV(self):
        res = convert_to_arabic('MMMMLIV')
        self.assertEqual(4054, res)

    def test_MMMMLV(self):
        res = convert_to_arabic('MMMMLV')
        self.assertEqual(4055, res)

    def test_MMMMLVI(self):
        res = convert_to_arabic('MMMMLVI')
        self.assertEqual(4056, res)

    def test_MMMMLVII(self):
        res = convert_to_arabic('MMMMLVII')
        self.assertEqual(4057, res)

    def test_MMMMLVIII(self):
        res = convert_to_arabic('MMMMLVIII')
        self.assertEqual(4058, res)

    def test_MMMMLIX(self):
        res = convert_to_arabic('MMMMLIX')
        self.assertEqual(4059, res)

    def test_MMMMLX(self):
        res = convert_to_arabic('MMMMLX')
        self.assertEqual(4060, res)

    def test_MMMMLXI(self):
        res = convert_to_arabic('MMMMLXI')
        self.assertEqual(4061, res)

    def test_MMMMLXII(self):
        res = convert_to_arabic('MMMMLXII')
        self.assertEqual(4062, res)

    def test_MMMMLXIII(self):
        res = convert_to_arabic('MMMMLXIII')
        self.assertEqual(4063, res)

    def test_MMMMLXIV(self):
        res = convert_to_arabic('MMMMLXIV')
        self.assertEqual(4064, res)

    def test_MMMMLXV(self):
        res = convert_to_arabic('MMMMLXV')
        self.assertEqual(4065, res)

    def test_MMMMLXVI(self):
        res = convert_to_arabic('MMMMLXVI')
        self.assertEqual(4066, res)

    def test_MMMMLXVII(self):
        res = convert_to_arabic('MMMMLXVII')
        self.assertEqual(4067, res)

    def test_MMMMLXVIII(self):
        res = convert_to_arabic('MMMMLXVIII')
        self.assertEqual(4068, res)

    def test_MMMMLXIX(self):
        res = convert_to_arabic('MMMMLXIX')
        self.assertEqual(4069, res)

    def test_MMMMLXX(self):
        res = convert_to_arabic('MMMMLXX')
        self.assertEqual(4070, res)

    def test_MMMMLXXI(self):
        res = convert_to_arabic('MMMMLXXI')
        self.assertEqual(4071, res)

    def test_MMMMLXXII(self):
        res = convert_to_arabic('MMMMLXXII')
        self.assertEqual(4072, res)

    def test_MMMMLXXIII(self):
        res = convert_to_arabic('MMMMLXXIII')
        self.assertEqual(4073, res)

    def test_MMMMLXXIV(self):
        res = convert_to_arabic('MMMMLXXIV')
        self.assertEqual(4074, res)

    def test_MMMMLXXV(self):
        res = convert_to_arabic('MMMMLXXV')
        self.assertEqual(4075, res)

    def test_MMMMLXXVI(self):
        res = convert_to_arabic('MMMMLXXVI')
        self.assertEqual(4076, res)

    def test_MMMMLXXVII(self):
        res = convert_to_arabic('MMMMLXXVII')
        self.assertEqual(4077, res)

    def test_MMMMLXXVIII(self):
        res = convert_to_arabic('MMMMLXXVIII')
        self.assertEqual(4078, res)

    def test_MMMMLXXIX(self):
        res = convert_to_arabic('MMMMLXXIX')
        self.assertEqual(4079, res)

    def test_MMMMLXXX(self):
        res = convert_to_arabic('MMMMLXXX')
        self.assertEqual(4080, res)

    def test_MMMMLXXXI(self):
        res = convert_to_arabic('MMMMLXXXI')
        self.assertEqual(4081, res)

    def test_MMMMLXXXII(self):
        res = convert_to_arabic('MMMMLXXXII')
        self.assertEqual(4082, res)

    def test_MMMMLXXXIII(self):
        res = convert_to_arabic('MMMMLXXXIII')
        self.assertEqual(4083, res)

    def test_MMMMLXXXIV(self):
        res = convert_to_arabic('MMMMLXXXIV')
        self.assertEqual(4084, res)

    def test_MMMMLXXXV(self):
        res = convert_to_arabic('MMMMLXXXV')
        self.assertEqual(4085, res)

    def test_MMMMLXXXVI(self):
        res = convert_to_arabic('MMMMLXXXVI')
        self.assertEqual(4086, res)

    def test_MMMMLXXXVII(self):
        res = convert_to_arabic('MMMMLXXXVII')
        self.assertEqual(4087, res)

    def test_MMMMLXXXVIII(self):
        res = convert_to_arabic('MMMMLXXXVIII')
        self.assertEqual(4088, res)

    def test_MMMMLXXXIX(self):
        res = convert_to_arabic('MMMMLXXXIX')
        self.assertEqual(4089, res)

    def test_MMMMXC(self):
        res = convert_to_arabic('MMMMXC')
        self.assertEqual(4090, res)

    def test_MMMMXCI(self):
        res = convert_to_arabic('MMMMXCI')
        self.assertEqual(4091, res)

    def test_MMMMXCII(self):
        res = convert_to_arabic('MMMMXCII')
        self.assertEqual(4092, res)

    def test_MMMMXCIII(self):
        res = convert_to_arabic('MMMMXCIII')
        self.assertEqual(4093, res)

    def test_MMMMXCIV(self):
        res = convert_to_arabic('MMMMXCIV')
        self.assertEqual(4094, res)

    def test_MMMMXCV(self):
        res = convert_to_arabic('MMMMXCV')
        self.assertEqual(4095, res)

    def test_MMMMXCVI(self):
        res = convert_to_arabic('MMMMXCVI')
        self.assertEqual(4096, res)

    def test_MMMMXCVII(self):
        res = convert_to_arabic('MMMMXCVII')
        self.assertEqual(4097, res)

    def test_MMMMXCVIII(self):
        res = convert_to_arabic('MMMMXCVIII')
        self.assertEqual(4098, res)

    def test_MMMMXCIX(self):
        res = convert_to_arabic('MMMMXCIX')
        self.assertEqual(4099, res)

    def test_MMMMC(self):
        res = convert_to_arabic('MMMMC')
        self.assertEqual(4100, res)

    def test_MMMMCI(self):
        res = convert_to_arabic('MMMMCI')
        self.assertEqual(4101, res)

    def test_MMMMCII(self):
        res = convert_to_arabic('MMMMCII')
        self.assertEqual(4102, res)

    def test_MMMMCIII(self):
        res = convert_to_arabic('MMMMCIII')
        self.assertEqual(4103, res)

    def test_MMMMCIV(self):
        res = convert_to_arabic('MMMMCIV')
        self.assertEqual(4104, res)

    def test_MMMMCV(self):
        res = convert_to_arabic('MMMMCV')
        self.assertEqual(4105, res)

    def test_MMMMCVI(self):
        res = convert_to_arabic('MMMMCVI')
        self.assertEqual(4106, res)

    def test_MMMMCVII(self):
        res = convert_to_arabic('MMMMCVII')
        self.assertEqual(4107, res)

    def test_MMMMCVIII(self):
        res = convert_to_arabic('MMMMCVIII')
        self.assertEqual(4108, res)

    def test_MMMMCIX(self):
        res = convert_to_arabic('MMMMCIX')
        self.assertEqual(4109, res)

    def test_MMMMCX(self):
        res = convert_to_arabic('MMMMCX')
        self.assertEqual(4110, res)

    def test_MMMMCXI(self):
        res = convert_to_arabic('MMMMCXI')
        self.assertEqual(4111, res)

    def test_MMMMCXII(self):
        res = convert_to_arabic('MMMMCXII')
        self.assertEqual(4112, res)

    def test_MMMMCXIII(self):
        res = convert_to_arabic('MMMMCXIII')
        self.assertEqual(4113, res)

    def test_MMMMCXIV(self):
        res = convert_to_arabic('MMMMCXIV')
        self.assertEqual(4114, res)

    def test_MMMMCXV(self):
        res = convert_to_arabic('MMMMCXV')
        self.assertEqual(4115, res)

    def test_MMMMCXVI(self):
        res = convert_to_arabic('MMMMCXVI')
        self.assertEqual(4116, res)

    def test_MMMMCXVII(self):
        res = convert_to_arabic('MMMMCXVII')
        self.assertEqual(4117, res)

    def test_MMMMCXVIII(self):
        res = convert_to_arabic('MMMMCXVIII')
        self.assertEqual(4118, res)

    def test_MMMMCXIX(self):
        res = convert_to_arabic('MMMMCXIX')
        self.assertEqual(4119, res)

    def test_MMMMCXX(self):
        res = convert_to_arabic('MMMMCXX')
        self.assertEqual(4120, res)

    def test_MMMMCXXI(self):
        res = convert_to_arabic('MMMMCXXI')
        self.assertEqual(4121, res)

    def test_MMMMCXXII(self):
        res = convert_to_arabic('MMMMCXXII')
        self.assertEqual(4122, res)

    def test_MMMMCXXIII(self):
        res = convert_to_arabic('MMMMCXXIII')
        self.assertEqual(4123, res)

    def test_MMMMCXXIV(self):
        res = convert_to_arabic('MMMMCXXIV')
        self.assertEqual(4124, res)

    def test_MMMMCXXV(self):
        res = convert_to_arabic('MMMMCXXV')
        self.assertEqual(4125, res)

    def test_MMMMCXXVI(self):
        res = convert_to_arabic('MMMMCXXVI')
        self.assertEqual(4126, res)

    def test_MMMMCXXVII(self):
        res = convert_to_arabic('MMMMCXXVII')
        self.assertEqual(4127, res)

    def test_MMMMCXXVIII(self):
        res = convert_to_arabic('MMMMCXXVIII')
        self.assertEqual(4128, res)

    def test_MMMMCXXIX(self):
        res = convert_to_arabic('MMMMCXXIX')
        self.assertEqual(4129, res)

    def test_MMMMCXXX(self):
        res = convert_to_arabic('MMMMCXXX')
        self.assertEqual(4130, res)

    def test_MMMMCXXXI(self):
        res = convert_to_arabic('MMMMCXXXI')
        self.assertEqual(4131, res)

    def test_MMMMCXXXII(self):
        res = convert_to_arabic('MMMMCXXXII')
        self.assertEqual(4132, res)

    def test_MMMMCXXXIII(self):
        res = convert_to_arabic('MMMMCXXXIII')
        self.assertEqual(4133, res)

    def test_MMMMCXXXIV(self):
        res = convert_to_arabic('MMMMCXXXIV')
        self.assertEqual(4134, res)

    def test_MMMMCXXXV(self):
        res = convert_to_arabic('MMMMCXXXV')
        self.assertEqual(4135, res)

    def test_MMMMCXXXVI(self):
        res = convert_to_arabic('MMMMCXXXVI')
        self.assertEqual(4136, res)

    def test_MMMMCXXXVII(self):
        res = convert_to_arabic('MMMMCXXXVII')
        self.assertEqual(4137, res)

    def test_MMMMCXXXVIII(self):
        res = convert_to_arabic('MMMMCXXXVIII')
        self.assertEqual(4138, res)

    def test_MMMMCXXXIX(self):
        res = convert_to_arabic('MMMMCXXXIX')
        self.assertEqual(4139, res)

    def test_MMMMCXL(self):
        res = convert_to_arabic('MMMMCXL')
        self.assertEqual(4140, res)

    def test_MMMMCXLI(self):
        res = convert_to_arabic('MMMMCXLI')
        self.assertEqual(4141, res)

    def test_MMMMCXLII(self):
        res = convert_to_arabic('MMMMCXLII')
        self.assertEqual(4142, res)

    def test_MMMMCXLIII(self):
        res = convert_to_arabic('MMMMCXLIII')
        self.assertEqual(4143, res)

    def test_MMMMCXLIV(self):
        res = convert_to_arabic('MMMMCXLIV')
        self.assertEqual(4144, res)

    def test_MMMMCXLV(self):
        res = convert_to_arabic('MMMMCXLV')
        self.assertEqual(4145, res)

    def test_MMMMCXLVI(self):
        res = convert_to_arabic('MMMMCXLVI')
        self.assertEqual(4146, res)

    def test_MMMMCXLVII(self):
        res = convert_to_arabic('MMMMCXLVII')
        self.assertEqual(4147, res)

    def test_MMMMCXLVIII(self):
        res = convert_to_arabic('MMMMCXLVIII')
        self.assertEqual(4148, res)

    def test_MMMMCXLIX(self):
        res = convert_to_arabic('MMMMCXLIX')
        self.assertEqual(4149, res)

    def test_MMMMCL(self):
        res = convert_to_arabic('MMMMCL')
        self.assertEqual(4150, res)

    def test_MMMMCLI(self):
        res = convert_to_arabic('MMMMCLI')
        self.assertEqual(4151, res)

    def test_MMMMCLII(self):
        res = convert_to_arabic('MMMMCLII')
        self.assertEqual(4152, res)

    def test_MMMMCLIII(self):
        res = convert_to_arabic('MMMMCLIII')
        self.assertEqual(4153, res)

    def test_MMMMCLIV(self):
        res = convert_to_arabic('MMMMCLIV')
        self.assertEqual(4154, res)

    def test_MMMMCLV(self):
        res = convert_to_arabic('MMMMCLV')
        self.assertEqual(4155, res)

    def test_MMMMCLVI(self):
        res = convert_to_arabic('MMMMCLVI')
        self.assertEqual(4156, res)

    def test_MMMMCLVII(self):
        res = convert_to_arabic('MMMMCLVII')
        self.assertEqual(4157, res)

    def test_MMMMCLVIII(self):
        res = convert_to_arabic('MMMMCLVIII')
        self.assertEqual(4158, res)

    def test_MMMMCLIX(self):
        res = convert_to_arabic('MMMMCLIX')
        self.assertEqual(4159, res)

    def test_MMMMCLX(self):
        res = convert_to_arabic('MMMMCLX')
        self.assertEqual(4160, res)

    def test_MMMMCLXI(self):
        res = convert_to_arabic('MMMMCLXI')
        self.assertEqual(4161, res)

    def test_MMMMCLXII(self):
        res = convert_to_arabic('MMMMCLXII')
        self.assertEqual(4162, res)

    def test_MMMMCLXIII(self):
        res = convert_to_arabic('MMMMCLXIII')
        self.assertEqual(4163, res)

    def test_MMMMCLXIV(self):
        res = convert_to_arabic('MMMMCLXIV')
        self.assertEqual(4164, res)

    def test_MMMMCLXV(self):
        res = convert_to_arabic('MMMMCLXV')
        self.assertEqual(4165, res)

    def test_MMMMCLXVI(self):
        res = convert_to_arabic('MMMMCLXVI')
        self.assertEqual(4166, res)

    def test_MMMMCLXVII(self):
        res = convert_to_arabic('MMMMCLXVII')
        self.assertEqual(4167, res)

    def test_MMMMCLXVIII(self):
        res = convert_to_arabic('MMMMCLXVIII')
        self.assertEqual(4168, res)

    def test_MMMMCLXIX(self):
        res = convert_to_arabic('MMMMCLXIX')
        self.assertEqual(4169, res)

    def test_MMMMCLXX(self):
        res = convert_to_arabic('MMMMCLXX')
        self.assertEqual(4170, res)

    def test_MMMMCLXXI(self):
        res = convert_to_arabic('MMMMCLXXI')
        self.assertEqual(4171, res)

    def test_MMMMCLXXII(self):
        res = convert_to_arabic('MMMMCLXXII')
        self.assertEqual(4172, res)

    def test_MMMMCLXXIII(self):
        res = convert_to_arabic('MMMMCLXXIII')
        self.assertEqual(4173, res)

    def test_MMMMCLXXIV(self):
        res = convert_to_arabic('MMMMCLXXIV')
        self.assertEqual(4174, res)

    def test_MMMMCLXXV(self):
        res = convert_to_arabic('MMMMCLXXV')
        self.assertEqual(4175, res)

    def test_MMMMCLXXVI(self):
        res = convert_to_arabic('MMMMCLXXVI')
        self.assertEqual(4176, res)

    def test_MMMMCLXXVII(self):
        res = convert_to_arabic('MMMMCLXXVII')
        self.assertEqual(4177, res)

    def test_MMMMCLXXVIII(self):
        res = convert_to_arabic('MMMMCLXXVIII')
        self.assertEqual(4178, res)

    def test_MMMMCLXXIX(self):
        res = convert_to_arabic('MMMMCLXXIX')
        self.assertEqual(4179, res)

    def test_MMMMCLXXX(self):
        res = convert_to_arabic('MMMMCLXXX')
        self.assertEqual(4180, res)

    def test_MMMMCLXXXI(self):
        res = convert_to_arabic('MMMMCLXXXI')
        self.assertEqual(4181, res)

    def test_MMMMCLXXXII(self):
        res = convert_to_arabic('MMMMCLXXXII')
        self.assertEqual(4182, res)

    def test_MMMMCLXXXIII(self):
        res = convert_to_arabic('MMMMCLXXXIII')
        self.assertEqual(4183, res)

    def test_MMMMCLXXXIV(self):
        res = convert_to_arabic('MMMMCLXXXIV')
        self.assertEqual(4184, res)

    def test_MMMMCLXXXV(self):
        res = convert_to_arabic('MMMMCLXXXV')
        self.assertEqual(4185, res)

    def test_MMMMCLXXXVI(self):
        res = convert_to_arabic('MMMMCLXXXVI')
        self.assertEqual(4186, res)

    def test_MMMMCLXXXVII(self):
        res = convert_to_arabic('MMMMCLXXXVII')
        self.assertEqual(4187, res)

    def test_MMMMCLXXXVIII(self):
        res = convert_to_arabic('MMMMCLXXXVIII')
        self.assertEqual(4188, res)

    def test_MMMMCLXXXIX(self):
        res = convert_to_arabic('MMMMCLXXXIX')
        self.assertEqual(4189, res)

    def test_MMMMCXC(self):
        res = convert_to_arabic('MMMMCXC')
        self.assertEqual(4190, res)

    def test_MMMMCXCI(self):
        res = convert_to_arabic('MMMMCXCI')
        self.assertEqual(4191, res)

    def test_MMMMCXCII(self):
        res = convert_to_arabic('MMMMCXCII')
        self.assertEqual(4192, res)

    def test_MMMMCXCIII(self):
        res = convert_to_arabic('MMMMCXCIII')
        self.assertEqual(4193, res)

    def test_MMMMCXCIV(self):
        res = convert_to_arabic('MMMMCXCIV')
        self.assertEqual(4194, res)

    def test_MMMMCXCV(self):
        res = convert_to_arabic('MMMMCXCV')
        self.assertEqual(4195, res)

    def test_MMMMCXCVI(self):
        res = convert_to_arabic('MMMMCXCVI')
        self.assertEqual(4196, res)

    def test_MMMMCXCVII(self):
        res = convert_to_arabic('MMMMCXCVII')
        self.assertEqual(4197, res)

    def test_MMMMCXCVIII(self):
        res = convert_to_arabic('MMMMCXCVIII')
        self.assertEqual(4198, res)

    def test_MMMMCXCIX(self):
        res = convert_to_arabic('MMMMCXCIX')
        self.assertEqual(4199, res)

    def test_MMMMCC(self):
        res = convert_to_arabic('MMMMCC')
        self.assertEqual(4200, res)

    def test_MMMMCCI(self):
        res = convert_to_arabic('MMMMCCI')
        self.assertEqual(4201, res)

    def test_MMMMCCII(self):
        res = convert_to_arabic('MMMMCCII')
        self.assertEqual(4202, res)

    def test_MMMMCCIII(self):
        res = convert_to_arabic('MMMMCCIII')
        self.assertEqual(4203, res)

    def test_MMMMCCIV(self):
        res = convert_to_arabic('MMMMCCIV')
        self.assertEqual(4204, res)

    def test_MMMMCCV(self):
        res = convert_to_arabic('MMMMCCV')
        self.assertEqual(4205, res)

    def test_MMMMCCVI(self):
        res = convert_to_arabic('MMMMCCVI')
        self.assertEqual(4206, res)

    def test_MMMMCCVII(self):
        res = convert_to_arabic('MMMMCCVII')
        self.assertEqual(4207, res)

    def test_MMMMCCVIII(self):
        res = convert_to_arabic('MMMMCCVIII')
        self.assertEqual(4208, res)

    def test_MMMMCCIX(self):
        res = convert_to_arabic('MMMMCCIX')
        self.assertEqual(4209, res)

    def test_MMMMCCX(self):
        res = convert_to_arabic('MMMMCCX')
        self.assertEqual(4210, res)

    def test_MMMMCCXI(self):
        res = convert_to_arabic('MMMMCCXI')
        self.assertEqual(4211, res)

    def test_MMMMCCXII(self):
        res = convert_to_arabic('MMMMCCXII')
        self.assertEqual(4212, res)

    def test_MMMMCCXIII(self):
        res = convert_to_arabic('MMMMCCXIII')
        self.assertEqual(4213, res)

    def test_MMMMCCXIV(self):
        res = convert_to_arabic('MMMMCCXIV')
        self.assertEqual(4214, res)

    def test_MMMMCCXV(self):
        res = convert_to_arabic('MMMMCCXV')
        self.assertEqual(4215, res)

    def test_MMMMCCXVI(self):
        res = convert_to_arabic('MMMMCCXVI')
        self.assertEqual(4216, res)

    def test_MMMMCCXVII(self):
        res = convert_to_arabic('MMMMCCXVII')
        self.assertEqual(4217, res)

    def test_MMMMCCXVIII(self):
        res = convert_to_arabic('MMMMCCXVIII')
        self.assertEqual(4218, res)

    def test_MMMMCCXIX(self):
        res = convert_to_arabic('MMMMCCXIX')
        self.assertEqual(4219, res)

    def test_MMMMCCXX(self):
        res = convert_to_arabic('MMMMCCXX')
        self.assertEqual(4220, res)

    def test_MMMMCCXXI(self):
        res = convert_to_arabic('MMMMCCXXI')
        self.assertEqual(4221, res)

    def test_MMMMCCXXII(self):
        res = convert_to_arabic('MMMMCCXXII')
        self.assertEqual(4222, res)

    def test_MMMMCCXXIII(self):
        res = convert_to_arabic('MMMMCCXXIII')
        self.assertEqual(4223, res)

    def test_MMMMCCXXIV(self):
        res = convert_to_arabic('MMMMCCXXIV')
        self.assertEqual(4224, res)

    def test_MMMMCCXXV(self):
        res = convert_to_arabic('MMMMCCXXV')
        self.assertEqual(4225, res)

    def test_MMMMCCXXVI(self):
        res = convert_to_arabic('MMMMCCXXVI')
        self.assertEqual(4226, res)

    def test_MMMMCCXXVII(self):
        res = convert_to_arabic('MMMMCCXXVII')
        self.assertEqual(4227, res)

    def test_MMMMCCXXVIII(self):
        res = convert_to_arabic('MMMMCCXXVIII')
        self.assertEqual(4228, res)

    def test_MMMMCCXXIX(self):
        res = convert_to_arabic('MMMMCCXXIX')
        self.assertEqual(4229, res)

    def test_MMMMCCXXX(self):
        res = convert_to_arabic('MMMMCCXXX')
        self.assertEqual(4230, res)

    def test_MMMMCCXXXI(self):
        res = convert_to_arabic('MMMMCCXXXI')
        self.assertEqual(4231, res)

    def test_MMMMCCXXXII(self):
        res = convert_to_arabic('MMMMCCXXXII')
        self.assertEqual(4232, res)

    def test_MMMMCCXXXIII(self):
        res = convert_to_arabic('MMMMCCXXXIII')
        self.assertEqual(4233, res)

    def test_MMMMCCXXXIV(self):
        res = convert_to_arabic('MMMMCCXXXIV')
        self.assertEqual(4234, res)

    def test_MMMMCCXXXV(self):
        res = convert_to_arabic('MMMMCCXXXV')
        self.assertEqual(4235, res)

    def test_MMMMCCXXXVI(self):
        res = convert_to_arabic('MMMMCCXXXVI')
        self.assertEqual(4236, res)

    def test_MMMMCCXXXVII(self):
        res = convert_to_arabic('MMMMCCXXXVII')
        self.assertEqual(4237, res)

    def test_MMMMCCXXXVIII(self):
        res = convert_to_arabic('MMMMCCXXXVIII')
        self.assertEqual(4238, res)

    def test_MMMMCCXXXIX(self):
        res = convert_to_arabic('MMMMCCXXXIX')
        self.assertEqual(4239, res)

    def test_MMMMCCXL(self):
        res = convert_to_arabic('MMMMCCXL')
        self.assertEqual(4240, res)

    def test_MMMMCCXLI(self):
        res = convert_to_arabic('MMMMCCXLI')
        self.assertEqual(4241, res)

    def test_MMMMCCXLII(self):
        res = convert_to_arabic('MMMMCCXLII')
        self.assertEqual(4242, res)

    def test_MMMMCCXLIII(self):
        res = convert_to_arabic('MMMMCCXLIII')
        self.assertEqual(4243, res)

    def test_MMMMCCXLIV(self):
        res = convert_to_arabic('MMMMCCXLIV')
        self.assertEqual(4244, res)

    def test_MMMMCCXLV(self):
        res = convert_to_arabic('MMMMCCXLV')
        self.assertEqual(4245, res)

    def test_MMMMCCXLVI(self):
        res = convert_to_arabic('MMMMCCXLVI')
        self.assertEqual(4246, res)

    def test_MMMMCCXLVII(self):
        res = convert_to_arabic('MMMMCCXLVII')
        self.assertEqual(4247, res)

    def test_MMMMCCXLVIII(self):
        res = convert_to_arabic('MMMMCCXLVIII')
        self.assertEqual(4248, res)

    def test_MMMMCCXLIX(self):
        res = convert_to_arabic('MMMMCCXLIX')
        self.assertEqual(4249, res)

    def test_MMMMCCL(self):
        res = convert_to_arabic('MMMMCCL')
        self.assertEqual(4250, res)

    def test_MMMMCCLI(self):
        res = convert_to_arabic('MMMMCCLI')
        self.assertEqual(4251, res)

    def test_MMMMCCLII(self):
        res = convert_to_arabic('MMMMCCLII')
        self.assertEqual(4252, res)

    def test_MMMMCCLIII(self):
        res = convert_to_arabic('MMMMCCLIII')
        self.assertEqual(4253, res)

    def test_MMMMCCLIV(self):
        res = convert_to_arabic('MMMMCCLIV')
        self.assertEqual(4254, res)

    def test_MMMMCCLV(self):
        res = convert_to_arabic('MMMMCCLV')
        self.assertEqual(4255, res)

    def test_MMMMCCLVI(self):
        res = convert_to_arabic('MMMMCCLVI')
        self.assertEqual(4256, res)

    def test_MMMMCCLVII(self):
        res = convert_to_arabic('MMMMCCLVII')
        self.assertEqual(4257, res)

    def test_MMMMCCLVIII(self):
        res = convert_to_arabic('MMMMCCLVIII')
        self.assertEqual(4258, res)

    def test_MMMMCCLIX(self):
        res = convert_to_arabic('MMMMCCLIX')
        self.assertEqual(4259, res)

    def test_MMMMCCLX(self):
        res = convert_to_arabic('MMMMCCLX')
        self.assertEqual(4260, res)

    def test_MMMMCCLXI(self):
        res = convert_to_arabic('MMMMCCLXI')
        self.assertEqual(4261, res)

    def test_MMMMCCLXII(self):
        res = convert_to_arabic('MMMMCCLXII')
        self.assertEqual(4262, res)

    def test_MMMMCCLXIII(self):
        res = convert_to_arabic('MMMMCCLXIII')
        self.assertEqual(4263, res)

    def test_MMMMCCLXIV(self):
        res = convert_to_arabic('MMMMCCLXIV')
        self.assertEqual(4264, res)

    def test_MMMMCCLXV(self):
        res = convert_to_arabic('MMMMCCLXV')
        self.assertEqual(4265, res)

    def test_MMMMCCLXVI(self):
        res = convert_to_arabic('MMMMCCLXVI')
        self.assertEqual(4266, res)

    def test_MMMMCCLXVII(self):
        res = convert_to_arabic('MMMMCCLXVII')
        self.assertEqual(4267, res)

    def test_MMMMCCLXVIII(self):
        res = convert_to_arabic('MMMMCCLXVIII')
        self.assertEqual(4268, res)

    def test_MMMMCCLXIX(self):
        res = convert_to_arabic('MMMMCCLXIX')
        self.assertEqual(4269, res)

    def test_MMMMCCLXX(self):
        res = convert_to_arabic('MMMMCCLXX')
        self.assertEqual(4270, res)

    def test_MMMMCCLXXI(self):
        res = convert_to_arabic('MMMMCCLXXI')
        self.assertEqual(4271, res)

    def test_MMMMCCLXXII(self):
        res = convert_to_arabic('MMMMCCLXXII')
        self.assertEqual(4272, res)

    def test_MMMMCCLXXIII(self):
        res = convert_to_arabic('MMMMCCLXXIII')
        self.assertEqual(4273, res)

    def test_MMMMCCLXXIV(self):
        res = convert_to_arabic('MMMMCCLXXIV')
        self.assertEqual(4274, res)

    def test_MMMMCCLXXV(self):
        res = convert_to_arabic('MMMMCCLXXV')
        self.assertEqual(4275, res)

    def test_MMMMCCLXXVI(self):
        res = convert_to_arabic('MMMMCCLXXVI')
        self.assertEqual(4276, res)

    def test_MMMMCCLXXVII(self):
        res = convert_to_arabic('MMMMCCLXXVII')
        self.assertEqual(4277, res)

    def test_MMMMCCLXXVIII(self):
        res = convert_to_arabic('MMMMCCLXXVIII')
        self.assertEqual(4278, res)

    def test_MMMMCCLXXIX(self):
        res = convert_to_arabic('MMMMCCLXXIX')
        self.assertEqual(4279, res)

    def test_MMMMCCLXXX(self):
        res = convert_to_arabic('MMMMCCLXXX')
        self.assertEqual(4280, res)

    def test_MMMMCCLXXXI(self):
        res = convert_to_arabic('MMMMCCLXXXI')
        self.assertEqual(4281, res)

    def test_MMMMCCLXXXII(self):
        res = convert_to_arabic('MMMMCCLXXXII')
        self.assertEqual(4282, res)

    def test_MMMMCCLXXXIII(self):
        res = convert_to_arabic('MMMMCCLXXXIII')
        self.assertEqual(4283, res)

    def test_MMMMCCLXXXIV(self):
        res = convert_to_arabic('MMMMCCLXXXIV')
        self.assertEqual(4284, res)

    def test_MMMMCCLXXXV(self):
        res = convert_to_arabic('MMMMCCLXXXV')
        self.assertEqual(4285, res)

    def test_MMMMCCLXXXVI(self):
        res = convert_to_arabic('MMMMCCLXXXVI')
        self.assertEqual(4286, res)

    def test_MMMMCCLXXXVII(self):
        res = convert_to_arabic('MMMMCCLXXXVII')
        self.assertEqual(4287, res)

    def test_MMMMCCLXXXVIII(self):
        res = convert_to_arabic('MMMMCCLXXXVIII')
        self.assertEqual(4288, res)

    def test_MMMMCCLXXXIX(self):
        res = convert_to_arabic('MMMMCCLXXXIX')
        self.assertEqual(4289, res)

    def test_MMMMCCXC(self):
        res = convert_to_arabic('MMMMCCXC')
        self.assertEqual(4290, res)

    def test_MMMMCCXCI(self):
        res = convert_to_arabic('MMMMCCXCI')
        self.assertEqual(4291, res)

    def test_MMMMCCXCII(self):
        res = convert_to_arabic('MMMMCCXCII')
        self.assertEqual(4292, res)

    def test_MMMMCCXCIII(self):
        res = convert_to_arabic('MMMMCCXCIII')
        self.assertEqual(4293, res)

    def test_MMMMCCXCIV(self):
        res = convert_to_arabic('MMMMCCXCIV')
        self.assertEqual(4294, res)

    def test_MMMMCCXCV(self):
        res = convert_to_arabic('MMMMCCXCV')
        self.assertEqual(4295, res)

    def test_MMMMCCXCVI(self):
        res = convert_to_arabic('MMMMCCXCVI')
        self.assertEqual(4296, res)

    def test_MMMMCCXCVII(self):
        res = convert_to_arabic('MMMMCCXCVII')
        self.assertEqual(4297, res)

    def test_MMMMCCXCVIII(self):
        res = convert_to_arabic('MMMMCCXCVIII')
        self.assertEqual(4298, res)

    def test_MMMMCCXCIX(self):
        res = convert_to_arabic('MMMMCCXCIX')
        self.assertEqual(4299, res)

    def test_MMMMCCC(self):
        res = convert_to_arabic('MMMMCCC')
        self.assertEqual(4300, res)

    def test_MMMMCCCI(self):
        res = convert_to_arabic('MMMMCCCI')
        self.assertEqual(4301, res)

    def test_MMMMCCCII(self):
        res = convert_to_arabic('MMMMCCCII')
        self.assertEqual(4302, res)

    def test_MMMMCCCIII(self):
        res = convert_to_arabic('MMMMCCCIII')
        self.assertEqual(4303, res)

    def test_MMMMCCCIV(self):
        res = convert_to_arabic('MMMMCCCIV')
        self.assertEqual(4304, res)

    def test_MMMMCCCV(self):
        res = convert_to_arabic('MMMMCCCV')
        self.assertEqual(4305, res)

    def test_MMMMCCCVI(self):
        res = convert_to_arabic('MMMMCCCVI')
        self.assertEqual(4306, res)

    def test_MMMMCCCVII(self):
        res = convert_to_arabic('MMMMCCCVII')
        self.assertEqual(4307, res)

    def test_MMMMCCCVIII(self):
        res = convert_to_arabic('MMMMCCCVIII')
        self.assertEqual(4308, res)

    def test_MMMMCCCIX(self):
        res = convert_to_arabic('MMMMCCCIX')
        self.assertEqual(4309, res)

    def test_MMMMCCCX(self):
        res = convert_to_arabic('MMMMCCCX')
        self.assertEqual(4310, res)

    def test_MMMMCCCXI(self):
        res = convert_to_arabic('MMMMCCCXI')
        self.assertEqual(4311, res)

    def test_MMMMCCCXII(self):
        res = convert_to_arabic('MMMMCCCXII')
        self.assertEqual(4312, res)

    def test_MMMMCCCXIII(self):
        res = convert_to_arabic('MMMMCCCXIII')
        self.assertEqual(4313, res)

    def test_MMMMCCCXIV(self):
        res = convert_to_arabic('MMMMCCCXIV')
        self.assertEqual(4314, res)

    def test_MMMMCCCXV(self):
        res = convert_to_arabic('MMMMCCCXV')
        self.assertEqual(4315, res)

    def test_MMMMCCCXVI(self):
        res = convert_to_arabic('MMMMCCCXVI')
        self.assertEqual(4316, res)

    def test_MMMMCCCXVII(self):
        res = convert_to_arabic('MMMMCCCXVII')
        self.assertEqual(4317, res)

    def test_MMMMCCCXVIII(self):
        res = convert_to_arabic('MMMMCCCXVIII')
        self.assertEqual(4318, res)

    def test_MMMMCCCXIX(self):
        res = convert_to_arabic('MMMMCCCXIX')
        self.assertEqual(4319, res)

    def test_MMMMCCCXX(self):
        res = convert_to_arabic('MMMMCCCXX')
        self.assertEqual(4320, res)

    def test_MMMMCCCXXI(self):
        res = convert_to_arabic('MMMMCCCXXI')
        self.assertEqual(4321, res)

    def test_MMMMCCCXXII(self):
        res = convert_to_arabic('MMMMCCCXXII')
        self.assertEqual(4322, res)

    def test_MMMMCCCXXIII(self):
        res = convert_to_arabic('MMMMCCCXXIII')
        self.assertEqual(4323, res)

    def test_MMMMCCCXXIV(self):
        res = convert_to_arabic('MMMMCCCXXIV')
        self.assertEqual(4324, res)

    def test_MMMMCCCXXV(self):
        res = convert_to_arabic('MMMMCCCXXV')
        self.assertEqual(4325, res)

    def test_MMMMCCCXXVI(self):
        res = convert_to_arabic('MMMMCCCXXVI')
        self.assertEqual(4326, res)

    def test_MMMMCCCXXVII(self):
        res = convert_to_arabic('MMMMCCCXXVII')
        self.assertEqual(4327, res)

    def test_MMMMCCCXXVIII(self):
        res = convert_to_arabic('MMMMCCCXXVIII')
        self.assertEqual(4328, res)

    def test_MMMMCCCXXIX(self):
        res = convert_to_arabic('MMMMCCCXXIX')
        self.assertEqual(4329, res)

    def test_MMMMCCCXXX(self):
        res = convert_to_arabic('MMMMCCCXXX')
        self.assertEqual(4330, res)

    def test_MMMMCCCXXXI(self):
        res = convert_to_arabic('MMMMCCCXXXI')
        self.assertEqual(4331, res)

    def test_MMMMCCCXXXII(self):
        res = convert_to_arabic('MMMMCCCXXXII')
        self.assertEqual(4332, res)

    def test_MMMMCCCXXXIII(self):
        res = convert_to_arabic('MMMMCCCXXXIII')
        self.assertEqual(4333, res)

    def test_MMMMCCCXXXIV(self):
        res = convert_to_arabic('MMMMCCCXXXIV')
        self.assertEqual(4334, res)

    def test_MMMMCCCXXXV(self):
        res = convert_to_arabic('MMMMCCCXXXV')
        self.assertEqual(4335, res)

    def test_MMMMCCCXXXVI(self):
        res = convert_to_arabic('MMMMCCCXXXVI')
        self.assertEqual(4336, res)

    def test_MMMMCCCXXXVII(self):
        res = convert_to_arabic('MMMMCCCXXXVII')
        self.assertEqual(4337, res)

    def test_MMMMCCCXXXVIII(self):
        res = convert_to_arabic('MMMMCCCXXXVIII')
        self.assertEqual(4338, res)

    def test_MMMMCCCXXXIX(self):
        res = convert_to_arabic('MMMMCCCXXXIX')
        self.assertEqual(4339, res)

    def test_MMMMCCCXL(self):
        res = convert_to_arabic('MMMMCCCXL')
        self.assertEqual(4340, res)

    def test_MMMMCCCXLI(self):
        res = convert_to_arabic('MMMMCCCXLI')
        self.assertEqual(4341, res)

    def test_MMMMCCCXLII(self):
        res = convert_to_arabic('MMMMCCCXLII')
        self.assertEqual(4342, res)

    def test_MMMMCCCXLIII(self):
        res = convert_to_arabic('MMMMCCCXLIII')
        self.assertEqual(4343, res)

    def test_MMMMCCCXLIV(self):
        res = convert_to_arabic('MMMMCCCXLIV')
        self.assertEqual(4344, res)

    def test_MMMMCCCXLV(self):
        res = convert_to_arabic('MMMMCCCXLV')
        self.assertEqual(4345, res)

    def test_MMMMCCCXLVI(self):
        res = convert_to_arabic('MMMMCCCXLVI')
        self.assertEqual(4346, res)

    def test_MMMMCCCXLVII(self):
        res = convert_to_arabic('MMMMCCCXLVII')
        self.assertEqual(4347, res)

    def test_MMMMCCCXLVIII(self):
        res = convert_to_arabic('MMMMCCCXLVIII')
        self.assertEqual(4348, res)

    def test_MMMMCCCXLIX(self):
        res = convert_to_arabic('MMMMCCCXLIX')
        self.assertEqual(4349, res)

    def test_MMMMCCCL(self):
        res = convert_to_arabic('MMMMCCCL')
        self.assertEqual(4350, res)

    def test_MMMMCCCLI(self):
        res = convert_to_arabic('MMMMCCCLI')
        self.assertEqual(4351, res)

    def test_MMMMCCCLII(self):
        res = convert_to_arabic('MMMMCCCLII')
        self.assertEqual(4352, res)

    def test_MMMMCCCLIII(self):
        res = convert_to_arabic('MMMMCCCLIII')
        self.assertEqual(4353, res)

    def test_MMMMCCCLIV(self):
        res = convert_to_arabic('MMMMCCCLIV')
        self.assertEqual(4354, res)

    def test_MMMMCCCLV(self):
        res = convert_to_arabic('MMMMCCCLV')
        self.assertEqual(4355, res)

    def test_MMMMCCCLVI(self):
        res = convert_to_arabic('MMMMCCCLVI')
        self.assertEqual(4356, res)

    def test_MMMMCCCLVII(self):
        res = convert_to_arabic('MMMMCCCLVII')
        self.assertEqual(4357, res)

    def test_MMMMCCCLVIII(self):
        res = convert_to_arabic('MMMMCCCLVIII')
        self.assertEqual(4358, res)

    def test_MMMMCCCLIX(self):
        res = convert_to_arabic('MMMMCCCLIX')
        self.assertEqual(4359, res)

    def test_MMMMCCCLX(self):
        res = convert_to_arabic('MMMMCCCLX')
        self.assertEqual(4360, res)

    def test_MMMMCCCLXI(self):
        res = convert_to_arabic('MMMMCCCLXI')
        self.assertEqual(4361, res)

    def test_MMMMCCCLXII(self):
        res = convert_to_arabic('MMMMCCCLXII')
        self.assertEqual(4362, res)

    def test_MMMMCCCLXIII(self):
        res = convert_to_arabic('MMMMCCCLXIII')
        self.assertEqual(4363, res)

    def test_MMMMCCCLXIV(self):
        res = convert_to_arabic('MMMMCCCLXIV')
        self.assertEqual(4364, res)

    def test_MMMMCCCLXV(self):
        res = convert_to_arabic('MMMMCCCLXV')
        self.assertEqual(4365, res)

    def test_MMMMCCCLXVI(self):
        res = convert_to_arabic('MMMMCCCLXVI')
        self.assertEqual(4366, res)

    def test_MMMMCCCLXVII(self):
        res = convert_to_arabic('MMMMCCCLXVII')
        self.assertEqual(4367, res)

    def test_MMMMCCCLXVIII(self):
        res = convert_to_arabic('MMMMCCCLXVIII')
        self.assertEqual(4368, res)

    def test_MMMMCCCLXIX(self):
        res = convert_to_arabic('MMMMCCCLXIX')
        self.assertEqual(4369, res)

    def test_MMMMCCCLXX(self):
        res = convert_to_arabic('MMMMCCCLXX')
        self.assertEqual(4370, res)

    def test_MMMMCCCLXXI(self):
        res = convert_to_arabic('MMMMCCCLXXI')
        self.assertEqual(4371, res)

    def test_MMMMCCCLXXII(self):
        res = convert_to_arabic('MMMMCCCLXXII')
        self.assertEqual(4372, res)

    def test_MMMMCCCLXXIII(self):
        res = convert_to_arabic('MMMMCCCLXXIII')
        self.assertEqual(4373, res)

    def test_MMMMCCCLXXIV(self):
        res = convert_to_arabic('MMMMCCCLXXIV')
        self.assertEqual(4374, res)

    def test_MMMMCCCLXXV(self):
        res = convert_to_arabic('MMMMCCCLXXV')
        self.assertEqual(4375, res)

    def test_MMMMCCCLXXVI(self):
        res = convert_to_arabic('MMMMCCCLXXVI')
        self.assertEqual(4376, res)

    def test_MMMMCCCLXXVII(self):
        res = convert_to_arabic('MMMMCCCLXXVII')
        self.assertEqual(4377, res)

    def test_MMMMCCCLXXVIII(self):
        res = convert_to_arabic('MMMMCCCLXXVIII')
        self.assertEqual(4378, res)

    def test_MMMMCCCLXXIX(self):
        res = convert_to_arabic('MMMMCCCLXXIX')
        self.assertEqual(4379, res)

    def test_MMMMCCCLXXX(self):
        res = convert_to_arabic('MMMMCCCLXXX')
        self.assertEqual(4380, res)

    def test_MMMMCCCLXXXI(self):
        res = convert_to_arabic('MMMMCCCLXXXI')
        self.assertEqual(4381, res)

    def test_MMMMCCCLXXXII(self):
        res = convert_to_arabic('MMMMCCCLXXXII')
        self.assertEqual(4382, res)

    def test_MMMMCCCLXXXIII(self):
        res = convert_to_arabic('MMMMCCCLXXXIII')
        self.assertEqual(4383, res)

    def test_MMMMCCCLXXXIV(self):
        res = convert_to_arabic('MMMMCCCLXXXIV')
        self.assertEqual(4384, res)

    def test_MMMMCCCLXXXV(self):
        res = convert_to_arabic('MMMMCCCLXXXV')
        self.assertEqual(4385, res)

    def test_MMMMCCCLXXXVI(self):
        res = convert_to_arabic('MMMMCCCLXXXVI')
        self.assertEqual(4386, res)

    def test_MMMMCCCLXXXVII(self):
        res = convert_to_arabic('MMMMCCCLXXXVII')
        self.assertEqual(4387, res)

    def test_MMMMCCCLXXXVIII(self):
        res = convert_to_arabic('MMMMCCCLXXXVIII')
        self.assertEqual(4388, res)

    def test_MMMMCCCLXXXIX(self):
        res = convert_to_arabic('MMMMCCCLXXXIX')
        self.assertEqual(4389, res)

    def test_MMMMCCCXC(self):
        res = convert_to_arabic('MMMMCCCXC')
        self.assertEqual(4390, res)

    def test_MMMMCCCXCI(self):
        res = convert_to_arabic('MMMMCCCXCI')
        self.assertEqual(4391, res)

    def test_MMMMCCCXCII(self):
        res = convert_to_arabic('MMMMCCCXCII')
        self.assertEqual(4392, res)

    def test_MMMMCCCXCIII(self):
        res = convert_to_arabic('MMMMCCCXCIII')
        self.assertEqual(4393, res)

    def test_MMMMCCCXCIV(self):
        res = convert_to_arabic('MMMMCCCXCIV')
        self.assertEqual(4394, res)

    def test_MMMMCCCXCV(self):
        res = convert_to_arabic('MMMMCCCXCV')
        self.assertEqual(4395, res)

    def test_MMMMCCCXCVI(self):
        res = convert_to_arabic('MMMMCCCXCVI')
        self.assertEqual(4396, res)

    def test_MMMMCCCXCVII(self):
        res = convert_to_arabic('MMMMCCCXCVII')
        self.assertEqual(4397, res)

    def test_MMMMCCCXCVIII(self):
        res = convert_to_arabic('MMMMCCCXCVIII')
        self.assertEqual(4398, res)

    def test_MMMMCCCXCIX(self):
        res = convert_to_arabic('MMMMCCCXCIX')
        self.assertEqual(4399, res)

    def test_MMMMCD(self):
        res = convert_to_arabic('MMMMCD')
        self.assertEqual(4400, res)

    def test_MMMMCDI(self):
        res = convert_to_arabic('MMMMCDI')
        self.assertEqual(4401, res)

    def test_MMMMCDII(self):
        res = convert_to_arabic('MMMMCDII')
        self.assertEqual(4402, res)

    def test_MMMMCDIII(self):
        res = convert_to_arabic('MMMMCDIII')
        self.assertEqual(4403, res)

    def test_MMMMCDIV(self):
        res = convert_to_arabic('MMMMCDIV')
        self.assertEqual(4404, res)

    def test_MMMMCDV(self):
        res = convert_to_arabic('MMMMCDV')
        self.assertEqual(4405, res)

    def test_MMMMCDVI(self):
        res = convert_to_arabic('MMMMCDVI')
        self.assertEqual(4406, res)

    def test_MMMMCDVII(self):
        res = convert_to_arabic('MMMMCDVII')
        self.assertEqual(4407, res)

    def test_MMMMCDVIII(self):
        res = convert_to_arabic('MMMMCDVIII')
        self.assertEqual(4408, res)

    def test_MMMMCDIX(self):
        res = convert_to_arabic('MMMMCDIX')
        self.assertEqual(4409, res)

    def test_MMMMCDX(self):
        res = convert_to_arabic('MMMMCDX')
        self.assertEqual(4410, res)

    def test_MMMMCDXI(self):
        res = convert_to_arabic('MMMMCDXI')
        self.assertEqual(4411, res)

    def test_MMMMCDXII(self):
        res = convert_to_arabic('MMMMCDXII')
        self.assertEqual(4412, res)

    def test_MMMMCDXIII(self):
        res = convert_to_arabic('MMMMCDXIII')
        self.assertEqual(4413, res)

    def test_MMMMCDXIV(self):
        res = convert_to_arabic('MMMMCDXIV')
        self.assertEqual(4414, res)

    def test_MMMMCDXV(self):
        res = convert_to_arabic('MMMMCDXV')
        self.assertEqual(4415, res)

    def test_MMMMCDXVI(self):
        res = convert_to_arabic('MMMMCDXVI')
        self.assertEqual(4416, res)

    def test_MMMMCDXVII(self):
        res = convert_to_arabic('MMMMCDXVII')
        self.assertEqual(4417, res)

    def test_MMMMCDXVIII(self):
        res = convert_to_arabic('MMMMCDXVIII')
        self.assertEqual(4418, res)

    def test_MMMMCDXIX(self):
        res = convert_to_arabic('MMMMCDXIX')
        self.assertEqual(4419, res)

    def test_MMMMCDXX(self):
        res = convert_to_arabic('MMMMCDXX')
        self.assertEqual(4420, res)

    def test_MMMMCDXXI(self):
        res = convert_to_arabic('MMMMCDXXI')
        self.assertEqual(4421, res)

    def test_MMMMCDXXII(self):
        res = convert_to_arabic('MMMMCDXXII')
        self.assertEqual(4422, res)

    def test_MMMMCDXXIII(self):
        res = convert_to_arabic('MMMMCDXXIII')
        self.assertEqual(4423, res)

    def test_MMMMCDXXIV(self):
        res = convert_to_arabic('MMMMCDXXIV')
        self.assertEqual(4424, res)

    def test_MMMMCDXXV(self):
        res = convert_to_arabic('MMMMCDXXV')
        self.assertEqual(4425, res)

    def test_MMMMCDXXVI(self):
        res = convert_to_arabic('MMMMCDXXVI')
        self.assertEqual(4426, res)

    def test_MMMMCDXXVII(self):
        res = convert_to_arabic('MMMMCDXXVII')
        self.assertEqual(4427, res)

    def test_MMMMCDXXVIII(self):
        res = convert_to_arabic('MMMMCDXXVIII')
        self.assertEqual(4428, res)

    def test_MMMMCDXXIX(self):
        res = convert_to_arabic('MMMMCDXXIX')
        self.assertEqual(4429, res)

    def test_MMMMCDXXX(self):
        res = convert_to_arabic('MMMMCDXXX')
        self.assertEqual(4430, res)

    def test_MMMMCDXXXI(self):
        res = convert_to_arabic('MMMMCDXXXI')
        self.assertEqual(4431, res)

    def test_MMMMCDXXXII(self):
        res = convert_to_arabic('MMMMCDXXXII')
        self.assertEqual(4432, res)

    def test_MMMMCDXXXIII(self):
        res = convert_to_arabic('MMMMCDXXXIII')
        self.assertEqual(4433, res)

    def test_MMMMCDXXXIV(self):
        res = convert_to_arabic('MMMMCDXXXIV')
        self.assertEqual(4434, res)

    def test_MMMMCDXXXV(self):
        res = convert_to_arabic('MMMMCDXXXV')
        self.assertEqual(4435, res)

    def test_MMMMCDXXXVI(self):
        res = convert_to_arabic('MMMMCDXXXVI')
        self.assertEqual(4436, res)

    def test_MMMMCDXXXVII(self):
        res = convert_to_arabic('MMMMCDXXXVII')
        self.assertEqual(4437, res)

    def test_MMMMCDXXXVIII(self):
        res = convert_to_arabic('MMMMCDXXXVIII')
        self.assertEqual(4438, res)

    def test_MMMMCDXXXIX(self):
        res = convert_to_arabic('MMMMCDXXXIX')
        self.assertEqual(4439, res)

    def test_MMMMCDXL(self):
        res = convert_to_arabic('MMMMCDXL')
        self.assertEqual(4440, res)

    def test_MMMMCDXLI(self):
        res = convert_to_arabic('MMMMCDXLI')
        self.assertEqual(4441, res)

    def test_MMMMCDXLII(self):
        res = convert_to_arabic('MMMMCDXLII')
        self.assertEqual(4442, res)

    def test_MMMMCDXLIII(self):
        res = convert_to_arabic('MMMMCDXLIII')
        self.assertEqual(4443, res)

    def test_MMMMCDXLIV(self):
        res = convert_to_arabic('MMMMCDXLIV')
        self.assertEqual(4444, res)

    def test_MMMMCDXLV(self):
        res = convert_to_arabic('MMMMCDXLV')
        self.assertEqual(4445, res)

    def test_MMMMCDXLVI(self):
        res = convert_to_arabic('MMMMCDXLVI')
        self.assertEqual(4446, res)

    def test_MMMMCDXLVII(self):
        res = convert_to_arabic('MMMMCDXLVII')
        self.assertEqual(4447, res)

    def test_MMMMCDXLVIII(self):
        res = convert_to_arabic('MMMMCDXLVIII')
        self.assertEqual(4448, res)

    def test_MMMMCDXLIX(self):
        res = convert_to_arabic('MMMMCDXLIX')
        self.assertEqual(4449, res)

    def test_MMMMCDL(self):
        res = convert_to_arabic('MMMMCDL')
        self.assertEqual(4450, res)

    def test_MMMMCDLI(self):
        res = convert_to_arabic('MMMMCDLI')
        self.assertEqual(4451, res)

    def test_MMMMCDLII(self):
        res = convert_to_arabic('MMMMCDLII')
        self.assertEqual(4452, res)

    def test_MMMMCDLIII(self):
        res = convert_to_arabic('MMMMCDLIII')
        self.assertEqual(4453, res)

    def test_MMMMCDLIV(self):
        res = convert_to_arabic('MMMMCDLIV')
        self.assertEqual(4454, res)

    def test_MMMMCDLV(self):
        res = convert_to_arabic('MMMMCDLV')
        self.assertEqual(4455, res)

    def test_MMMMCDLVI(self):
        res = convert_to_arabic('MMMMCDLVI')
        self.assertEqual(4456, res)

    def test_MMMMCDLVII(self):
        res = convert_to_arabic('MMMMCDLVII')
        self.assertEqual(4457, res)

    def test_MMMMCDLVIII(self):
        res = convert_to_arabic('MMMMCDLVIII')
        self.assertEqual(4458, res)

    def test_MMMMCDLIX(self):
        res = convert_to_arabic('MMMMCDLIX')
        self.assertEqual(4459, res)

    def test_MMMMCDLX(self):
        res = convert_to_arabic('MMMMCDLX')
        self.assertEqual(4460, res)

    def test_MMMMCDLXI(self):
        res = convert_to_arabic('MMMMCDLXI')
        self.assertEqual(4461, res)

    def test_MMMMCDLXII(self):
        res = convert_to_arabic('MMMMCDLXII')
        self.assertEqual(4462, res)

    def test_MMMMCDLXIII(self):
        res = convert_to_arabic('MMMMCDLXIII')
        self.assertEqual(4463, res)

    def test_MMMMCDLXIV(self):
        res = convert_to_arabic('MMMMCDLXIV')
        self.assertEqual(4464, res)

    def test_MMMMCDLXV(self):
        res = convert_to_arabic('MMMMCDLXV')
        self.assertEqual(4465, res)

    def test_MMMMCDLXVI(self):
        res = convert_to_arabic('MMMMCDLXVI')
        self.assertEqual(4466, res)

    def test_MMMMCDLXVII(self):
        res = convert_to_arabic('MMMMCDLXVII')
        self.assertEqual(4467, res)

    def test_MMMMCDLXVIII(self):
        res = convert_to_arabic('MMMMCDLXVIII')
        self.assertEqual(4468, res)

    def test_MMMMCDLXIX(self):
        res = convert_to_arabic('MMMMCDLXIX')
        self.assertEqual(4469, res)

    def test_MMMMCDLXX(self):
        res = convert_to_arabic('MMMMCDLXX')
        self.assertEqual(4470, res)

    def test_MMMMCDLXXI(self):
        res = convert_to_arabic('MMMMCDLXXI')
        self.assertEqual(4471, res)

    def test_MMMMCDLXXII(self):
        res = convert_to_arabic('MMMMCDLXXII')
        self.assertEqual(4472, res)

    def test_MMMMCDLXXIII(self):
        res = convert_to_arabic('MMMMCDLXXIII')
        self.assertEqual(4473, res)

    def test_MMMMCDLXXIV(self):
        res = convert_to_arabic('MMMMCDLXXIV')
        self.assertEqual(4474, res)

    def test_MMMMCDLXXV(self):
        res = convert_to_arabic('MMMMCDLXXV')
        self.assertEqual(4475, res)

    def test_MMMMCDLXXVI(self):
        res = convert_to_arabic('MMMMCDLXXVI')
        self.assertEqual(4476, res)

    def test_MMMMCDLXXVII(self):
        res = convert_to_arabic('MMMMCDLXXVII')
        self.assertEqual(4477, res)

    def test_MMMMCDLXXVIII(self):
        res = convert_to_arabic('MMMMCDLXXVIII')
        self.assertEqual(4478, res)

    def test_MMMMCDLXXIX(self):
        res = convert_to_arabic('MMMMCDLXXIX')
        self.assertEqual(4479, res)

    def test_MMMMCDLXXX(self):
        res = convert_to_arabic('MMMMCDLXXX')
        self.assertEqual(4480, res)

    def test_MMMMCDLXXXI(self):
        res = convert_to_arabic('MMMMCDLXXXI')
        self.assertEqual(4481, res)

    def test_MMMMCDLXXXII(self):
        res = convert_to_arabic('MMMMCDLXXXII')
        self.assertEqual(4482, res)

    def test_MMMMCDLXXXIII(self):
        res = convert_to_arabic('MMMMCDLXXXIII')
        self.assertEqual(4483, res)

    def test_MMMMCDLXXXIV(self):
        res = convert_to_arabic('MMMMCDLXXXIV')
        self.assertEqual(4484, res)

    def test_MMMMCDLXXXV(self):
        res = convert_to_arabic('MMMMCDLXXXV')
        self.assertEqual(4485, res)

    def test_MMMMCDLXXXVI(self):
        res = convert_to_arabic('MMMMCDLXXXVI')
        self.assertEqual(4486, res)

    def test_MMMMCDLXXXVII(self):
        res = convert_to_arabic('MMMMCDLXXXVII')
        self.assertEqual(4487, res)

    def test_MMMMCDLXXXVIII(self):
        res = convert_to_arabic('MMMMCDLXXXVIII')
        self.assertEqual(4488, res)

    def test_MMMMCDLXXXIX(self):
        res = convert_to_arabic('MMMMCDLXXXIX')
        self.assertEqual(4489, res)

    def test_MMMMCDXC(self):
        res = convert_to_arabic('MMMMCDXC')
        self.assertEqual(4490, res)

    def test_MMMMCDXCI(self):
        res = convert_to_arabic('MMMMCDXCI')
        self.assertEqual(4491, res)

    def test_MMMMCDXCII(self):
        res = convert_to_arabic('MMMMCDXCII')
        self.assertEqual(4492, res)

    def test_MMMMCDXCIII(self):
        res = convert_to_arabic('MMMMCDXCIII')
        self.assertEqual(4493, res)

    def test_MMMMCDXCIV(self):
        res = convert_to_arabic('MMMMCDXCIV')
        self.assertEqual(4494, res)

    def test_MMMMCDXCV(self):
        res = convert_to_arabic('MMMMCDXCV')
        self.assertEqual(4495, res)

    def test_MMMMCDXCVI(self):
        res = convert_to_arabic('MMMMCDXCVI')
        self.assertEqual(4496, res)

    def test_MMMMCDXCVII(self):
        res = convert_to_arabic('MMMMCDXCVII')
        self.assertEqual(4497, res)

    def test_MMMMCDXCVIII(self):
        res = convert_to_arabic('MMMMCDXCVIII')
        self.assertEqual(4498, res)

    def test_MMMMCDXCIX(self):
        res = convert_to_arabic('MMMMCDXCIX')
        self.assertEqual(4499, res)

    def test_MMMMD(self):
        res = convert_to_arabic('MMMMD')
        self.assertEqual(4500, res)

    def test_MMMMDI(self):
        res = convert_to_arabic('MMMMDI')
        self.assertEqual(4501, res)

    def test_MMMMDII(self):
        res = convert_to_arabic('MMMMDII')
        self.assertEqual(4502, res)

    def test_MMMMDIII(self):
        res = convert_to_arabic('MMMMDIII')
        self.assertEqual(4503, res)

    def test_MMMMDIV(self):
        res = convert_to_arabic('MMMMDIV')
        self.assertEqual(4504, res)

    def test_MMMMDV(self):
        res = convert_to_arabic('MMMMDV')
        self.assertEqual(4505, res)

    def test_MMMMDVI(self):
        res = convert_to_arabic('MMMMDVI')
        self.assertEqual(4506, res)

    def test_MMMMDVII(self):
        res = convert_to_arabic('MMMMDVII')
        self.assertEqual(4507, res)

    def test_MMMMDVIII(self):
        res = convert_to_arabic('MMMMDVIII')
        self.assertEqual(4508, res)

    def test_MMMMDIX(self):
        res = convert_to_arabic('MMMMDIX')
        self.assertEqual(4509, res)

    def test_MMMMDX(self):
        res = convert_to_arabic('MMMMDX')
        self.assertEqual(4510, res)

    def test_MMMMDXI(self):
        res = convert_to_arabic('MMMMDXI')
        self.assertEqual(4511, res)

    def test_MMMMDXII(self):
        res = convert_to_arabic('MMMMDXII')
        self.assertEqual(4512, res)

    def test_MMMMDXIII(self):
        res = convert_to_arabic('MMMMDXIII')
        self.assertEqual(4513, res)

    def test_MMMMDXIV(self):
        res = convert_to_arabic('MMMMDXIV')
        self.assertEqual(4514, res)

    def test_MMMMDXV(self):
        res = convert_to_arabic('MMMMDXV')
        self.assertEqual(4515, res)

    def test_MMMMDXVI(self):
        res = convert_to_arabic('MMMMDXVI')
        self.assertEqual(4516, res)

    def test_MMMMDXVII(self):
        res = convert_to_arabic('MMMMDXVII')
        self.assertEqual(4517, res)

    def test_MMMMDXVIII(self):
        res = convert_to_arabic('MMMMDXVIII')
        self.assertEqual(4518, res)

    def test_MMMMDXIX(self):
        res = convert_to_arabic('MMMMDXIX')
        self.assertEqual(4519, res)

    def test_MMMMDXX(self):
        res = convert_to_arabic('MMMMDXX')
        self.assertEqual(4520, res)

    def test_MMMMDXXI(self):
        res = convert_to_arabic('MMMMDXXI')
        self.assertEqual(4521, res)

    def test_MMMMDXXII(self):
        res = convert_to_arabic('MMMMDXXII')
        self.assertEqual(4522, res)

    def test_MMMMDXXIII(self):
        res = convert_to_arabic('MMMMDXXIII')
        self.assertEqual(4523, res)

    def test_MMMMDXXIV(self):
        res = convert_to_arabic('MMMMDXXIV')
        self.assertEqual(4524, res)

    def test_MMMMDXXV(self):
        res = convert_to_arabic('MMMMDXXV')
        self.assertEqual(4525, res)

    def test_MMMMDXXVI(self):
        res = convert_to_arabic('MMMMDXXVI')
        self.assertEqual(4526, res)

    def test_MMMMDXXVII(self):
        res = convert_to_arabic('MMMMDXXVII')
        self.assertEqual(4527, res)

    def test_MMMMDXXVIII(self):
        res = convert_to_arabic('MMMMDXXVIII')
        self.assertEqual(4528, res)

    def test_MMMMDXXIX(self):
        res = convert_to_arabic('MMMMDXXIX')
        self.assertEqual(4529, res)

    def test_MMMMDXXX(self):
        res = convert_to_arabic('MMMMDXXX')
        self.assertEqual(4530, res)

    def test_MMMMDXXXI(self):
        res = convert_to_arabic('MMMMDXXXI')
        self.assertEqual(4531, res)

    def test_MMMMDXXXII(self):
        res = convert_to_arabic('MMMMDXXXII')
        self.assertEqual(4532, res)

    def test_MMMMDXXXIII(self):
        res = convert_to_arabic('MMMMDXXXIII')
        self.assertEqual(4533, res)

    def test_MMMMDXXXIV(self):
        res = convert_to_arabic('MMMMDXXXIV')
        self.assertEqual(4534, res)

    def test_MMMMDXXXV(self):
        res = convert_to_arabic('MMMMDXXXV')
        self.assertEqual(4535, res)

    def test_MMMMDXXXVI(self):
        res = convert_to_arabic('MMMMDXXXVI')
        self.assertEqual(4536, res)

    def test_MMMMDXXXVII(self):
        res = convert_to_arabic('MMMMDXXXVII')
        self.assertEqual(4537, res)

    def test_MMMMDXXXVIII(self):
        res = convert_to_arabic('MMMMDXXXVIII')
        self.assertEqual(4538, res)

    def test_MMMMDXXXIX(self):
        res = convert_to_arabic('MMMMDXXXIX')
        self.assertEqual(4539, res)

    def test_MMMMDXL(self):
        res = convert_to_arabic('MMMMDXL')
        self.assertEqual(4540, res)

    def test_MMMMDXLI(self):
        res = convert_to_arabic('MMMMDXLI')
        self.assertEqual(4541, res)

    def test_MMMMDXLII(self):
        res = convert_to_arabic('MMMMDXLII')
        self.assertEqual(4542, res)

    def test_MMMMDXLIII(self):
        res = convert_to_arabic('MMMMDXLIII')
        self.assertEqual(4543, res)

    def test_MMMMDXLIV(self):
        res = convert_to_arabic('MMMMDXLIV')
        self.assertEqual(4544, res)

    def test_MMMMDXLV(self):
        res = convert_to_arabic('MMMMDXLV')
        self.assertEqual(4545, res)

    def test_MMMMDXLVI(self):
        res = convert_to_arabic('MMMMDXLVI')
        self.assertEqual(4546, res)

    def test_MMMMDXLVII(self):
        res = convert_to_arabic('MMMMDXLVII')
        self.assertEqual(4547, res)

    def test_MMMMDXLVIII(self):
        res = convert_to_arabic('MMMMDXLVIII')
        self.assertEqual(4548, res)

    def test_MMMMDXLIX(self):
        res = convert_to_arabic('MMMMDXLIX')
        self.assertEqual(4549, res)

    def test_MMMMDL(self):
        res = convert_to_arabic('MMMMDL')
        self.assertEqual(4550, res)

    def test_MMMMDLI(self):
        res = convert_to_arabic('MMMMDLI')
        self.assertEqual(4551, res)

    def test_MMMMDLII(self):
        res = convert_to_arabic('MMMMDLII')
        self.assertEqual(4552, res)

    def test_MMMMDLIII(self):
        res = convert_to_arabic('MMMMDLIII')
        self.assertEqual(4553, res)

    def test_MMMMDLIV(self):
        res = convert_to_arabic('MMMMDLIV')
        self.assertEqual(4554, res)

    def test_MMMMDLV(self):
        res = convert_to_arabic('MMMMDLV')
        self.assertEqual(4555, res)

    def test_MMMMDLVI(self):
        res = convert_to_arabic('MMMMDLVI')
        self.assertEqual(4556, res)

    def test_MMMMDLVII(self):
        res = convert_to_arabic('MMMMDLVII')
        self.assertEqual(4557, res)

    def test_MMMMDLVIII(self):
        res = convert_to_arabic('MMMMDLVIII')
        self.assertEqual(4558, res)

    def test_MMMMDLIX(self):
        res = convert_to_arabic('MMMMDLIX')
        self.assertEqual(4559, res)

    def test_MMMMDLX(self):
        res = convert_to_arabic('MMMMDLX')
        self.assertEqual(4560, res)

    def test_MMMMDLXI(self):
        res = convert_to_arabic('MMMMDLXI')
        self.assertEqual(4561, res)

    def test_MMMMDLXII(self):
        res = convert_to_arabic('MMMMDLXII')
        self.assertEqual(4562, res)

    def test_MMMMDLXIII(self):
        res = convert_to_arabic('MMMMDLXIII')
        self.assertEqual(4563, res)

    def test_MMMMDLXIV(self):
        res = convert_to_arabic('MMMMDLXIV')
        self.assertEqual(4564, res)

    def test_MMMMDLXV(self):
        res = convert_to_arabic('MMMMDLXV')
        self.assertEqual(4565, res)

    def test_MMMMDLXVI(self):
        res = convert_to_arabic('MMMMDLXVI')
        self.assertEqual(4566, res)

    def test_MMMMDLXVII(self):
        res = convert_to_arabic('MMMMDLXVII')
        self.assertEqual(4567, res)

    def test_MMMMDLXVIII(self):
        res = convert_to_arabic('MMMMDLXVIII')
        self.assertEqual(4568, res)

    def test_MMMMDLXIX(self):
        res = convert_to_arabic('MMMMDLXIX')
        self.assertEqual(4569, res)

    def test_MMMMDLXX(self):
        res = convert_to_arabic('MMMMDLXX')
        self.assertEqual(4570, res)

    def test_MMMMDLXXI(self):
        res = convert_to_arabic('MMMMDLXXI')
        self.assertEqual(4571, res)

    def test_MMMMDLXXII(self):
        res = convert_to_arabic('MMMMDLXXII')
        self.assertEqual(4572, res)

    def test_MMMMDLXXIII(self):
        res = convert_to_arabic('MMMMDLXXIII')
        self.assertEqual(4573, res)

    def test_MMMMDLXXIV(self):
        res = convert_to_arabic('MMMMDLXXIV')
        self.assertEqual(4574, res)

    def test_MMMMDLXXV(self):
        res = convert_to_arabic('MMMMDLXXV')
        self.assertEqual(4575, res)

    def test_MMMMDLXXVI(self):
        res = convert_to_arabic('MMMMDLXXVI')
        self.assertEqual(4576, res)

    def test_MMMMDLXXVII(self):
        res = convert_to_arabic('MMMMDLXXVII')
        self.assertEqual(4577, res)

    def test_MMMMDLXXVIII(self):
        res = convert_to_arabic('MMMMDLXXVIII')
        self.assertEqual(4578, res)

    def test_MMMMDLXXIX(self):
        res = convert_to_arabic('MMMMDLXXIX')
        self.assertEqual(4579, res)

    def test_MMMMDLXXX(self):
        res = convert_to_arabic('MMMMDLXXX')
        self.assertEqual(4580, res)

    def test_MMMMDLXXXI(self):
        res = convert_to_arabic('MMMMDLXXXI')
        self.assertEqual(4581, res)

    def test_MMMMDLXXXII(self):
        res = convert_to_arabic('MMMMDLXXXII')
        self.assertEqual(4582, res)

    def test_MMMMDLXXXIII(self):
        res = convert_to_arabic('MMMMDLXXXIII')
        self.assertEqual(4583, res)

    def test_MMMMDLXXXIV(self):
        res = convert_to_arabic('MMMMDLXXXIV')
        self.assertEqual(4584, res)

    def test_MMMMDLXXXV(self):
        res = convert_to_arabic('MMMMDLXXXV')
        self.assertEqual(4585, res)

    def test_MMMMDLXXXVI(self):
        res = convert_to_arabic('MMMMDLXXXVI')
        self.assertEqual(4586, res)

    def test_MMMMDLXXXVII(self):
        res = convert_to_arabic('MMMMDLXXXVII')
        self.assertEqual(4587, res)

    def test_MMMMDLXXXVIII(self):
        res = convert_to_arabic('MMMMDLXXXVIII')
        self.assertEqual(4588, res)

    def test_MMMMDLXXXIX(self):
        res = convert_to_arabic('MMMMDLXXXIX')
        self.assertEqual(4589, res)

    def test_MMMMDXC(self):
        res = convert_to_arabic('MMMMDXC')
        self.assertEqual(4590, res)

    def test_MMMMDXCI(self):
        res = convert_to_arabic('MMMMDXCI')
        self.assertEqual(4591, res)

    def test_MMMMDXCII(self):
        res = convert_to_arabic('MMMMDXCII')
        self.assertEqual(4592, res)

    def test_MMMMDXCIII(self):
        res = convert_to_arabic('MMMMDXCIII')
        self.assertEqual(4593, res)

    def test_MMMMDXCIV(self):
        res = convert_to_arabic('MMMMDXCIV')
        self.assertEqual(4594, res)

    def test_MMMMDXCV(self):
        res = convert_to_arabic('MMMMDXCV')
        self.assertEqual(4595, res)

    def test_MMMMDXCVI(self):
        res = convert_to_arabic('MMMMDXCVI')
        self.assertEqual(4596, res)

    def test_MMMMDXCVII(self):
        res = convert_to_arabic('MMMMDXCVII')
        self.assertEqual(4597, res)

    def test_MMMMDXCVIII(self):
        res = convert_to_arabic('MMMMDXCVIII')
        self.assertEqual(4598, res)

    def test_MMMMDXCIX(self):
        res = convert_to_arabic('MMMMDXCIX')
        self.assertEqual(4599, res)

    def test_MMMMDC(self):
        res = convert_to_arabic('MMMMDC')
        self.assertEqual(4600, res)

    def test_MMMMDCI(self):
        res = convert_to_arabic('MMMMDCI')
        self.assertEqual(4601, res)

    def test_MMMMDCII(self):
        res = convert_to_arabic('MMMMDCII')
        self.assertEqual(4602, res)

    def test_MMMMDCIII(self):
        res = convert_to_arabic('MMMMDCIII')
        self.assertEqual(4603, res)

    def test_MMMMDCIV(self):
        res = convert_to_arabic('MMMMDCIV')
        self.assertEqual(4604, res)

    def test_MMMMDCV(self):
        res = convert_to_arabic('MMMMDCV')
        self.assertEqual(4605, res)

    def test_MMMMDCVI(self):
        res = convert_to_arabic('MMMMDCVI')
        self.assertEqual(4606, res)

    def test_MMMMDCVII(self):
        res = convert_to_arabic('MMMMDCVII')
        self.assertEqual(4607, res)

    def test_MMMMDCVIII(self):
        res = convert_to_arabic('MMMMDCVIII')
        self.assertEqual(4608, res)

    def test_MMMMDCIX(self):
        res = convert_to_arabic('MMMMDCIX')
        self.assertEqual(4609, res)

    def test_MMMMDCX(self):
        res = convert_to_arabic('MMMMDCX')
        self.assertEqual(4610, res)

    def test_MMMMDCXI(self):
        res = convert_to_arabic('MMMMDCXI')
        self.assertEqual(4611, res)

    def test_MMMMDCXII(self):
        res = convert_to_arabic('MMMMDCXII')
        self.assertEqual(4612, res)

    def test_MMMMDCXIII(self):
        res = convert_to_arabic('MMMMDCXIII')
        self.assertEqual(4613, res)

    def test_MMMMDCXIV(self):
        res = convert_to_arabic('MMMMDCXIV')
        self.assertEqual(4614, res)

    def test_MMMMDCXV(self):
        res = convert_to_arabic('MMMMDCXV')
        self.assertEqual(4615, res)

    def test_MMMMDCXVI(self):
        res = convert_to_arabic('MMMMDCXVI')
        self.assertEqual(4616, res)

    def test_MMMMDCXVII(self):
        res = convert_to_arabic('MMMMDCXVII')
        self.assertEqual(4617, res)

    def test_MMMMDCXVIII(self):
        res = convert_to_arabic('MMMMDCXVIII')
        self.assertEqual(4618, res)

    def test_MMMMDCXIX(self):
        res = convert_to_arabic('MMMMDCXIX')
        self.assertEqual(4619, res)

    def test_MMMMDCXX(self):
        res = convert_to_arabic('MMMMDCXX')
        self.assertEqual(4620, res)

    def test_MMMMDCXXI(self):
        res = convert_to_arabic('MMMMDCXXI')
        self.assertEqual(4621, res)

    def test_MMMMDCXXII(self):
        res = convert_to_arabic('MMMMDCXXII')
        self.assertEqual(4622, res)

    def test_MMMMDCXXIII(self):
        res = convert_to_arabic('MMMMDCXXIII')
        self.assertEqual(4623, res)

    def test_MMMMDCXXIV(self):
        res = convert_to_arabic('MMMMDCXXIV')
        self.assertEqual(4624, res)

    def test_MMMMDCXXV(self):
        res = convert_to_arabic('MMMMDCXXV')
        self.assertEqual(4625, res)

    def test_MMMMDCXXVI(self):
        res = convert_to_arabic('MMMMDCXXVI')
        self.assertEqual(4626, res)

    def test_MMMMDCXXVII(self):
        res = convert_to_arabic('MMMMDCXXVII')
        self.assertEqual(4627, res)

    def test_MMMMDCXXVIII(self):
        res = convert_to_arabic('MMMMDCXXVIII')
        self.assertEqual(4628, res)

    def test_MMMMDCXXIX(self):
        res = convert_to_arabic('MMMMDCXXIX')
        self.assertEqual(4629, res)

    def test_MMMMDCXXX(self):
        res = convert_to_arabic('MMMMDCXXX')
        self.assertEqual(4630, res)

    def test_MMMMDCXXXI(self):
        res = convert_to_arabic('MMMMDCXXXI')
        self.assertEqual(4631, res)

    def test_MMMMDCXXXII(self):
        res = convert_to_arabic('MMMMDCXXXII')
        self.assertEqual(4632, res)

    def test_MMMMDCXXXIII(self):
        res = convert_to_arabic('MMMMDCXXXIII')
        self.assertEqual(4633, res)

    def test_MMMMDCXXXIV(self):
        res = convert_to_arabic('MMMMDCXXXIV')
        self.assertEqual(4634, res)

    def test_MMMMDCXXXV(self):
        res = convert_to_arabic('MMMMDCXXXV')
        self.assertEqual(4635, res)

    def test_MMMMDCXXXVI(self):
        res = convert_to_arabic('MMMMDCXXXVI')
        self.assertEqual(4636, res)

    def test_MMMMDCXXXVII(self):
        res = convert_to_arabic('MMMMDCXXXVII')
        self.assertEqual(4637, res)

    def test_MMMMDCXXXVIII(self):
        res = convert_to_arabic('MMMMDCXXXVIII')
        self.assertEqual(4638, res)

    def test_MMMMDCXXXIX(self):
        res = convert_to_arabic('MMMMDCXXXIX')
        self.assertEqual(4639, res)

    def test_MMMMDCXL(self):
        res = convert_to_arabic('MMMMDCXL')
        self.assertEqual(4640, res)

    def test_MMMMDCXLI(self):
        res = convert_to_arabic('MMMMDCXLI')
        self.assertEqual(4641, res)

    def test_MMMMDCXLII(self):
        res = convert_to_arabic('MMMMDCXLII')
        self.assertEqual(4642, res)

    def test_MMMMDCXLIII(self):
        res = convert_to_arabic('MMMMDCXLIII')
        self.assertEqual(4643, res)

    def test_MMMMDCXLIV(self):
        res = convert_to_arabic('MMMMDCXLIV')
        self.assertEqual(4644, res)

    def test_MMMMDCXLV(self):
        res = convert_to_arabic('MMMMDCXLV')
        self.assertEqual(4645, res)

    def test_MMMMDCXLVI(self):
        res = convert_to_arabic('MMMMDCXLVI')
        self.assertEqual(4646, res)

    def test_MMMMDCXLVII(self):
        res = convert_to_arabic('MMMMDCXLVII')
        self.assertEqual(4647, res)

    def test_MMMMDCXLVIII(self):
        res = convert_to_arabic('MMMMDCXLVIII')
        self.assertEqual(4648, res)

    def test_MMMMDCXLIX(self):
        res = convert_to_arabic('MMMMDCXLIX')
        self.assertEqual(4649, res)

    def test_MMMMDCL(self):
        res = convert_to_arabic('MMMMDCL')
        self.assertEqual(4650, res)

    def test_MMMMDCLI(self):
        res = convert_to_arabic('MMMMDCLI')
        self.assertEqual(4651, res)

    def test_MMMMDCLII(self):
        res = convert_to_arabic('MMMMDCLII')
        self.assertEqual(4652, res)

    def test_MMMMDCLIII(self):
        res = convert_to_arabic('MMMMDCLIII')
        self.assertEqual(4653, res)

    def test_MMMMDCLIV(self):
        res = convert_to_arabic('MMMMDCLIV')
        self.assertEqual(4654, res)

    def test_MMMMDCLV(self):
        res = convert_to_arabic('MMMMDCLV')
        self.assertEqual(4655, res)

    def test_MMMMDCLVI(self):
        res = convert_to_arabic('MMMMDCLVI')
        self.assertEqual(4656, res)

    def test_MMMMDCLVII(self):
        res = convert_to_arabic('MMMMDCLVII')
        self.assertEqual(4657, res)

    def test_MMMMDCLVIII(self):
        res = convert_to_arabic('MMMMDCLVIII')
        self.assertEqual(4658, res)

    def test_MMMMDCLIX(self):
        res = convert_to_arabic('MMMMDCLIX')
        self.assertEqual(4659, res)

    def test_MMMMDCLX(self):
        res = convert_to_arabic('MMMMDCLX')
        self.assertEqual(4660, res)

    def test_MMMMDCLXI(self):
        res = convert_to_arabic('MMMMDCLXI')
        self.assertEqual(4661, res)

    def test_MMMMDCLXII(self):
        res = convert_to_arabic('MMMMDCLXII')
        self.assertEqual(4662, res)

    def test_MMMMDCLXIII(self):
        res = convert_to_arabic('MMMMDCLXIII')
        self.assertEqual(4663, res)

    def test_MMMMDCLXIV(self):
        res = convert_to_arabic('MMMMDCLXIV')
        self.assertEqual(4664, res)

    def test_MMMMDCLXV(self):
        res = convert_to_arabic('MMMMDCLXV')
        self.assertEqual(4665, res)

    def test_MMMMDCLXVI(self):
        res = convert_to_arabic('MMMMDCLXVI')
        self.assertEqual(4666, res)

    def test_MMMMDCLXVII(self):
        res = convert_to_arabic('MMMMDCLXVII')
        self.assertEqual(4667, res)

    def test_MMMMDCLXVIII(self):
        res = convert_to_arabic('MMMMDCLXVIII')
        self.assertEqual(4668, res)

    def test_MMMMDCLXIX(self):
        res = convert_to_arabic('MMMMDCLXIX')
        self.assertEqual(4669, res)

    def test_MMMMDCLXX(self):
        res = convert_to_arabic('MMMMDCLXX')
        self.assertEqual(4670, res)

    def test_MMMMDCLXXI(self):
        res = convert_to_arabic('MMMMDCLXXI')
        self.assertEqual(4671, res)

    def test_MMMMDCLXXII(self):
        res = convert_to_arabic('MMMMDCLXXII')
        self.assertEqual(4672, res)

    def test_MMMMDCLXXIII(self):
        res = convert_to_arabic('MMMMDCLXXIII')
        self.assertEqual(4673, res)

    def test_MMMMDCLXXIV(self):
        res = convert_to_arabic('MMMMDCLXXIV')
        self.assertEqual(4674, res)

    def test_MMMMDCLXXV(self):
        res = convert_to_arabic('MMMMDCLXXV')
        self.assertEqual(4675, res)

    def test_MMMMDCLXXVI(self):
        res = convert_to_arabic('MMMMDCLXXVI')
        self.assertEqual(4676, res)

    def test_MMMMDCLXXVII(self):
        res = convert_to_arabic('MMMMDCLXXVII')
        self.assertEqual(4677, res)

    def test_MMMMDCLXXVIII(self):
        res = convert_to_arabic('MMMMDCLXXVIII')
        self.assertEqual(4678, res)

    def test_MMMMDCLXXIX(self):
        res = convert_to_arabic('MMMMDCLXXIX')
        self.assertEqual(4679, res)

    def test_MMMMDCLXXX(self):
        res = convert_to_arabic('MMMMDCLXXX')
        self.assertEqual(4680, res)

    def test_MMMMDCLXXXI(self):
        res = convert_to_arabic('MMMMDCLXXXI')
        self.assertEqual(4681, res)

    def test_MMMMDCLXXXII(self):
        res = convert_to_arabic('MMMMDCLXXXII')
        self.assertEqual(4682, res)

    def test_MMMMDCLXXXIII(self):
        res = convert_to_arabic('MMMMDCLXXXIII')
        self.assertEqual(4683, res)

    def test_MMMMDCLXXXIV(self):
        res = convert_to_arabic('MMMMDCLXXXIV')
        self.assertEqual(4684, res)

    def test_MMMMDCLXXXV(self):
        res = convert_to_arabic('MMMMDCLXXXV')
        self.assertEqual(4685, res)

    def test_MMMMDCLXXXVI(self):
        res = convert_to_arabic('MMMMDCLXXXVI')
        self.assertEqual(4686, res)

    def test_MMMMDCLXXXVII(self):
        res = convert_to_arabic('MMMMDCLXXXVII')
        self.assertEqual(4687, res)

    def test_MMMMDCLXXXVIII(self):
        res = convert_to_arabic('MMMMDCLXXXVIII')
        self.assertEqual(4688, res)

    def test_MMMMDCLXXXIX(self):
        res = convert_to_arabic('MMMMDCLXXXIX')
        self.assertEqual(4689, res)

    def test_MMMMDCXC(self):
        res = convert_to_arabic('MMMMDCXC')
        self.assertEqual(4690, res)

    def test_MMMMDCXCI(self):
        res = convert_to_arabic('MMMMDCXCI')
        self.assertEqual(4691, res)

    def test_MMMMDCXCII(self):
        res = convert_to_arabic('MMMMDCXCII')
        self.assertEqual(4692, res)

    def test_MMMMDCXCIII(self):
        res = convert_to_arabic('MMMMDCXCIII')
        self.assertEqual(4693, res)

    def test_MMMMDCXCIV(self):
        res = convert_to_arabic('MMMMDCXCIV')
        self.assertEqual(4694, res)

    def test_MMMMDCXCV(self):
        res = convert_to_arabic('MMMMDCXCV')
        self.assertEqual(4695, res)

    def test_MMMMDCXCVI(self):
        res = convert_to_arabic('MMMMDCXCVI')
        self.assertEqual(4696, res)

    def test_MMMMDCXCVII(self):
        res = convert_to_arabic('MMMMDCXCVII')
        self.assertEqual(4697, res)

    def test_MMMMDCXCVIII(self):
        res = convert_to_arabic('MMMMDCXCVIII')
        self.assertEqual(4698, res)

    def test_MMMMDCXCIX(self):
        res = convert_to_arabic('MMMMDCXCIX')
        self.assertEqual(4699, res)

    def test_MMMMDCC(self):
        res = convert_to_arabic('MMMMDCC')
        self.assertEqual(4700, res)

    def test_MMMMDCCI(self):
        res = convert_to_arabic('MMMMDCCI')
        self.assertEqual(4701, res)

    def test_MMMMDCCII(self):
        res = convert_to_arabic('MMMMDCCII')
        self.assertEqual(4702, res)

    def test_MMMMDCCIII(self):
        res = convert_to_arabic('MMMMDCCIII')
        self.assertEqual(4703, res)

    def test_MMMMDCCIV(self):
        res = convert_to_arabic('MMMMDCCIV')
        self.assertEqual(4704, res)

    def test_MMMMDCCV(self):
        res = convert_to_arabic('MMMMDCCV')
        self.assertEqual(4705, res)

    def test_MMMMDCCVI(self):
        res = convert_to_arabic('MMMMDCCVI')
        self.assertEqual(4706, res)

    def test_MMMMDCCVII(self):
        res = convert_to_arabic('MMMMDCCVII')
        self.assertEqual(4707, res)

    def test_MMMMDCCVIII(self):
        res = convert_to_arabic('MMMMDCCVIII')
        self.assertEqual(4708, res)

    def test_MMMMDCCIX(self):
        res = convert_to_arabic('MMMMDCCIX')
        self.assertEqual(4709, res)

    def test_MMMMDCCX(self):
        res = convert_to_arabic('MMMMDCCX')
        self.assertEqual(4710, res)

    def test_MMMMDCCXI(self):
        res = convert_to_arabic('MMMMDCCXI')
        self.assertEqual(4711, res)

    def test_MMMMDCCXII(self):
        res = convert_to_arabic('MMMMDCCXII')
        self.assertEqual(4712, res)

    def test_MMMMDCCXIII(self):
        res = convert_to_arabic('MMMMDCCXIII')
        self.assertEqual(4713, res)

    def test_MMMMDCCXIV(self):
        res = convert_to_arabic('MMMMDCCXIV')
        self.assertEqual(4714, res)

    def test_MMMMDCCXV(self):
        res = convert_to_arabic('MMMMDCCXV')
        self.assertEqual(4715, res)

    def test_MMMMDCCXVI(self):
        res = convert_to_arabic('MMMMDCCXVI')
        self.assertEqual(4716, res)

    def test_MMMMDCCXVII(self):
        res = convert_to_arabic('MMMMDCCXVII')
        self.assertEqual(4717, res)

    def test_MMMMDCCXVIII(self):
        res = convert_to_arabic('MMMMDCCXVIII')
        self.assertEqual(4718, res)

    def test_MMMMDCCXIX(self):
        res = convert_to_arabic('MMMMDCCXIX')
        self.assertEqual(4719, res)

    def test_MMMMDCCXX(self):
        res = convert_to_arabic('MMMMDCCXX')
        self.assertEqual(4720, res)

    def test_MMMMDCCXXI(self):
        res = convert_to_arabic('MMMMDCCXXI')
        self.assertEqual(4721, res)

    def test_MMMMDCCXXII(self):
        res = convert_to_arabic('MMMMDCCXXII')
        self.assertEqual(4722, res)

    def test_MMMMDCCXXIII(self):
        res = convert_to_arabic('MMMMDCCXXIII')
        self.assertEqual(4723, res)

    def test_MMMMDCCXXIV(self):
        res = convert_to_arabic('MMMMDCCXXIV')
        self.assertEqual(4724, res)

    def test_MMMMDCCXXV(self):
        res = convert_to_arabic('MMMMDCCXXV')
        self.assertEqual(4725, res)

    def test_MMMMDCCXXVI(self):
        res = convert_to_arabic('MMMMDCCXXVI')
        self.assertEqual(4726, res)

    def test_MMMMDCCXXVII(self):
        res = convert_to_arabic('MMMMDCCXXVII')
        self.assertEqual(4727, res)

    def test_MMMMDCCXXVIII(self):
        res = convert_to_arabic('MMMMDCCXXVIII')
        self.assertEqual(4728, res)

    def test_MMMMDCCXXIX(self):
        res = convert_to_arabic('MMMMDCCXXIX')
        self.assertEqual(4729, res)

    def test_MMMMDCCXXX(self):
        res = convert_to_arabic('MMMMDCCXXX')
        self.assertEqual(4730, res)

    def test_MMMMDCCXXXI(self):
        res = convert_to_arabic('MMMMDCCXXXI')
        self.assertEqual(4731, res)

    def test_MMMMDCCXXXII(self):
        res = convert_to_arabic('MMMMDCCXXXII')
        self.assertEqual(4732, res)

    def test_MMMMDCCXXXIII(self):
        res = convert_to_arabic('MMMMDCCXXXIII')
        self.assertEqual(4733, res)

    def test_MMMMDCCXXXIV(self):
        res = convert_to_arabic('MMMMDCCXXXIV')
        self.assertEqual(4734, res)

    def test_MMMMDCCXXXV(self):
        res = convert_to_arabic('MMMMDCCXXXV')
        self.assertEqual(4735, res)

    def test_MMMMDCCXXXVI(self):
        res = convert_to_arabic('MMMMDCCXXXVI')
        self.assertEqual(4736, res)

    def test_MMMMDCCXXXVII(self):
        res = convert_to_arabic('MMMMDCCXXXVII')
        self.assertEqual(4737, res)

    def test_MMMMDCCXXXVIII(self):
        res = convert_to_arabic('MMMMDCCXXXVIII')
        self.assertEqual(4738, res)

    def test_MMMMDCCXXXIX(self):
        res = convert_to_arabic('MMMMDCCXXXIX')
        self.assertEqual(4739, res)

    def test_MMMMDCCXL(self):
        res = convert_to_arabic('MMMMDCCXL')
        self.assertEqual(4740, res)

    def test_MMMMDCCXLI(self):
        res = convert_to_arabic('MMMMDCCXLI')
        self.assertEqual(4741, res)

    def test_MMMMDCCXLII(self):
        res = convert_to_arabic('MMMMDCCXLII')
        self.assertEqual(4742, res)

    def test_MMMMDCCXLIII(self):
        res = convert_to_arabic('MMMMDCCXLIII')
        self.assertEqual(4743, res)

    def test_MMMMDCCXLIV(self):
        res = convert_to_arabic('MMMMDCCXLIV')
        self.assertEqual(4744, res)

    def test_MMMMDCCXLV(self):
        res = convert_to_arabic('MMMMDCCXLV')
        self.assertEqual(4745, res)

    def test_MMMMDCCXLVI(self):
        res = convert_to_arabic('MMMMDCCXLVI')
        self.assertEqual(4746, res)

    def test_MMMMDCCXLVII(self):
        res = convert_to_arabic('MMMMDCCXLVII')
        self.assertEqual(4747, res)

    def test_MMMMDCCXLVIII(self):
        res = convert_to_arabic('MMMMDCCXLVIII')
        self.assertEqual(4748, res)

    def test_MMMMDCCXLIX(self):
        res = convert_to_arabic('MMMMDCCXLIX')
        self.assertEqual(4749, res)

    def test_MMMMDCCL(self):
        res = convert_to_arabic('MMMMDCCL')
        self.assertEqual(4750, res)

    def test_MMMMDCCLI(self):
        res = convert_to_arabic('MMMMDCCLI')
        self.assertEqual(4751, res)

    def test_MMMMDCCLII(self):
        res = convert_to_arabic('MMMMDCCLII')
        self.assertEqual(4752, res)

    def test_MMMMDCCLIII(self):
        res = convert_to_arabic('MMMMDCCLIII')
        self.assertEqual(4753, res)

    def test_MMMMDCCLIV(self):
        res = convert_to_arabic('MMMMDCCLIV')
        self.assertEqual(4754, res)

    def test_MMMMDCCLV(self):
        res = convert_to_arabic('MMMMDCCLV')
        self.assertEqual(4755, res)

    def test_MMMMDCCLVI(self):
        res = convert_to_arabic('MMMMDCCLVI')
        self.assertEqual(4756, res)

    def test_MMMMDCCLVII(self):
        res = convert_to_arabic('MMMMDCCLVII')
        self.assertEqual(4757, res)

    def test_MMMMDCCLVIII(self):
        res = convert_to_arabic('MMMMDCCLVIII')
        self.assertEqual(4758, res)

    def test_MMMMDCCLIX(self):
        res = convert_to_arabic('MMMMDCCLIX')
        self.assertEqual(4759, res)

    def test_MMMMDCCLX(self):
        res = convert_to_arabic('MMMMDCCLX')
        self.assertEqual(4760, res)

    def test_MMMMDCCLXI(self):
        res = convert_to_arabic('MMMMDCCLXI')
        self.assertEqual(4761, res)

    def test_MMMMDCCLXII(self):
        res = convert_to_arabic('MMMMDCCLXII')
        self.assertEqual(4762, res)

    def test_MMMMDCCLXIII(self):
        res = convert_to_arabic('MMMMDCCLXIII')
        self.assertEqual(4763, res)

    def test_MMMMDCCLXIV(self):
        res = convert_to_arabic('MMMMDCCLXIV')
        self.assertEqual(4764, res)

    def test_MMMMDCCLXV(self):
        res = convert_to_arabic('MMMMDCCLXV')
        self.assertEqual(4765, res)

    def test_MMMMDCCLXVI(self):
        res = convert_to_arabic('MMMMDCCLXVI')
        self.assertEqual(4766, res)

    def test_MMMMDCCLXVII(self):
        res = convert_to_arabic('MMMMDCCLXVII')
        self.assertEqual(4767, res)

    def test_MMMMDCCLXVIII(self):
        res = convert_to_arabic('MMMMDCCLXVIII')
        self.assertEqual(4768, res)

    def test_MMMMDCCLXIX(self):
        res = convert_to_arabic('MMMMDCCLXIX')
        self.assertEqual(4769, res)

    def test_MMMMDCCLXX(self):
        res = convert_to_arabic('MMMMDCCLXX')
        self.assertEqual(4770, res)

    def test_MMMMDCCLXXI(self):
        res = convert_to_arabic('MMMMDCCLXXI')
        self.assertEqual(4771, res)

    def test_MMMMDCCLXXII(self):
        res = convert_to_arabic('MMMMDCCLXXII')
        self.assertEqual(4772, res)

    def test_MMMMDCCLXXIII(self):
        res = convert_to_arabic('MMMMDCCLXXIII')
        self.assertEqual(4773, res)

    def test_MMMMDCCLXXIV(self):
        res = convert_to_arabic('MMMMDCCLXXIV')
        self.assertEqual(4774, res)

    def test_MMMMDCCLXXV(self):
        res = convert_to_arabic('MMMMDCCLXXV')
        self.assertEqual(4775, res)

    def test_MMMMDCCLXXVI(self):
        res = convert_to_arabic('MMMMDCCLXXVI')
        self.assertEqual(4776, res)

    def test_MMMMDCCLXXVII(self):
        res = convert_to_arabic('MMMMDCCLXXVII')
        self.assertEqual(4777, res)

    def test_MMMMDCCLXXVIII(self):
        res = convert_to_arabic('MMMMDCCLXXVIII')
        self.assertEqual(4778, res)

    def test_MMMMDCCLXXIX(self):
        res = convert_to_arabic('MMMMDCCLXXIX')
        self.assertEqual(4779, res)

    def test_MMMMDCCLXXX(self):
        res = convert_to_arabic('MMMMDCCLXXX')
        self.assertEqual(4780, res)

    def test_MMMMDCCLXXXI(self):
        res = convert_to_arabic('MMMMDCCLXXXI')
        self.assertEqual(4781, res)

    def test_MMMMDCCLXXXII(self):
        res = convert_to_arabic('MMMMDCCLXXXII')
        self.assertEqual(4782, res)

    def test_MMMMDCCLXXXIII(self):
        res = convert_to_arabic('MMMMDCCLXXXIII')
        self.assertEqual(4783, res)

    def test_MMMMDCCLXXXIV(self):
        res = convert_to_arabic('MMMMDCCLXXXIV')
        self.assertEqual(4784, res)

    def test_MMMMDCCLXXXV(self):
        res = convert_to_arabic('MMMMDCCLXXXV')
        self.assertEqual(4785, res)

    def test_MMMMDCCLXXXVI(self):
        res = convert_to_arabic('MMMMDCCLXXXVI')
        self.assertEqual(4786, res)

    def test_MMMMDCCLXXXVII(self):
        res = convert_to_arabic('MMMMDCCLXXXVII')
        self.assertEqual(4787, res)

    def test_MMMMDCCLXXXVIII(self):
        res = convert_to_arabic('MMMMDCCLXXXVIII')
        self.assertEqual(4788, res)

    def test_MMMMDCCLXXXIX(self):
        res = convert_to_arabic('MMMMDCCLXXXIX')
        self.assertEqual(4789, res)

    def test_MMMMDCCXC(self):
        res = convert_to_arabic('MMMMDCCXC')
        self.assertEqual(4790, res)

    def test_MMMMDCCXCI(self):
        res = convert_to_arabic('MMMMDCCXCI')
        self.assertEqual(4791, res)

    def test_MMMMDCCXCII(self):
        res = convert_to_arabic('MMMMDCCXCII')
        self.assertEqual(4792, res)

    def test_MMMMDCCXCIII(self):
        res = convert_to_arabic('MMMMDCCXCIII')
        self.assertEqual(4793, res)

    def test_MMMMDCCXCIV(self):
        res = convert_to_arabic('MMMMDCCXCIV')
        self.assertEqual(4794, res)

    def test_MMMMDCCXCV(self):
        res = convert_to_arabic('MMMMDCCXCV')
        self.assertEqual(4795, res)

    def test_MMMMDCCXCVI(self):
        res = convert_to_arabic('MMMMDCCXCVI')
        self.assertEqual(4796, res)

    def test_MMMMDCCXCVII(self):
        res = convert_to_arabic('MMMMDCCXCVII')
        self.assertEqual(4797, res)

    def test_MMMMDCCXCVIII(self):
        res = convert_to_arabic('MMMMDCCXCVIII')
        self.assertEqual(4798, res)

    def test_MMMMDCCXCIX(self):
        res = convert_to_arabic('MMMMDCCXCIX')
        self.assertEqual(4799, res)

    def test_MMMMDCCC(self):
        res = convert_to_arabic('MMMMDCCC')
        self.assertEqual(4800, res)

    def test_MMMMDCCCI(self):
        res = convert_to_arabic('MMMMDCCCI')
        self.assertEqual(4801, res)

    def test_MMMMDCCCII(self):
        res = convert_to_arabic('MMMMDCCCII')
        self.assertEqual(4802, res)

    def test_MMMMDCCCIII(self):
        res = convert_to_arabic('MMMMDCCCIII')
        self.assertEqual(4803, res)

    def test_MMMMDCCCIV(self):
        res = convert_to_arabic('MMMMDCCCIV')
        self.assertEqual(4804, res)

    def test_MMMMDCCCV(self):
        res = convert_to_arabic('MMMMDCCCV')
        self.assertEqual(4805, res)

    def test_MMMMDCCCVI(self):
        res = convert_to_arabic('MMMMDCCCVI')
        self.assertEqual(4806, res)

    def test_MMMMDCCCVII(self):
        res = convert_to_arabic('MMMMDCCCVII')
        self.assertEqual(4807, res)

    def test_MMMMDCCCVIII(self):
        res = convert_to_arabic('MMMMDCCCVIII')
        self.assertEqual(4808, res)

    def test_MMMMDCCCIX(self):
        res = convert_to_arabic('MMMMDCCCIX')
        self.assertEqual(4809, res)

    def test_MMMMDCCCX(self):
        res = convert_to_arabic('MMMMDCCCX')
        self.assertEqual(4810, res)

    def test_MMMMDCCCXI(self):
        res = convert_to_arabic('MMMMDCCCXI')
        self.assertEqual(4811, res)

    def test_MMMMDCCCXII(self):
        res = convert_to_arabic('MMMMDCCCXII')
        self.assertEqual(4812, res)

    def test_MMMMDCCCXIII(self):
        res = convert_to_arabic('MMMMDCCCXIII')
        self.assertEqual(4813, res)

    def test_MMMMDCCCXIV(self):
        res = convert_to_arabic('MMMMDCCCXIV')
        self.assertEqual(4814, res)

    def test_MMMMDCCCXV(self):
        res = convert_to_arabic('MMMMDCCCXV')
        self.assertEqual(4815, res)

    def test_MMMMDCCCXVI(self):
        res = convert_to_arabic('MMMMDCCCXVI')
        self.assertEqual(4816, res)

    def test_MMMMDCCCXVII(self):
        res = convert_to_arabic('MMMMDCCCXVII')
        self.assertEqual(4817, res)

    def test_MMMMDCCCXVIII(self):
        res = convert_to_arabic('MMMMDCCCXVIII')
        self.assertEqual(4818, res)

    def test_MMMMDCCCXIX(self):
        res = convert_to_arabic('MMMMDCCCXIX')
        self.assertEqual(4819, res)

    def test_MMMMDCCCXX(self):
        res = convert_to_arabic('MMMMDCCCXX')
        self.assertEqual(4820, res)

    def test_MMMMDCCCXXI(self):
        res = convert_to_arabic('MMMMDCCCXXI')
        self.assertEqual(4821, res)

    def test_MMMMDCCCXXII(self):
        res = convert_to_arabic('MMMMDCCCXXII')
        self.assertEqual(4822, res)

    def test_MMMMDCCCXXIII(self):
        res = convert_to_arabic('MMMMDCCCXXIII')
        self.assertEqual(4823, res)

    def test_MMMMDCCCXXIV(self):
        res = convert_to_arabic('MMMMDCCCXXIV')
        self.assertEqual(4824, res)

    def test_MMMMDCCCXXV(self):
        res = convert_to_arabic('MMMMDCCCXXV')
        self.assertEqual(4825, res)

    def test_MMMMDCCCXXVI(self):
        res = convert_to_arabic('MMMMDCCCXXVI')
        self.assertEqual(4826, res)

    def test_MMMMDCCCXXVII(self):
        res = convert_to_arabic('MMMMDCCCXXVII')
        self.assertEqual(4827, res)

    def test_MMMMDCCCXXVIII(self):
        res = convert_to_arabic('MMMMDCCCXXVIII')
        self.assertEqual(4828, res)

    def test_MMMMDCCCXXIX(self):
        res = convert_to_arabic('MMMMDCCCXXIX')
        self.assertEqual(4829, res)

    def test_MMMMDCCCXXX(self):
        res = convert_to_arabic('MMMMDCCCXXX')
        self.assertEqual(4830, res)

    def test_MMMMDCCCXXXI(self):
        res = convert_to_arabic('MMMMDCCCXXXI')
        self.assertEqual(4831, res)

    def test_MMMMDCCCXXXII(self):
        res = convert_to_arabic('MMMMDCCCXXXII')
        self.assertEqual(4832, res)

    def test_MMMMDCCCXXXIII(self):
        res = convert_to_arabic('MMMMDCCCXXXIII')
        self.assertEqual(4833, res)

    def test_MMMMDCCCXXXIV(self):
        res = convert_to_arabic('MMMMDCCCXXXIV')
        self.assertEqual(4834, res)

    def test_MMMMDCCCXXXV(self):
        res = convert_to_arabic('MMMMDCCCXXXV')
        self.assertEqual(4835, res)

    def test_MMMMDCCCXXXVI(self):
        res = convert_to_arabic('MMMMDCCCXXXVI')
        self.assertEqual(4836, res)

    def test_MMMMDCCCXXXVII(self):
        res = convert_to_arabic('MMMMDCCCXXXVII')
        self.assertEqual(4837, res)

    def test_MMMMDCCCXXXVIII(self):
        res = convert_to_arabic('MMMMDCCCXXXVIII')
        self.assertEqual(4838, res)

    def test_MMMMDCCCXXXIX(self):
        res = convert_to_arabic('MMMMDCCCXXXIX')
        self.assertEqual(4839, res)

    def test_MMMMDCCCXL(self):
        res = convert_to_arabic('MMMMDCCCXL')
        self.assertEqual(4840, res)

    def test_MMMMDCCCXLI(self):
        res = convert_to_arabic('MMMMDCCCXLI')
        self.assertEqual(4841, res)

    def test_MMMMDCCCXLII(self):
        res = convert_to_arabic('MMMMDCCCXLII')
        self.assertEqual(4842, res)

    def test_MMMMDCCCXLIII(self):
        res = convert_to_arabic('MMMMDCCCXLIII')
        self.assertEqual(4843, res)

    def test_MMMMDCCCXLIV(self):
        res = convert_to_arabic('MMMMDCCCXLIV')
        self.assertEqual(4844, res)

    def test_MMMMDCCCXLV(self):
        res = convert_to_arabic('MMMMDCCCXLV')
        self.assertEqual(4845, res)

    def test_MMMMDCCCXLVI(self):
        res = convert_to_arabic('MMMMDCCCXLVI')
        self.assertEqual(4846, res)

    def test_MMMMDCCCXLVII(self):
        res = convert_to_arabic('MMMMDCCCXLVII')
        self.assertEqual(4847, res)

    def test_MMMMDCCCXLVIII(self):
        res = convert_to_arabic('MMMMDCCCXLVIII')
        self.assertEqual(4848, res)

    def test_MMMMDCCCXLIX(self):
        res = convert_to_arabic('MMMMDCCCXLIX')
        self.assertEqual(4849, res)

    def test_MMMMDCCCL(self):
        res = convert_to_arabic('MMMMDCCCL')
        self.assertEqual(4850, res)

    def test_MMMMDCCCLI(self):
        res = convert_to_arabic('MMMMDCCCLI')
        self.assertEqual(4851, res)

    def test_MMMMDCCCLII(self):
        res = convert_to_arabic('MMMMDCCCLII')
        self.assertEqual(4852, res)

    def test_MMMMDCCCLIII(self):
        res = convert_to_arabic('MMMMDCCCLIII')
        self.assertEqual(4853, res)

    def test_MMMMDCCCLIV(self):
        res = convert_to_arabic('MMMMDCCCLIV')
        self.assertEqual(4854, res)

    def test_MMMMDCCCLV(self):
        res = convert_to_arabic('MMMMDCCCLV')
        self.assertEqual(4855, res)

    def test_MMMMDCCCLVI(self):
        res = convert_to_arabic('MMMMDCCCLVI')
        self.assertEqual(4856, res)

    def test_MMMMDCCCLVII(self):
        res = convert_to_arabic('MMMMDCCCLVII')
        self.assertEqual(4857, res)

    def test_MMMMDCCCLVIII(self):
        res = convert_to_arabic('MMMMDCCCLVIII')
        self.assertEqual(4858, res)

    def test_MMMMDCCCLIX(self):
        res = convert_to_arabic('MMMMDCCCLIX')
        self.assertEqual(4859, res)

    def test_MMMMDCCCLX(self):
        res = convert_to_arabic('MMMMDCCCLX')
        self.assertEqual(4860, res)

    def test_MMMMDCCCLXI(self):
        res = convert_to_arabic('MMMMDCCCLXI')
        self.assertEqual(4861, res)

    def test_MMMMDCCCLXII(self):
        res = convert_to_arabic('MMMMDCCCLXII')
        self.assertEqual(4862, res)

    def test_MMMMDCCCLXIII(self):
        res = convert_to_arabic('MMMMDCCCLXIII')
        self.assertEqual(4863, res)

    def test_MMMMDCCCLXIV(self):
        res = convert_to_arabic('MMMMDCCCLXIV')
        self.assertEqual(4864, res)

    def test_MMMMDCCCLXV(self):
        res = convert_to_arabic('MMMMDCCCLXV')
        self.assertEqual(4865, res)

    def test_MMMMDCCCLXVI(self):
        res = convert_to_arabic('MMMMDCCCLXVI')
        self.assertEqual(4866, res)

    def test_MMMMDCCCLXVII(self):
        res = convert_to_arabic('MMMMDCCCLXVII')
        self.assertEqual(4867, res)

    def test_MMMMDCCCLXVIII(self):
        res = convert_to_arabic('MMMMDCCCLXVIII')
        self.assertEqual(4868, res)

    def test_MMMMDCCCLXIX(self):
        res = convert_to_arabic('MMMMDCCCLXIX')
        self.assertEqual(4869, res)

    def test_MMMMDCCCLXX(self):
        res = convert_to_arabic('MMMMDCCCLXX')
        self.assertEqual(4870, res)

    def test_MMMMDCCCLXXI(self):
        res = convert_to_arabic('MMMMDCCCLXXI')
        self.assertEqual(4871, res)

    def test_MMMMDCCCLXXII(self):
        res = convert_to_arabic('MMMMDCCCLXXII')
        self.assertEqual(4872, res)

    def test_MMMMDCCCLXXIII(self):
        res = convert_to_arabic('MMMMDCCCLXXIII')
        self.assertEqual(4873, res)

    def test_MMMMDCCCLXXIV(self):
        res = convert_to_arabic('MMMMDCCCLXXIV')
        self.assertEqual(4874, res)

    def test_MMMMDCCCLXXV(self):
        res = convert_to_arabic('MMMMDCCCLXXV')
        self.assertEqual(4875, res)

    def test_MMMMDCCCLXXVI(self):
        res = convert_to_arabic('MMMMDCCCLXXVI')
        self.assertEqual(4876, res)

    def test_MMMMDCCCLXXVII(self):
        res = convert_to_arabic('MMMMDCCCLXXVII')
        self.assertEqual(4877, res)

    def test_MMMMDCCCLXXVIII(self):
        res = convert_to_arabic('MMMMDCCCLXXVIII')
        self.assertEqual(4878, res)

    def test_MMMMDCCCLXXIX(self):
        res = convert_to_arabic('MMMMDCCCLXXIX')
        self.assertEqual(4879, res)

    def test_MMMMDCCCLXXX(self):
        res = convert_to_arabic('MMMMDCCCLXXX')
        self.assertEqual(4880, res)

    def test_MMMMDCCCLXXXI(self):
        res = convert_to_arabic('MMMMDCCCLXXXI')
        self.assertEqual(4881, res)

    def test_MMMMDCCCLXXXII(self):
        res = convert_to_arabic('MMMMDCCCLXXXII')
        self.assertEqual(4882, res)

    def test_MMMMDCCCLXXXIII(self):
        res = convert_to_arabic('MMMMDCCCLXXXIII')
        self.assertEqual(4883, res)

    def test_MMMMDCCCLXXXIV(self):
        res = convert_to_arabic('MMMMDCCCLXXXIV')
        self.assertEqual(4884, res)

    def test_MMMMDCCCLXXXV(self):
        res = convert_to_arabic('MMMMDCCCLXXXV')
        self.assertEqual(4885, res)

    def test_MMMMDCCCLXXXVI(self):
        res = convert_to_arabic('MMMMDCCCLXXXVI')
        self.assertEqual(4886, res)

    def test_MMMMDCCCLXXXVII(self):
        res = convert_to_arabic('MMMMDCCCLXXXVII')
        self.assertEqual(4887, res)

    def test_MMMMDCCCLXXXVIII(self):
        res = convert_to_arabic('MMMMDCCCLXXXVIII')
        self.assertEqual(4888, res)

    def test_MMMMDCCCLXXXIX(self):
        res = convert_to_arabic('MMMMDCCCLXXXIX')
        self.assertEqual(4889, res)

    def test_MMMMDCCCXC(self):
        res = convert_to_arabic('MMMMDCCCXC')
        self.assertEqual(4890, res)

    def test_MMMMDCCCXCI(self):
        res = convert_to_arabic('MMMMDCCCXCI')
        self.assertEqual(4891, res)

    def test_MMMMDCCCXCII(self):
        res = convert_to_arabic('MMMMDCCCXCII')
        self.assertEqual(4892, res)

    def test_MMMMDCCCXCIII(self):
        res = convert_to_arabic('MMMMDCCCXCIII')
        self.assertEqual(4893, res)

    def test_MMMMDCCCXCIV(self):
        res = convert_to_arabic('MMMMDCCCXCIV')
        self.assertEqual(4894, res)

    def test_MMMMDCCCXCV(self):
        res = convert_to_arabic('MMMMDCCCXCV')
        self.assertEqual(4895, res)

    def test_MMMMDCCCXCVI(self):
        res = convert_to_arabic('MMMMDCCCXCVI')
        self.assertEqual(4896, res)

    def test_MMMMDCCCXCVII(self):
        res = convert_to_arabic('MMMMDCCCXCVII')
        self.assertEqual(4897, res)

    def test_MMMMDCCCXCVIII(self):
        res = convert_to_arabic('MMMMDCCCXCVIII')
        self.assertEqual(4898, res)

    def test_MMMMDCCCXCIX(self):
        res = convert_to_arabic('MMMMDCCCXCIX')
        self.assertEqual(4899, res)

    def test_MMMMCM(self):
        res = convert_to_arabic('MMMMCM')
        self.assertEqual(4900, res)

    def test_MMMMCMI(self):
        res = convert_to_arabic('MMMMCMI')
        self.assertEqual(4901, res)

    def test_MMMMCMII(self):
        res = convert_to_arabic('MMMMCMII')
        self.assertEqual(4902, res)

    def test_MMMMCMIII(self):
        res = convert_to_arabic('MMMMCMIII')
        self.assertEqual(4903, res)

    def test_MMMMCMIV(self):
        res = convert_to_arabic('MMMMCMIV')
        self.assertEqual(4904, res)

    def test_MMMMCMV(self):
        res = convert_to_arabic('MMMMCMV')
        self.assertEqual(4905, res)

    def test_MMMMCMVI(self):
        res = convert_to_arabic('MMMMCMVI')
        self.assertEqual(4906, res)

    def test_MMMMCMVII(self):
        res = convert_to_arabic('MMMMCMVII')
        self.assertEqual(4907, res)

    def test_MMMMCMVIII(self):
        res = convert_to_arabic('MMMMCMVIII')
        self.assertEqual(4908, res)

    def test_MMMMCMIX(self):
        res = convert_to_arabic('MMMMCMIX')
        self.assertEqual(4909, res)

    def test_MMMMCMX(self):
        res = convert_to_arabic('MMMMCMX')
        self.assertEqual(4910, res)

    def test_MMMMCMXI(self):
        res = convert_to_arabic('MMMMCMXI')
        self.assertEqual(4911, res)

    def test_MMMMCMXII(self):
        res = convert_to_arabic('MMMMCMXII')
        self.assertEqual(4912, res)

    def test_MMMMCMXIII(self):
        res = convert_to_arabic('MMMMCMXIII')
        self.assertEqual(4913, res)

    def test_MMMMCMXIV(self):
        res = convert_to_arabic('MMMMCMXIV')
        self.assertEqual(4914, res)

    def test_MMMMCMXV(self):
        res = convert_to_arabic('MMMMCMXV')
        self.assertEqual(4915, res)

    def test_MMMMCMXVI(self):
        res = convert_to_arabic('MMMMCMXVI')
        self.assertEqual(4916, res)

    def test_MMMMCMXVII(self):
        res = convert_to_arabic('MMMMCMXVII')
        self.assertEqual(4917, res)

    def test_MMMMCMXVIII(self):
        res = convert_to_arabic('MMMMCMXVIII')
        self.assertEqual(4918, res)

    def test_MMMMCMXIX(self):
        res = convert_to_arabic('MMMMCMXIX')
        self.assertEqual(4919, res)

    def test_MMMMCMXX(self):
        res = convert_to_arabic('MMMMCMXX')
        self.assertEqual(4920, res)

    def test_MMMMCMXXI(self):
        res = convert_to_arabic('MMMMCMXXI')
        self.assertEqual(4921, res)

    def test_MMMMCMXXII(self):
        res = convert_to_arabic('MMMMCMXXII')
        self.assertEqual(4922, res)

    def test_MMMMCMXXIII(self):
        res = convert_to_arabic('MMMMCMXXIII')
        self.assertEqual(4923, res)

    def test_MMMMCMXXIV(self):
        res = convert_to_arabic('MMMMCMXXIV')
        self.assertEqual(4924, res)

    def test_MMMMCMXXV(self):
        res = convert_to_arabic('MMMMCMXXV')
        self.assertEqual(4925, res)

    def test_MMMMCMXXVI(self):
        res = convert_to_arabic('MMMMCMXXVI')
        self.assertEqual(4926, res)

    def test_MMMMCMXXVII(self):
        res = convert_to_arabic('MMMMCMXXVII')
        self.assertEqual(4927, res)

    def test_MMMMCMXXVIII(self):
        res = convert_to_arabic('MMMMCMXXVIII')
        self.assertEqual(4928, res)

    def test_MMMMCMXXIX(self):
        res = convert_to_arabic('MMMMCMXXIX')
        self.assertEqual(4929, res)

    def test_MMMMCMXXX(self):
        res = convert_to_arabic('MMMMCMXXX')
        self.assertEqual(4930, res)

    def test_MMMMCMXXXI(self):
        res = convert_to_arabic('MMMMCMXXXI')
        self.assertEqual(4931, res)

    def test_MMMMCMXXXII(self):
        res = convert_to_arabic('MMMMCMXXXII')
        self.assertEqual(4932, res)

    def test_MMMMCMXXXIII(self):
        res = convert_to_arabic('MMMMCMXXXIII')
        self.assertEqual(4933, res)

    def test_MMMMCMXXXIV(self):
        res = convert_to_arabic('MMMMCMXXXIV')
        self.assertEqual(4934, res)

    def test_MMMMCMXXXV(self):
        res = convert_to_arabic('MMMMCMXXXV')
        self.assertEqual(4935, res)

    def test_MMMMCMXXXVI(self):
        res = convert_to_arabic('MMMMCMXXXVI')
        self.assertEqual(4936, res)

    def test_MMMMCMXXXVII(self):
        res = convert_to_arabic('MMMMCMXXXVII')
        self.assertEqual(4937, res)

    def test_MMMMCMXXXVIII(self):
        res = convert_to_arabic('MMMMCMXXXVIII')
        self.assertEqual(4938, res)

    def test_MMMMCMXXXIX(self):
        res = convert_to_arabic('MMMMCMXXXIX')
        self.assertEqual(4939, res)

    def test_MMMMCMXL(self):
        res = convert_to_arabic('MMMMCMXL')
        self.assertEqual(4940, res)

    def test_MMMMCMXLI(self):
        res = convert_to_arabic('MMMMCMXLI')
        self.assertEqual(4941, res)

    def test_MMMMCMXLII(self):
        res = convert_to_arabic('MMMMCMXLII')
        self.assertEqual(4942, res)

    def test_MMMMCMXLIII(self):
        res = convert_to_arabic('MMMMCMXLIII')
        self.assertEqual(4943, res)

    def test_MMMMCMXLIV(self):
        res = convert_to_arabic('MMMMCMXLIV')
        self.assertEqual(4944, res)

    def test_MMMMCMXLV(self):
        res = convert_to_arabic('MMMMCMXLV')
        self.assertEqual(4945, res)

    def test_MMMMCMXLVI(self):
        res = convert_to_arabic('MMMMCMXLVI')
        self.assertEqual(4946, res)

    def test_MMMMCMXLVII(self):
        res = convert_to_arabic('MMMMCMXLVII')
        self.assertEqual(4947, res)

    def test_MMMMCMXLVIII(self):
        res = convert_to_arabic('MMMMCMXLVIII')
        self.assertEqual(4948, res)

    def test_MMMMCMXLIX(self):
        res = convert_to_arabic('MMMMCMXLIX')
        self.assertEqual(4949, res)

    def test_MMMMCML(self):
        res = convert_to_arabic('MMMMCML')
        self.assertEqual(4950, res)

    def test_MMMMCMLI(self):
        res = convert_to_arabic('MMMMCMLI')
        self.assertEqual(4951, res)

    def test_MMMMCMLII(self):
        res = convert_to_arabic('MMMMCMLII')
        self.assertEqual(4952, res)

    def test_MMMMCMLIII(self):
        res = convert_to_arabic('MMMMCMLIII')
        self.assertEqual(4953, res)

    def test_MMMMCMLIV(self):
        res = convert_to_arabic('MMMMCMLIV')
        self.assertEqual(4954, res)

    def test_MMMMCMLV(self):
        res = convert_to_arabic('MMMMCMLV')
        self.assertEqual(4955, res)

    def test_MMMMCMLVI(self):
        res = convert_to_arabic('MMMMCMLVI')
        self.assertEqual(4956, res)

    def test_MMMMCMLVII(self):
        res = convert_to_arabic('MMMMCMLVII')
        self.assertEqual(4957, res)

    def test_MMMMCMLVIII(self):
        res = convert_to_arabic('MMMMCMLVIII')
        self.assertEqual(4958, res)

    def test_MMMMCMLIX(self):
        res = convert_to_arabic('MMMMCMLIX')
        self.assertEqual(4959, res)

    def test_MMMMCMLX(self):
        res = convert_to_arabic('MMMMCMLX')
        self.assertEqual(4960, res)

    def test_MMMMCMLXI(self):
        res = convert_to_arabic('MMMMCMLXI')
        self.assertEqual(4961, res)

    def test_MMMMCMLXII(self):
        res = convert_to_arabic('MMMMCMLXII')
        self.assertEqual(4962, res)

    def test_MMMMCMLXIII(self):
        res = convert_to_arabic('MMMMCMLXIII')
        self.assertEqual(4963, res)

    def test_MMMMCMLXIV(self):
        res = convert_to_arabic('MMMMCMLXIV')
        self.assertEqual(4964, res)

    def test_MMMMCMLXV(self):
        res = convert_to_arabic('MMMMCMLXV')
        self.assertEqual(4965, res)

    def test_MMMMCMLXVI(self):
        res = convert_to_arabic('MMMMCMLXVI')
        self.assertEqual(4966, res)

    def test_MMMMCMLXVII(self):
        res = convert_to_arabic('MMMMCMLXVII')
        self.assertEqual(4967, res)

    def test_MMMMCMLXVIII(self):
        res = convert_to_arabic('MMMMCMLXVIII')
        self.assertEqual(4968, res)

    def test_MMMMCMLXIX(self):
        res = convert_to_arabic('MMMMCMLXIX')
        self.assertEqual(4969, res)

    def test_MMMMCMLXX(self):
        res = convert_to_arabic('MMMMCMLXX')
        self.assertEqual(4970, res)

    def test_MMMMCMLXXI(self):
        res = convert_to_arabic('MMMMCMLXXI')
        self.assertEqual(4971, res)

    def test_MMMMCMLXXII(self):
        res = convert_to_arabic('MMMMCMLXXII')
        self.assertEqual(4972, res)

    def test_MMMMCMLXXIII(self):
        res = convert_to_arabic('MMMMCMLXXIII')
        self.assertEqual(4973, res)

    def test_MMMMCMLXXIV(self):
        res = convert_to_arabic('MMMMCMLXXIV')
        self.assertEqual(4974, res)

    def test_MMMMCMLXXV(self):
        res = convert_to_arabic('MMMMCMLXXV')
        self.assertEqual(4975, res)

    def test_MMMMCMLXXVI(self):
        res = convert_to_arabic('MMMMCMLXXVI')
        self.assertEqual(4976, res)

    def test_MMMMCMLXXVII(self):
        res = convert_to_arabic('MMMMCMLXXVII')
        self.assertEqual(4977, res)

    def test_MMMMCMLXXVIII(self):
        res = convert_to_arabic('MMMMCMLXXVIII')
        self.assertEqual(4978, res)

    def test_MMMMCMLXXIX(self):
        res = convert_to_arabic('MMMMCMLXXIX')
        self.assertEqual(4979, res)

    def test_MMMMCMLXXX(self):
        res = convert_to_arabic('MMMMCMLXXX')
        self.assertEqual(4980, res)

    def test_MMMMCMLXXXI(self):
        res = convert_to_arabic('MMMMCMLXXXI')
        self.assertEqual(4981, res)

    def test_MMMMCMLXXXII(self):
        res = convert_to_arabic('MMMMCMLXXXII')
        self.assertEqual(4982, res)

    def test_MMMMCMLXXXIII(self):
        res = convert_to_arabic('MMMMCMLXXXIII')
        self.assertEqual(4983, res)

    def test_MMMMCMLXXXIV(self):
        res = convert_to_arabic('MMMMCMLXXXIV')
        self.assertEqual(4984, res)

    def test_MMMMCMLXXXV(self):
        res = convert_to_arabic('MMMMCMLXXXV')
        self.assertEqual(4985, res)

    def test_MMMMCMLXXXVI(self):
        res = convert_to_arabic('MMMMCMLXXXVI')
        self.assertEqual(4986, res)

    def test_MMMMCMLXXXVII(self):
        res = convert_to_arabic('MMMMCMLXXXVII')
        self.assertEqual(4987, res)

    def test_MMMMCMLXXXVIII(self):
        res = convert_to_arabic('MMMMCMLXXXVIII')
        self.assertEqual(4988, res)

    def test_MMMMCMLXXXIX(self):
        res = convert_to_arabic('MMMMCMLXXXIX')
        self.assertEqual(4989, res)

    def test_MMMMCMXC(self):
        res = convert_to_arabic('MMMMCMXC')
        self.assertEqual(4990, res)

    def test_MMMMCMXCI(self):
        res = convert_to_arabic('MMMMCMXCI')
        self.assertEqual(4991, res)

    def test_MMMMCMXCII(self):
        res = convert_to_arabic('MMMMCMXCII')
        self.assertEqual(4992, res)

    def test_MMMMCMXCIII(self):
        res = convert_to_arabic('MMMMCMXCIII')
        self.assertEqual(4993, res)

    def test_MMMMCMXCIV(self):
        res = convert_to_arabic('MMMMCMXCIV')
        self.assertEqual(4994, res)

    def test_MMMMCMXCV(self):
        res = convert_to_arabic('MMMMCMXCV')
        self.assertEqual(4995, res)

    def test_MMMMCMXCVI(self):
        res = convert_to_arabic('MMMMCMXCVI')
        self.assertEqual(4996, res)

    def test_MMMMCMXCVII(self):
        res = convert_to_arabic('MMMMCMXCVII')
        self.assertEqual(4997, res)

    def test_MMMMCMXCVIII(self):
        res = convert_to_arabic('MMMMCMXCVIII')
        self.assertEqual(4998, res)

    def test_MMMMCMXCIX(self):
        res = convert_to_arabic('MMMMCMXCIX')
        self.assertEqual(4999, res)


if __name__ == '__main__':
    unittest.main()
