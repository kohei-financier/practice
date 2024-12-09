""" num = int(input())
if num > 0:
    print(f"{num}円の収入です")
elif num == 0:
    print(f"0以外の整数を入力してください")
else:
    print(f"{num}円の収入です") """


""" for i in range(1, 11):
    print('HELLO!')

for value in range(1,11):
    print(value) """

""" num = list(range(1, 11))
print(num)
# sum = sum(num)
# print(sum)

print(num[0:3])
print(num[-1:])

names = []
names.append('ドラえもん')
names.append('のび太')
names.append('ジャイアン')
print(names)

names.remove('ジャイアン')
print(names) """

""" nums = [-10, 2, -8, 5]
minus,plus = 0,0
for value in nums:
    if value < 0:
        print(f"{value}円支出")
        minus += value
    else:
        print(f"{value}円収入")
        plus += value

print(minus)
print(plus) """

person = {'氏名': '鈴木一郎', '住所':'東京都'}
for key, value in person.items():
    print(f"{key}:{value}")

person['メール'] = "メール"

