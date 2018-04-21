import math

import utils
from base import PlaneAngleUnit


class Degree(PlaneAngleUnit):

  @property
  def name(self):
    return 'degree'

  @property
  def symbol(self):
    return u'\xb0'  # the degree symbol

  @property
  def si_unit_conversion(self):
    # keep a long float for conversion to a string since python will auto e-notation
    return utils.long_float_to_str(math.pi / 180)
