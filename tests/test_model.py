import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_initial_expression_is_empty(self):
        self.assertEqual("", self.calculator.expression)

    def test_digit(self):
        self.calculator.digit(1)
        self.assertEqual("1", self.calculator.expression)

    def test_plus(self):
        self.calculator.plus()
        self.assertEqual("+", self.calculator.expression)

    def test_minus(self):
        self.calculator.minus()
        self.assertEqual("-", self.calculator.expression)
    
    def test_multiply(self):
        self.calculator.multiply()
        self.assertEqual("*", self.calculator.expression)
    
    def test_divide(self):
        self.calculator.divide()
        self.assertEqual("/", self.calculator.expression)


class TestCalculatorUsage(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_expression_insertion(self):
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(2)
        self.assertEqual("1+2", self.calculator.expression)

    def test_compute_result(self):
        self.calculator.expression = "1+2"
        self.assertEqual(3, self.calculator.compute_result())

    def test_compute_result_with_invalid_expression(self):
        self.calculator.expression = "1+"
        with self.assertRaises(ValueError) as context:
            self.calculator.compute_result()
        self.assertEqual("Invalid expression: 1+", str(context.exception))

class TestComplexExpression(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_usage_of_parentheses(self):
        #(1+2)*3=9
        self.calculator.open_parentheses()
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(2)
        self.calculator.close_parentheses()
        self.calculator.multiply()
        self.calculator.digit(3)
        self.assertEqual("(1+2)*3", self.calculator.expression)
        self.assertEqual(9, self.calculator.compute_result())
    
    def test_usage_of_square_root_expression(self):
        #1+sqrt(11-2)=4
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.square_root() #append "sqrt(" to the expression
        self.calculator.digit(1)
        self.calculator.digit(1)
        self.calculator.minus()
        self.calculator.digit(2)
        self.calculator.close_parentheses()
        self.assertEqual("1+sqrt(11-2)", self.calculator.expression)
        self.assertEqual(4, self.calculator.compute_result())

    def test_usage_of_power(self):
        #2**3=8
        self.calculator.digit(2)
        self.calculator.power() #append "**" to the expression
        self.calculator.digit(3)
        self.assertEqual("2**3", self.calculator.expression)
        self.assertEqual(8, self.calculator.compute_result())