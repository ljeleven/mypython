#__author:"longjin"
#date:  2019/8/28
# -*- coding: UTF-8 -*-

import unittest
from lianshou.testtest import fk_math

class TestFkMath(unittest.TestCase):
    def test_one_equation(self):
        self.assertEqual(fk_math.one_equation(5, 9), 1.8)
        self.assertTrue(fk_math.one_equation(4, 10) == -2.5, .00001)
        self.assertTrue(fk_math.one_equation(4, -27) == 27 / 4)
        with self.assertRaises(ValueError):
            fk_math.one_equation(0, 9)

    def test_two_equation(self):
        r1, r2 = fk_math.two_equation(1, -3, 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
        r1, r2 = fk_math.two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        r = fk_math.two_equation(1, -4, 4)
        self.assertEqual(r, 2.0, '求解出错')
        with self.assertRaises(ValueError):
            fk_math.two_equation(4, 2, 3)


if __name__ == '__main__':
    unittest.main()
