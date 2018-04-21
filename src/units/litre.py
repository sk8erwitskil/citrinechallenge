from base import VolumeUnit


class Litre(VolumeUnit):

  @property
  def name(self):
    return 'litre'

  @property
  def symbol(self):
    return 'L'

  @property
  def si_unit_conversion(self):
    return 0.001
