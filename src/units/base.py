from abc import ABCMeta, abstractproperty


class BaseUnit(object):
  """
  Implements a unit type
  """

  __metaclass__ = ABCMeta

  @abstractproperty
  def name(self):
    pass

  @abstractproperty
  def symbol(self):
    pass

  @abstractproperty
  def type(self):
    pass

  @abstractproperty
  def si_unit_conversion(self):
    pass

  def __mul__(self, other):
    """
    Allows to do cool things like (Degree() * 60)
    """

    return self.si_unit_conversion * other

  def __rmul__(self, other):
    """
    Allows to do cool things like (60 * Minute())
    """

    return other * self.si_unit_conversion

  def __div__(self, other):
    """
    Allows to do cool things like (Degree() / 60)
    """

    return self.si_unit_conversion / other

  def __rdiv__(self, other):
    """
    Allows to do cool things like (60 / Minute())
    """

    return other / self.si_unit_conversion


class TimeUnit(BaseUnit):
  """
  Implements time unit conversions in seconds
  """

  @property
  def type(self):
    return 's'


class PlaneAngleUnit(BaseUnit):
  """
  Implements plane angle unit conversions in radians
  """

  @property
  def type(self):
    return 'rad'


class AreaUnit(BaseUnit):
  """
  Implements area unit conversions in meters squared
  """

  @property
  def type(self):
    return 'm2'


class VolumeUnit(BaseUnit):
  """
  Implements volume unit conversions in cubic meters
  """

  @property
  def type(self):
    return 'm3'


class MassUnit(BaseUnit):
  """
  Implements mass unit conversions in kilograms
  """

  @property
  def type(self):
    return 'kg'
