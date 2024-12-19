import json

# 以前に保存されたユーザー名があれば読み込む
# 見つからない場合、ユーザー名の入力を促し保存する

def get_stored_username():
    
    filename = '第10章 ファイルと例外\\username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():

    username = input("あなたの名前は？　")
    filename = '第10章 ファイルと例外\\username.json'
    with open(filename, 'w') as f:
        json.dump(username,f)
        return username

def greet_user():

    username = get_stored_username()

    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = get_new_username()
        print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")

greet_user()