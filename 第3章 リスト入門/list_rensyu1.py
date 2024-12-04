# 空のリストを作成し、初期化
fruits = []

# 果物を追加
fruits = ['apple', 'banana', 'orange', 'lemon']
fruits.append('melon')
print(fruits)

fruits.append('watermelon')
print(fruits)

# 果物を削除する
fruits.remove('banana')
print(fruits)

popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)
