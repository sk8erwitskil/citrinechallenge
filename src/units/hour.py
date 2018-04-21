from base import TimeUnit


class Hour(TimeUnit):

  @property
  def name(self):
    return 'hour'

  @property
  def symbol(self):
    return 'h'

  @property
  def si_unit_conversion(self):
    return 3600
