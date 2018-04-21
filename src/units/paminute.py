import math

import utils
from base import PlaneAngleUnit


class PAMinute(PlaneAngleUnit):

  @property
  def name(self):
    # no name for this class since it collides with the minute time unit
    return None

  @property
  def symbol(self):
    return '\''

  @property
  def si_unit_conversion(self):
    # supports conversion to a string to keep float length
    return utils.long_float_to_str(math.pi / 10800)
