import decimal
import math
import re


def sigdigits(num, n=14):
  """
  Converts a float to a particular number of significant digits
  """

  return round(num, -int(math.floor(math.log10(num))) + (n - 1))


def scrub_arithmetic(arg):
  """
  Scrub acceptable arithmetic from the expression
  """

  # remove ( ) / *
  clean = re.sub('[\(|\)|\*|\/]', ' ', arg)
  # replace multiple spaces with a single space
  return re.sub('\s+', ' ', clean).strip()


def long_float(num):
  """
  Stores a long float as a decimal.Decimal to retain length
  """

  # python is dumb with long floats and will auto-e-notation them,
  # so we convert to a Decimal to not lose precision
  ctx = decimal.Context()
  ctx.prec = 50
  return ctx.create_decimal(repr(num))


def long_float_to_str(num):
  """
  Stringified version of a long float (i.e. Decimal)
  """

  d1 = long_float(num)
  return format(d1, 'f')
