import unittest
from logic.logic import convert_to_decimal
from logic.logic import convert_to_quinary
from logic.logic import add
from logic.logic import subtract
from logic.logic import multiply
from logic.logic import divide
from logic.logic import sqrt
from logic.logic import square


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

if __name__ == '__main__':
    unittest.main()
