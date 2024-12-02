# 並べ替え

# sort() →　ABC順に並べ替え
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # → ['audi', 'bmw', 'subaru', 'toyota']

# reverse=True → 逆順に並び替え
cars.sort(reverse=True)
print(cars) # → ['toyota', 'subaru', 'bmw', 'audi']

# 日本語の場合は、文字コード順に並び変えられる
cars = ['bmw', 'アウディ', '豊田', 'すばる']
cars.sort()
print(cars) # → ['bmw', 'すばる', 'アウディ', '豊田']


# sorted()だと、一時的な入れ替えになる
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars) # → ['bmw', 'audi', 'toyota', 'subaru']  

print(sorted(cars)) # → ['audi', 'bmw', 'subaru', 'toyota']  

print(cars) # → ['bmw', 'audi', 'toyota', 'subaru']


# 逆順で出力する　reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars) # → ['subaru', 'toyota', 'audi', 'bmw']

