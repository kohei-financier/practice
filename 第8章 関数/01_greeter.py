# 関数はdefで作る
def greet_user():
    """シンプルなあいさつメッセージを出力する"""
    print("こんにちは！")

greet_user()

# メソッドに引数を入れる
def greet_user(username): # <- このusernameは「仮引数」と言う
    """シンプルなあいさつメッセージを出力する"""
    print(f"こんにちは{username.title()}！")

greet_user('jesse') # <- この'jesse'は「実引数」と言う