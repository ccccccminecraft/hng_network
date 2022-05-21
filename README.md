# README

minecraftのサーバーを監視して、ステータスをreturnします

## セットアップ

ホストに
docker
docker-compose
は入れておいてくだしあ
(一応一番下に導入方法は書きました)

## 初回のみ dockerのビルド

/src ディレクトリで
docker-compose build --no-cache
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
pytho3 app.py
```

## apiアクセス

https://localhost:5000/{エンドポイント}
で行けるはず

## メモ

オーナーは
Windows10 + Ubuntu(WSL2)
環境で開発してます

## docker install方法

(自分の環境) docker インストール
で検索したほうがはやい

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