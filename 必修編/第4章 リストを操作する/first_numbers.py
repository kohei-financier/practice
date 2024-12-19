# 数値の配列
for value in range(1, 5):
    print(value)

# range ※引数は添え字になる
for value in range(1,6):
    print(value)

# リストを作成する
numbers = list(range(1, 6))
print(numbers)

# range()に3つ目の引数を与えると、ステップ数になる
even_numbers = list(range(2, 11, 2)) # ->2step設定に(2,4,6.....)
print(even_numbers)

# 10までの2乗の数をリストとして生成する
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 上のリストを1行でも書ける
squares = []
squares = [value**2 for value in range(1,11)]
print(squares)

# 練習問題
print("--------------------------------")
# 4-3
# for value in range(1,20):
#     print(value)

# 4-4
# for value in range(1, 1_000_001):
#     print(value)

# 4-5
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6
'''
for numbers in range(1, 20, 2):
    print(numbers)
'''

# 4-7
""" for numbers in range(3, 31, 3):
    print(numbers) """

# 4-8
""" squares = [value**3 for value in range(1,11)]
print(squares) """

numbers = list(range(1,11))
print(sum(numbers))

for numbers in range(2, 11, 2):
    print(numbers**2*3.14)