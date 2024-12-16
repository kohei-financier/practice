filename = '第10章 ファイルと例外\\programming.txt'

# w で新規作成・上書き（データを消してしまってから作成する）
with open(filename, 'w') as file_object:
    file_object.write(f"I love programming.\n")
    file_object.write("Hello world!\n")

# a で追記（既存のデータに追記）
with open(filename, 'a') as file_object:
    file_object.write("わわわわわわわわわわわわ\n")
    file_object.write("わわわわわわわわわわわわ\n")