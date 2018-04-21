import decimal

from flask.json import JSONEncoder


class DecimalJSONEncoder(JSONEncoder):
  """
  A flask json encoder to turn Decimals to floats
  """

  def default(self, obj):
    try:
      if isinstance(obj, decimal.Decimal):
        return float(obj)
      iterable = iter(obj)
    except TypeError:
      pass
    else:
      return list(iterable)
    return JSONEncoder.default(self, obj)
