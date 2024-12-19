prompt = "あなたが誰か教えてくれたら、あなた向けの挨拶をします"
prompt += "\nあなたの名前は？"

name = input(prompt)
print(f"\nこんにちは！{name}!")

# 数字を入れても、文字列型になっている
age = input("何歳ですか？")
age = int(age)
age >= 18
print(f"\nあなたは{age}歳です！")