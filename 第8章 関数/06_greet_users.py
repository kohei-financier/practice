def greet_users(names):
    for name in names:
        msg = f"こんにちは{name.title()}！"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)