# Twitter モラズbot V4

## モラズbot とは
福岡の妙齢の女モラズ [@morazumorazu](https://twitter.com/morazumorazu) こと、年齢性別不詳の謎のツイッタラー・モラズのbot のことです。

詳細参考：
- [モラズbot V4 製作の途中経過](https://note.com/arkb/n/n803ad5d54293)

## 環境

動作環境は Raspberry Pi 4。Raspbian OS のバージョンは下記です。

```
Distributor ID:	Debian
Description:	Debian GNU/Linux 11 (bullseye)
Release:	11
Codename:	bullseye
```

## モラズbot V4 のインストール

ラズパイに pi にてログインし下記コマンドでインストールします。

```
mkdir -p /home/pi/work && cd /home/pi/work
git clone https://github.com/arkB/morazubot_v4.git
cd morazubot_v4
bash install.sh
```

.env ファイルを作成し、下記 bot の TwitterID とアクセストークン等を入力します。

```
BOT_SCREEN_NAME = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
```

## モラズbot V4 使い方

1回ずつツイートする場合は下記コマンドで実行します。

```
source /home/pi/work/morazubot_v4/v4env/bin/activate
bash /home/pi/work/morazubot_v4/tweet.sh
```

実行例：
![](images/tweet.PNG)

モラズBotのフォロワーからのリプに返事をする場合は下記コマンドで実行します。

```
source /home/pi/work/morazubot_v4/v4env/bin/activate
bash /home/pi/work/morazubot_v4/reply.sh
```

実行例：
![](images/reply.PNG)
