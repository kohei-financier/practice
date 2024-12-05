# 辞書
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 辞書を配列に入れる
aliens = [alien_0, alien_1, alien_2]

# ループで辞書を取り出せる
for alien in aliens:
    print(alien)

print("------------------------")

# 空のエイリアンの配列を作成する
aliens = []

# 30匹のエイリアンを生成する
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 最初の3体だけ黄色で10ポイントに変更する(配列の入れ子)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
    print(alien)

# 生成されたエイリアンの数を出力する
print(f"全エイリアンの数：{len(aliens)}")