# 辞書を入れ子構造にする
users = {

    #  {key1:value1, key2:value2…}という形になっている
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nユーザー名： {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\t氏名： {full_name.title()}")
    print(f"\t名前： {location.title()}")