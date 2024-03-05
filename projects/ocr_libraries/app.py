from flask import Flask, render_template, request, jsonify
# from waitress import serve

app = Flask(__name__)


@app.route('/')
def homepage():
    return "aaaaaa"


if __name__ == '__main__':
    # serve(app, host="0.0.0.0", port=8080)
    app.run()
