#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return "This is the covid 19 estimator api"
  
if __name__ == '__main__':
  app.run(debug=True)