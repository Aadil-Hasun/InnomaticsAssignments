from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Welcome to the Home Page"


@app.route("/username")
def print_name():
    name = request.args.get('name')
    return name.upper()


if __name__ == '__main__':
    app.run(debug=True)
