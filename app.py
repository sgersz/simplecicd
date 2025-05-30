from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Docker CI/CD pipeline!, this is v2.1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)