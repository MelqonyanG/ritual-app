import ast
from algebraic_operations.exceptions import (
    UnsupportedFunction,
    DivisionByZero,
)


class ExpressionEvaluator(ast.NodeVisitor):
    def visit_Num(self, node):
        return node.n

    def visit_Str(self, node):
        return node.s

    def visit_BinOp(self, node):
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
        if isinstance(node.func, ast.Name):
            if node.func.id == 'len':
                return len(self.visit(node.args[0]))
            elif node.func.id == 'abs':
                return abs(self.visit(node.args[0]))
            else:
                raise UnsupportedFunction()

    def visit_Expr(self, node):
        return self.visit(node.value)


def evaluate_expression(expression):
    evaluator = ExpressionEvaluator()
    parsed_expression = ast.parse(expression, mode='eval')
    result = evaluator.visit(parsed_expression.body)

    return result