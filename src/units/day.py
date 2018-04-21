from base import TimeUnit


class Day(TimeUnit):

  @property
  def name(self):
    return 'day'

  @property
  def symbol(self):
    return 'd'

  @property
  def si_unit_conversion(self):
    return 86400
