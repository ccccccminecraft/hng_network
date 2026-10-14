from flask import Flask
from flask_cors import CORS
import json
import os
import ssl
from RedisController import RedisController

app = Flask(__name__)
FILE_NAME = ""
CORS(
    app,
    supports_credentials=True
)


@app.route("/")
def index():
    return "hng_network"


@app.route('/.well-known/acme-challenge/<filename>')
def well_known(filename):
    path = f"./.well-known/{filename}"
    with open(path) as f:
        return f.read()


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
    ssl_enabled = os.getenv("HNG_SSL_ENABLED", "false").strip().lower() in {
        "1", "true", "yes", "on"
    }
    ssl_context = None
    if ssl_enabled:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        cert_path = os.getenv("HNG_SSL_CERT_PATH", "./.pem/cert.pem")
        key_path = os.getenv("HNG_SSL_KEY_PATH", "./.pem/server_secret.key")
        ssl_context.load_cert_chain(cert_path, key_path)

    default_port = "443" if ssl_enabled else "5000"
    port = int(os.getenv("HNG_PORT", default_port))
    app.run(host="0.0.0.0", port=port, ssl_context=ssl_context)
