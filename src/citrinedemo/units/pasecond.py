import math

import utils
from base import PlaneAngleUnit


class PASecond(PlaneAngleUnit):

  @property
  def name(self):
    return 'second'

  @property
  def symbol(self):
    return '"'

  @property
  def si_unit_conversion(self):
    # supports string conversion to keep float length
    return utils.long_float_to_str(math.pi / 648000)
