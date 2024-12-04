# タプル（変更や追加ができないリスト）
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 -> これはエラーになる！
# print(dimensions)

# 追加したい場合は、再定義する

print("元のサイズ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #変更のために再定義
print("\n変更したサイズ")
for dimension in dimensions:
    print(dimension)