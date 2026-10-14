# README

！！！！！！！！！masterブランチで直接コミットしないこと！！！！！！！

minecraftのサーバーを監視して、ステータスをreturnします

## セットアップ

ホストに
docker
docker-compose
は入れておいてくだしあ
(一応一番下に導入方法は書きました)

## 初回のみ dockerのビルド

/src ディレクトリで
```shell
docker-compose build --no-cache
```
を実行

## 環境立ち上げ

/src ディレクトリで
```shell
docker-compose up -d
```

## flaskを起動

1. flaskのコンテナ内にbashで入る

```shell
docker exec -it src_flask_1 bash
```

2. flaskを起動する

```shell
python3 app.py
```

ローカル開発では SSL を設定しなくても HTTP で起動できます。API は次の URL からアクセスします。

```text
http://localhost:5000/{エンドポイント}
```

## サーバーで HTTPS を有効にする

`src/.env` を作成し、サーバー上の証明書と秘密鍵のパスを設定します。パスは Flask コンテナ内から見える場所を指定してください。証明書ファイルは `src/flask/.pem/` に置く構成なら、以下を使えます。

```dotenv
HNG_SSL_ENABLED=true
HNG_PORT=443
HNG_SSL_CERT_PATH=./.pem/cert.pem
HNG_SSL_KEY_PATH=./.pem/server_secret.key
```

この設定で `docker-compose up -d` を実行すると HTTPS で起動し、API は `https://<サーバーのホスト名>/{エンドポイント}` からアクセスできます。SSL を使わない場合は `HNG_SSL_ENABLED=false`（既定値）にし、`HNG_PORT` は省略するか `5000` にしてください。

## メモ

オーナーは
Windows10 + Ubuntu(WSL2)
環境で開発してます

## docker install方法

(自分の環境) docker インストール
で検索したほうがはやい

1. [ここ](https://docs.docker.com/desktop/windows/install/)からDocker Desktop for WindowsでDL。
2. インストーラーを起動
3. [Docker hub](https://hub.docker.com/)でアカウントを作成
4. Accept画面が後ろで開かれていたらそちらにてAcceptを押す。（タコみたいなのがいる画面）

windows10 + WSL2の環境 or Ubuntu

aptで入ったっけ？

``` shell
sudo apt update
sudo apt install docker-ce
sudo apt install docker-compose
```

dockerを起動

WSL2の場合(systemctlがなんか動かないので)

```shell
service docker start
```

linux

```shell
systemctl enable docker
systemctl start docker
```
