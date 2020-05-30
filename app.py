from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My pytorch model got deleted, so deployment will be delayed.'

if __name__ == '__main__':
    app.run()