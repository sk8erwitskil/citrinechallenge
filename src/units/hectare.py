from base import AreaUnit


class Hectare(AreaUnit):

  @property
  def name(self):
    return 'hectare'

  @property
  def symbol(self):
    return 'ha'

  @property
  def si_unit_conversion(self):
    return 10000
