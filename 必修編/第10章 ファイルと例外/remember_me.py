import json

username = input("あなたの名前は？")

filename = "第10章 ファイルと例外\\username.json"
with open(filename, "w") as f:
    json.dump(username, f)
    print(f"戻ってきた時にも名前を覚えていますよ、{username}さん！")