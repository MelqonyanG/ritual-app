import ast
from algebraic_operations.exceptions import (
    UnsupportedFunction,
    DivisionByZero,
    InvalidExpression,
)


class ExpressionEvaluator(ast.NodeVisitor):
    """
    Evaluates arithmetic and functional expressions parsed from AST nodes.

    Methods:
        visit_Num(self, node): Visits and processes numeric nodes.
        visit_Str(self, node): Visits and processes string nodes.
        visit_BinOp(self, node): Visits and processes binary operation nodes.
        visit_UnaryOp(self, node): Visits and processes unary operation nodes.
        visit_Call(self, node): Visits and processes call nodes.
        visit_Expr(self, node): Visits and processes expression nodes.

    Functions:
        evaluate_expression(expression): Evaluates the given arithmetic or functional expression.
    """

    def visit_Num(self, node):
        """
        Processes numeric nodes.

        Args:
            node: Numeric node from the AST.

        Returns:
            int or float: Value of the numeric node.
        """
        return node.n

    def visit_Str(self, node):
        """
        Processes string nodes.

        Args:
            node: String node from the AST.

        Returns:
            str: Value of the string node.
        """
        return node.s


    def visit_BinOp(self, node):
        """
        Processes binary operation nodes.

        Args:
            node: Binary operation node from the AST.

        Returns:
            int or float: Result of the binary operation.
        Raises:
            DivisionByZero: If division by zero is encountered.
        """
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            if right == 0:
                raise DivisionByZero()
            return left / right

    def visit_UnaryOp(self, node):
        """
        Processes unary operation nodes.

        Args:
            node: Unary operation node from the AST.

        Returns:
            int or float: Result of the unary operation.
        Raises:
            UnsupportedFunction: If an unsupported function is used.
        """
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.Call):
            if isinstance(node.op.func, ast.Name) and node.op.func.id == 'len':
                return len(operand)
            elif isinstance(node.op.func, ast.Name) and node.op.func.id == 'abs':
                return abs(operand)
            else:
                raise UnsupportedFunction()

    def visit_Call(self, node):
        """
        Processes call nodes.

        Args:
            node: Call node from the AST.

        Returns:
            int or float: Result of the call operation.
        Raises:
            UnsupportedFunction: If an unsupported function is used.
        """
        if isinstance(node.func, ast.Name):
            if node.func.id == 'len':
                return len(self.visit(node.args[0]))
            elif node.func.id == 'abs':
                return abs(self.visit(node.args[0]))
            else:
                raise UnsupportedFunction()

    def visit_Expr(self, node):
        """
        Processes expression nodes.

        Args:
            node: Expression node from the AST.

        Returns:
            int or float: Result of the expression node.
        """
        return self.visit(node.value)


def evaluate_expression(expression):
    """
    Evaluates an expression using the ExpressionEvaluator.

    Args:
        expression (str): The arithmetic or functional expression to evaluate.

    Returns:
        int, float, or result of the expression evaluation.

    Raises:
        InvalidExpression: If the expression is invalid or cannot be evaluated.
        DivisionByZero: If division by zero is encountered during evaluation.
        UnsupportedFunction: If an unsupported function is used in the expression.
    """
    evaluator = ExpressionEvaluator()
    parsed_expression = ast.parse(expression, mode='eval')
    result = evaluator.visit(parsed_expression.body)

    if result is None:
        raise InvalidExpression()

    return result