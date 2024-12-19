# リストをコピーする
my_foods = ['ピザ', 'だんご', 'ケーキ']
friend_foods = my_foods[:]

my_foods.append('チョコレート')
friend_foods.append('アイスクリーム')

print("私の好きな食べ物")
print(my_foods)

print("\n友達が好きな食べ物")
print(friend_foods)

# ※注意※　代入するだけだと、別のリストが生成されない！
my_foods = ['ピザ', 'だんご', 'ケーキ']
# 代入
friend_foods = my_foods

my_foods.append('チョコレート')
friend_foods.append('アイスクリーム')

print("\n私の好きな食べ物")
print(my_foods)

print("\n友達が好きな食べ物")
print(friend_foods)