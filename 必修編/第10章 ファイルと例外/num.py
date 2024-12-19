import json

filename = '第10章 ファイルと例外\\num.txt'
number = input("あなたの好きな数字は？")
               
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f"あなたの好きな数字を知っています! それは{number}です！")