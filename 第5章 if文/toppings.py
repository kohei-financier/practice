requested_topping = 'マッシュルーム'

if requested_topping != 'アンチョビ':
    print("アンチョビを注文してください！")

banned_users = ['andrew', 'caralina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}はコメントを書き込めます")