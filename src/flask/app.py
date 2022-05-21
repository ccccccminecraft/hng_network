from flask import Flask
from MinecraftServerChecker import MinecraftServerChecker
app = Flask(__name__)

@app.route("/")
def index():
    return "chinchin"

@app.route("/minecraft")
def minecraft():
    checker = MinecraftServerChecker()
    ret = checker.run()
    return ret

@app.route("/days")
def days():
    return "まだないよ"

@app.route("/ark")
def ark():
    return "まだないよ"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)