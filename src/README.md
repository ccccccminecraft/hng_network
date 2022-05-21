# README

minecraftのサーバーを監視して、ステータスをreturnします

## セットアップ

ホストに
docker
docker-compose
は入れておいてくだしあ

## 初回ビルド

/src ディレクトリで
docker-compose build --no-cache
を実行

## 環境立ち上げ

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
pytho3 app.py
```

## apiアクセス

https://localhost:5000/{エンドポイント}
で行けるはず

## メモ

オーナーは
Windows10 + Ubuntu(WSL2)
環境で開発してます
