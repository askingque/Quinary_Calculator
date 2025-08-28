import unittest
from logic_1 import convert_to_decimal
from logic_1 import convert_to_quinary
from logic_1 import add
from logic_1 import subtract
from logic_1 import multiply
from logic_1 import divide
from logic_1 import sqrt
from logic_1 import square


class TestLogic(unittest.TestCase):
    def testConvertToDecimal(self):
        self.assertEqual(convert_to_decimal(1), 1)

    def testConvertToQuinary(self):
        self.assertEqual(convert_to_quinary(5), 10)

    def testAddition(self):
        self.assertEqual(add(1, 5), 11)

    def testSubtraction(self):
        self.assertEqual(subtract(5,10), 15)

    def testMultiplication(self):
        self.assertEqual(multiply(5, 10), 15)

    def testDivision(self):
        self.assertEqual(divide(5, 10), 15)

    def testSquare(self):
        self.assertEqual(square(5), 5)

    def testSqrt(self):
        self.assertEqual(sqrt(5), 5)