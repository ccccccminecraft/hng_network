import redis


class RedisController:
    def insert_server(self, data):
        r = redis.Redis(host="redis", port=6379, db=0)
        r.hset(f"server_status:{data['game']}:{data['server_name']}", mapping=data)

    # redisからデータ取得
    # ゲーム:サーバー名で検索
    def get_server_status(self, game, server_name):
        r = redis.Redis(host="redis", port=6379, db=0, decode_responses= True)

        res = r.hgetall(f"server_status:{game}:{server_name}")
        return res

    # ゲームで検索
    def get_game_server_status(self, game):
        r = redis.Redis(host="redis", port=6379, db=0, decode_responses= True)

        res = []
        keys = r.scan(match=f"server_status:{game}*")
        for key in keys[1]:
            res.append(r.hgetall(key))

        return res

    # 全サーバー検索
    def get_all_server_status(self):
        r = redis.Redis(host="redis", port=6379, db=0, decode_responses= True)

        res = []
        keys = r.scan(match="server_status:*")
        for key in keys[1]:
            res.append(r.hgetall(key))

        return res


# デバッグ用
if __name__ == "__main__":
    debug_r = RedisController()
    debug_r.insert_server_status()
    print(debug_r.get_server_status("minecraft", "ccserver"))
    print(debug_r.get_game_server_status("minecraft"))
    print(debug_r.get_all_server_status())
