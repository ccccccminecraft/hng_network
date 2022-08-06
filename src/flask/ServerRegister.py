import json
from RedisController import RedisController

# サーバーリストに新規サーバーを登録するスクリプトです


# テスト用データ
class ServerRegister:
    def regist_server(self, data):
        redis_controller = RedisController()
        redis_controller.insert_server(data)
