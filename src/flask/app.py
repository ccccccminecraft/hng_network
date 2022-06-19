from flask import Flask
from flask_cors import CORS
import json
from RedisController import RedisController

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

@app.route("/")
def index():
    return "hng_network"

@app.route("/minecraft")
def minecraft():
    redis_controller = RedisController()
    res = redis_controller.get_game_server_status("minecraft")
    ret = []
    for server in res:
        ret.append({
            "server_name": server["server_name"],
            "game": server["game"],
            "global_address": server["global_address"],
            "players": server["players"],
            "ping": server["ping"],
        })
    return json.dumps(ret)

if __name__ == '__main__':
    # 今のところは適宜コメントアウトして運用
    # ローカル実行時
    # app.run(host="0.0.0.0", debug=True)
    
    # サーバー実行時
    app.run(host="0.0.0.0")
    