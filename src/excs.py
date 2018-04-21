class InvalidExpressionSyntaxException(Exception):
  """
  When a user enters wrong syntax. i.e. "degree - minute"
  """

  pass


class InvalidUnitException(Exception):
  """
  When a user enters a wrong unit. i.e. degrees/liters
  """

  pass


class NameCollisionException(Exception):
  """
  When multiple units have been configured with the same name
  """

  pass


class SymbolCollisionException(Exception):
  """
  When multiple units have been configured with the same symbol
  """

  pass
