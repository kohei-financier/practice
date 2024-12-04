motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# motocycles[0] = 'ducati'
# print(motocycles)

motocycles.append('ducati')
print(motocycles)

# appendで配列に要素を追加する
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

print(motocycles)

# 指定した要素番号に要素を追加する
motocycles = ['honda', 'yamaha', 'suzuki']
motocycles.insert(0, 'dacati')
print(motocycles)

# リストから要素を削除する del
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)

# popメソッドを利用して要素を削除する
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
popped_motocycle = motocycles.pop() #pop（リストからは取り出される）されてpopped~に代入される
print(motocycles) # → ['honda', 'yamaha']
print(popped_motocycle) # → suzuki (popされた要素は配列としては格納されていないことに注意が必要)

# popメソッドも要素数を指定することが可能
motocycles = ['honda', 'yamaha', 'suzuki']
first_owned = motocycles.pop(0) # →このように要素数を入れることができる
print(f"最初に手に入れたバイクは{first_owned.title()}です")

#削除したい値の位置が不明な場合は、remove()メソッドを使う
motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)

motocycles.remove('ducati') #要素数が分からなくても値を直接指定で削除可能
print(motocycles)

too_expensive = 'yamaha'
motocycles.remove(too_expensive) #値を代入した形でも使用可能
print(motocycles)

# 以下練習

# リストを作成
member = ['mother', 'father', 'brother', 'sister', 'me']

# memberを変更する
member[4] = 'grandmother'
print(member)

# memberを追加する
member.append('grandfather')
print(member) 

member.insert(0, 'me')
print(member)

# memberから取り出したり、削除したりする
del member[0]
popped_member = member.pop(0)
member.remove('father')
print(member)