import json
from mcstatus import JavaServer

class MinecraftServerChecker:
    def run(self):
        mc_servers = self.get_server_list()
        ret = []
        for mc_server in mc_servers:
            status = self.check_status(mc_server["address"])
            ret.append(
                {
                    "name": mc_server["server_name"],
                    "players": status["players"],
                    "ping": status["ping"]
                }
            )
        return json.dumps(ret)
    
    def get_server_list(self):
        with open ("serverlist.json", mode="rt", encoding="utf-8") as file:
            data = json.load(file)
            if data["minecraft"]:
                return data["minecraft"]
            else:
                return None
    
    def check_status(self, address):
        server = JavaServer.lookup(address)
        # もっと書きようがある
        ret = {
            "players": None,
            "ping": None,
        }
        try:
            status = server.status()
        except:
            return ret
        
        ret["players"] = status.players.online
        ret["ping"] = status.latency
        
        return ret

# デバッグ用そのうち消す
if __name__ == "__main__":
    checker = MinecraftServerChecker()
    res = checker.run()
    print(res)