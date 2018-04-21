import excs
from app import app
from units import Units

from flask import jsonify, request


@app.errorhandler(excs.InvalidUnitException)
def handle_invalid_unit(error):
  response = jsonify(
    error='Invalid Unit Type',
    message=error.args[0]
  )
  response.status_code = 400
  return response


@app.errorhandler(excs.InvalidExpressionSyntaxException)
def handle_invalid_expr(error):
  response = jsonify(
    error='Invalid Syntax',
    message=error.args[0]
  )
  response.status_code = 400
  return response


@app.route('/')
def index():
  """
  Index page... not used
  """

  return 'Hello, World!'


@app.route('/units/si', methods=['GET'])
def units_si():
  """
  Converts si units
  """

  uns = Units()
  units_arg = request.args.get('units')
  res = uns.convert(units_arg)
  return jsonify(
    multiplication_factor=res.multiplication_factor,
    unit_name=res.unit_name
  )
