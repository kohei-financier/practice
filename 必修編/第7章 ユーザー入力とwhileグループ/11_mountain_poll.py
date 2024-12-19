# ユーザーの入力から辞書を作る
responses = {}

# 投票がアクティブなことを示すフラグをセット
polling_active = True

while polling_active:
    # 入力プロンプトで名前と回答を受け付ける
    name = input("\nあなたのお名前は？\n")
    response = input("いつか登りたい山は何ですか？\n")

    # 解凍を辞書に保存する -> キーに値を紐づけるときは「値s[キー] = 値」
    responses[name] = response

    # 誰かほかに投票するひとがいるかどうか確認する
    repeat = input("誰か他に回答してくれる人はいますか？ (yes/no) \n")
    if repeat == 'no':
        polling_active = False

# 投票を終了し、結果を表示する
print("\n----投票結果----")
for name, response in responses.items():
    print(f"{name}さんが登りたいのは{response}です。")