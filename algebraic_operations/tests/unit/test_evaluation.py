from django.test import TestCase
from algebraic_operations.operations.utils.evaluator import evaluate_expression
from algebraic_operations.exceptions import UnsupportedFunction, DivisionByZero


class ExpressionEvaluationTests(TestCase):
    def test_simple_expression(self):
        result = evaluate_expression("2 + 3 * 4")
        self.assertEqual(result, 14)

    def test_function_calls(self):
        result = evaluate_expression("abs(-5) * len('hello')")
        self.assertEqual(result, 25)

    def test_division_by_zero(self):
        with self.assertRaises(DivisionByZero):
            evaluate_expression("10 / 0")

    def test_unsupported_function(self):
        with self.assertRaises(UnsupportedFunction):
            evaluate_expression("some_function(5)")

    def test_invalid_expression(self):
        with self.assertRaises(Exception):
            evaluate_expression("2 + * 3")
