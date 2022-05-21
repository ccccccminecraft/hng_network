import json
from RedisController import RedisController

# サーバーリストに新規サーバーを登録するスクリプトです

# テスト用データ
data = {
    "server_name": "Mohist Home Server",
    "game": "minecraft",
    "owner": "CCCCCC",
    "address": "192.168.0.176:25566",
    "players": "",
    "ping": ""
}

redis_controller = RedisController()
redis_controller.insert_server(data)
