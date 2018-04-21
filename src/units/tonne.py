import math

from base import MassUnit


class Tonne(MassUnit):

  @property
  def name(self):
    return 'tonne'

  @property
  def symbol(self):
    return 't'

  @property
  def si_unit_conversion(self):
    # 10 to the power of 3
    return math.pow(10, 3)
