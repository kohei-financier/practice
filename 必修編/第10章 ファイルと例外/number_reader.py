import json
filename = '第10章 ファイルと例外\\numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)