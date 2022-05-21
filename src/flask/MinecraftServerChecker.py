import json
from mcstatus import JavaServer
from RedisController import RedisController

class MinecraftServerChecker:
    # Minecraftのサーバーの情報を取得し、redisに保存
    def run(self):
        redis_controller = RedisController()
        # redisからサーバーリストを取得
        mc_servers = redis_controller.get_game_server_status("minecraft")
        
        for mc_server in mc_servers:
            # サーバーの疎通確認
            status = self.check_status(mc_server["address"])
            mc_server["players"] = status["players"]
            mc_server["ping"] = status["ping"]
            # 情報を更新してredisのデータを上書き
            redis_controller.insert_server(mc_server) 
    
    # サーバー情報を取得
    def check_status(self, address):
        server = JavaServer.lookup(address)

        ret = {
            "players": "",
            "ping": "",
        }
        try:
            status = server.status()
        except:
            return ret
        
        ret["players"] = str(status.players.online)
        ret["ping"] = str(status.latency)
        
        return ret

# デバッグ用
if __name__ == "__main__":
    checker = MinecraftServerChecker()
    res = checker.run()
