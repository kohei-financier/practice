# 9-5
class User():

    """ユーザーのプロフィールを表すクラス"""

    def __init__(self, first_name, last_name, username, email, location):
        """ユーザーを初期化する"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """ユーザーの情報を出力する"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  ユーザー名: {self.username}")
        print(f"  メールアドレス: {self.email}")
        print(f"  場所: {self.location}")

    def greet_user(self):
        """ユーザー宛のあいさつメッセージを出力する"""
        print(f"\nおかえりなさい{self.username}！")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

        self.privileges = Privileges()


class Privileges():
    
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\n管理者の権限一覧")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- このユーザーには権限がありません。")


# takanory = Admin('takanori', 'suzuki', 'takanory', 'takanory@example.com',
#                 'toshima-ku')
# takanory.describe_user()
# takanory.privileges.show_privileges()

# takanory_privileges = [
#     '投稿を追加する',
#     "投稿を削除する",
#     "ユーザーを利用禁止にする"
# ]

# takanory.privileges.privileges = takanory_privileges
# takanory.privileges.show_privileges()
""" 
takanory.show_privileges()

takanory.greet_user()

print("-------------")
takanory.increment_login_attempts()
takanory.increment_login_attempts()
takanory.increment_login_attempts()
print(f"ログイン試行回数：{takanory.login_attempts}")

print("ログイン回数をリセットする")
takanory.reset_login_attempts()
print(f"ログイン試行回数：{takanory.login_attempts}") """

