# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, running docker container through GitHub Actions"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
