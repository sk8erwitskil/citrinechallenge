from flask import Flask
app = Flask(__name__)
from views import *  # noqa
from encoder import DecimalJSONEncoder
app.json_encoder = DecimalJSONEncoder
