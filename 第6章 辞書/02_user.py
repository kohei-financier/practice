# 辞書をループしたいとき

# 辞書を登録
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# ループ処理
# forのあとに取り出したい箱を設定、user_0の辞書に書かれているものを代入する
for key, value in user_0.items():
    print(f"\nキー: {key}")
    print(f"値: {value}")
