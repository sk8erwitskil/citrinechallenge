import excs
import strexpr
import utils
from day import Day
from degree import Degree
from hectare import Hectare
from hour import Hour
from litre import Litre
from minute import Minute
from paminute import PAMinute
from pasecond import PASecond
from tonne import Tonne


class UnitConversion(object):
  """
  A conversion result
  """

  def __init__(self, multiplication_factor, unit_name):
    self.multiplication_factor = multiplication_factor
    self.unit_name = unit_name


class Units(object):
  """
  Holder class for all units and interaction with units
  """

  def __init__(self):
    self.available = {
      'day': Day(),
      'degree': Degree(),
      'hectare': Hectare(),
      'hour': Hour(),
      'litre': Litre(),
      'minute': Minute(),
      'paminute': PAMinute(),
      'pasecond': PASecond(),
      'tonne': Tonne(),
    }

    # this allows us to call Units().day for example
    for k, v in self.available.items():
      setattr(self, k, v)

    # creates a mapping from all possible inputs (i.e. second or ")
    # to the corresponding unit class
    self.mapping = {}
    for _, unit_obj in self.available.items():
      if unit_obj.symbol in self.mapping:
        raise excs.SymbolCollisionException(
          'Found multiple units with same symbol: {} / {}'.format(
            unit_obj, self.mapping[unit_obj.symbol]))
      self.mapping[unit_obj.symbol] = unit_obj
      if unit_obj.name is not None:
        if unit_obj.name in self.mapping:
          raise excs.NameCollisionException(
            'Found multiple units with same name: {} / {}'.format(
              unit_obj, self.mapping[unit_obj.name]))
        self.mapping[unit_obj.name] = unit_obj

  def _conversions(self, candidates):
    """
    Given a list of all possible candidates for conversion (minus the arithmetic)
    attempts to find the corresponding unit class. If no mapping exists,
    raises InvalidUnitException as the user entered an unsupported unit type
    """

    matches = {}
    for candidate in candidates:
      match = self.get(candidate)
      if match is None:
        raise excs.InvalidUnitException('{} is not a valid unit'.format(candidate))
      matches[candidate] = match
    return matches

  def get(self, unit_key):
    """
    Fetches a unit class for a input value or returns None
    """

    return self.mapping.get(unit_key)

  def convert(self, string):
    """
    Given an expression string attempts to convert it to
    a multiplication_factor and a unit_name
    """

    candidates = utils.scrub_arithmetic(string).split()
    expr_string = string
    name_string = string
    for ident, repl in self._conversions(candidates).items():
      expr_string = expr_string.replace(ident, str(repl.si_unit_conversion))
      name_string = name_string.replace(ident, str(repl.type))
    calculated_expression = strexpr.calc_expr(expr_string)
    calculated_sigdigits = utils.sigdigits(calculated_expression)
    calculated_float = utils.long_float(calculated_sigdigits)
    return UnitConversion(calculated_float, name_string)
