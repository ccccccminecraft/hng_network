from ServerRegister import ServerRegister

data = {
    "server_name": "hanage_lobby",
    "game": "minecraft",
    "owner": "CCCCCC",
    "global_address": "hanage-community-servers:25565",
    "address": "hanage-community-servers:25565",
    "players": "",
    "ping": ""
}

register = ServerRegister()
register.regist_server(data)