#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])z
def index():
  return "This is the covid 19 estimator api"
