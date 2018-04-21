import ast
import operator as op

import excs


# all operators... not necessarily ones which are supported in this application
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def calc_expr(expr):
  """
  Calculates an expression from a string by parsing every operator
  """

  try:
    return _calc(ast.parse(expr, mode='eval').body)
  except Exception as e:
    raise excs.InvalidExpressionSyntaxException(str(e))


def _calc(node):
  if isinstance(node, ast.Num):
    return node.n
  elif isinstance(node, ast.BinOp):
    return operators[type(node.op)](_calc(node.left), _calc(node.right))
  elif isinstance(node, ast.UnaryOp):
    return operators[type(node.op)](_calc(node.operand))
  else:
    raise TypeError(node)
