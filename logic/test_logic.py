import unittest
from core_logic import convert_to_decimal
from core_logic import convert_to_quinary
from core_logic import add
from core_logic import subtract
from core_logic import multiply
from core_logic import divide
from core_logic import sqrt
from core_logic import square

class TestLogic(unittest.TestCase):
    def testConvertToDecimal(self):
        self.assertEqual(convert_to_decimal(104), 29)

    def testConvertToQuinary(self):
        self.assertEqual(convert_to_quinary(29), 104)

    def testAddition(self):
        self.assertEqual(add(14, 42), 111)
        self.assertEqual(add(-3, -24), -32)

    def testSubtraction(self):
        self.assertEqual(subtract(10, 4), 1)
        self.assertEqual(subtract(-3,-24), 21)

    def testMultiplication(self):
        self.assertEqual(multiply(4, 10), 40)
        self.assertEqual(multiply(4, -10), -40)

    def testDivision(self):
        self.assertEqual(divide(100, 1), 100)
        self.assertEqual(divide(40, 4), 10)
        self.assertEqual(divide(1234, 0), "Cannot divide by zero")

    def testSquare(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(11), 121)
        self.assertEqual(square(-14), 311)

    def testSqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(121), 11)
        self.assertEqual(sqrt(-3), "No root")

if __name__ == '__main__':
    unittest.main()
