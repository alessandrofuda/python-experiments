from flask import Flask, request, jsonify
from model.model import predict_salary
from waitress import serve

app = Flask(__name__)


# @app.route('/')
# def homepage():
#     return "Welcome to the Salary Prediction homepage"

@app.route('/api/calculate/salary', methods=['POST'])
def salary_calculation_api():
    return jsonify({
        "salary": predict_salary(request.json['experience'], request.json['level'])
    })


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
