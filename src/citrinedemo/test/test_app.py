import json
import unittest

import app


class AppTests(unittest.TestCase):

  def setUp(self):
    app.app.testing = True
    self.app = app.app.test_client()

  def test_index(self):
    rv = self.app.get('/')
    self.assertEquals(rv.data, 'Hello, World!')

  def test_single_unit(self):
    rv = self.app.get('/units/si?units=degree')
    self.assertEquals(
      json.loads(rv.data),
      {
        "multiplication_factor": 0.017453292519943,
        "unit_name": "rad"
      }
    )

  def test_multiple_units(self):
    rv = self.app.get('/units/si?units=degree/minute')
    self.assertEquals(
      json.loads(rv.data),
      {
        "multiplication_factor": 0.00029088820866572, 
        "unit_name": "rad/s"
      }
    )

  def test_multiple_units_spacing(self):
    rv = self.app.get('/units/si?units=degree / minute')
    self.assertEquals(
      json.loads(rv.data),
      {
        "multiplication_factor": 0.00029088820866572,
        "unit_name": "rad / s"
      }
    )

  def test_complex_units(self):
    rv = self.app.get('/units/si?units=(degree/(minute*hectare))')
    self.assertEquals(
      json.loads(rv.data),
      {
        "multiplication_factor": 2.9088820866572e-08,
        "unit_name": "(rad/(s*m2))"
      }
    )

  def test_invalid_unit(self):
    rv = self.app.get('/units/si?units=bogus')
    self.assertEquals(
      json.loads(rv.data),
      {
        "error": "Invalid Unit Type",
        "message": "bogus is not a valid unit"
      }
    )
