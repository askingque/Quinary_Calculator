import unittest
from logic import convert_to_decimal
from logic import convert_to_quinary
from logic import add
from logic import subtract
from logic import multiply
from logic import divide
from logic import sqrt
from logic import square


class TestLogic(unittest.TestCase):
    def testConvertToDecimal(self):
        self.assertEqual(convert_to_decimal(1), 1)

    def testConvertToQuinary(self):
        self.assertEqual(convert_to_quinary(5), 10)


    #ALL ARE (quinary) -> (decimal)
    def testAddition(self):
        self.assertEqual(add(1, 10), 6)

    def testSubtraction(self):
        self.assertEqual(subtract(10, 4), 1)

    def testMultiplication(self):
        self.assertEqual(multiply(4, 10), 20)

    def testDivision(self):
        self.assertEqual(divide(100, 10), 5)

    def testSquare(self):
        self.assertEqual(square(10), 25)

    def testSqrt(self):
        self.assertEqual(sqrt(100), 5)

if __name__ == '__main__':
    unittest.main()
