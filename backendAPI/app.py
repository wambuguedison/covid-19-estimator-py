#!flask/bin/python
from flask import Flask, jsonify, request, g
from dicttoxml import dicttoxml
import time

from src.estimator import estimator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return jsonify({
    'message': "This is the covid 19 estimator api" 
  })

@app.route('/api/v1/on-covid-19', methods=['POST'])
def json_api():
  data = {
    "region": {
      "name": request.json['region']['name'],
      "avgAge": request.json['region']['avgAge'],
      "avgDailyIncomeInUSD": request.json['region']['avgDailyIncomeInUSD'],
      "avgDailyIncomePopulation": request.json['region']['avgDailyIncomePopulation']
    },
    "periodType": request.json['periodType'],
    "timeToElapse": request.json['timeToElapse'],
    "reportedCases": request.json['reportedCases'],
    "population": request.json['population'],
    "totalHospitalBeds": request.json['totalHospitalBeds']
  }
  
  headers = {
    "Content-Type":'application/json',
    "charset":'utf-8'
  }
  
  return jsonify(estimator(data)), 200, headers

@app.route('/api/v1/on-covid-19/json', methods=['POST'])
def json_fallback_api():
  data = {
    "region": {
      "name": request.json['region']['name'],
      "avgAge": request.json['region']['avgAge'],
      "avgDailyIncomeInUSD": request.json['region']['avgDailyIncomeInUSD'],
      "avgDailyIncomePopulation": request.json['region']['avgDailyIncomePopulation']
    },
    "periodType": request.json['periodType'],
    "timeToElapse": request.json['timeToElapse'],
    "reportedCases": request.json['reportedCases'],
    "population": request.json['population'],
    "totalHospitalBeds": request.json['totalHospitalBeds']
  }
  
  headers = {
    "Content-Type":'application/json',
    "charset":'utf-8'
  }
  
  return jsonify(estimator(data)), 200, headers

@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def xml_api():
  data = {
    "region": {
      "name": request.json['region']['name'],
      "avgAge": request.json['region']['avgAge'],
      "avgDailyIncomeInUSD": request.json['region']['avgDailyIncomeInUSD'],
      "avgDailyIncomePopulation": request.json['region']['avgDailyIncomePopulation']
    },
    "periodType": request.json['periodType'],
    "timeToElapse": request.json['timeToElapse'],
    "reportedCases": request.json['reportedCases'],
    "population": request.json['population'],
    "totalHospitalBeds": request.json['totalHospitalBeds']
  }
  
  headers = {
    "Content-Type":'application/xml',
    "charset":'utf-8'
  }
  
  estimate = estimator(data)
  
  return dicttoxml(estimate), 200, headers
  
@app.route('/api/v1/on-covid-19/logs', methods=['GET'])
def logs():
  with open('myfile.txt') as in_file:
    content = in_file.read()
  
  headers = {
    "Content-Type":'text/plain',
    "charset":'utf-8'
  }
  return content, 200, headers

@app.before_request
def before_timer():
  g.start = time.time()

@app.after_request
def after_request(response):
  now = time.time()
  duration = round((now - g.start)*100)
  duration = str(duration)+"ms"
  duration = duration.zfill(4)
  method = request.method
  url = request.path
  status = response.status
  status = str(status)[:3]
  print('example log')
  print(duration, method, url, status)
  log = str(method + "  " + url + "    " + status + "  " + duration + "\n")
  with open("backendAPI/logs.txt", "w") as logs:
    logs.write(log)
  print('end log')
  return response