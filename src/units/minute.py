from base import TimeUnit


class Minute(TimeUnit):

  @property
  def name(self):
    return 'minute'

  @property
  def symbol(self):
    return 'min'

  @property
  def si_unit_conversion(self):
    return 60
