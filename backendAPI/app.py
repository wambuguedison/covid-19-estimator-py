#!flask/bin/python
from flask import Flask, jsonify, abort, request

from src.estimator import estimator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return jsonify({
    'message': "This is the covid 19 estimator api" 
  });

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
  
  return jsonify(estimator(data))
