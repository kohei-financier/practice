filename = '第10章 ファイルと例外\\guest.txt'

# 練習問題 10-3  新規作成
# with open(filename, 'w') as file_object:
#     file_object.write(input("あなたの名前は？"))

# 練習問題 10-4  名前を入力→あいさつ→名前を入力のループ
message=""
with open(filename, 'w', encoding = 'UTF-8' ) as file_object:
    while message != "終了":
        message = input("あなたの名前は？")
        if message != "終了":
            print(f"こんにちは！{message}さん！\n")
            file_object.write(f"こんにちは！{message}さん！\n")
            