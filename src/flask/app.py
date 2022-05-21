from flask import Flask
import json
from RedisController import RedisController

app = Flask(__name__)

@app.route("/")
def index():
    return "chinchin"

@app.route("/minecraft")
def minecraft():
    redis_controller = RedisController()
    mc_servers = json.dumps(redis_controller.get_game_server_status("minecraft"))
    return mc_servers

@app.route("/days")
def days():
    return "まだないよ"

@app.route("/ark")
def ark():
    return "まだないよ"

if __name__ == '__main__':
    # 今のところは適宜コメントアウトして運用
    # ローカル実行時
    app.run(host="0.0.0.0", debug=True)
    
    # サーバー実行時
    # app.run(host="0.0.0.0")
    