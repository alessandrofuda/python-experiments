from flask import Flask  # , render_template, request, jsonify
# from waitress import serve

app = Flask(__name__)


@app.route('/')
def homepage():
    return "OOKK"


# API
# @app.route('/api/calculate/salary', methods=['POST'])
# def salary_calculation_api():
#     return jsonify({
#         "salary": predict_salary(request.json['experience'], request.json['level'])
#     })
#
#
# # WEB form
# @app.route('/calculate/salary', methods=['GET'])
# def salary_calculation_get():
#     # Jinja2 template engine is used to render html page
#     return render_template('form.html')
#
#
# @app.route('/calculate/salary', methods=['POST'])
# def salary_calculation():
#     experience = request.form['experience']
#     level = request.form['level']
#     salary = "{:.2f}".format(predict_salary(experience, level))
#     return render_template('form.html', salary=salary, experience=experience, level=level)


if __name__ == '__main__':
    app.run(debug=True)
#     serve(app, host="0.0.0.0", port=8080)
