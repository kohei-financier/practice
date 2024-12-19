from user2 import User

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


