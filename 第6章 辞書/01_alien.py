# 辞書
# ｛キー：値｝で紐づけがされている
alien_0 = {'color': 'green', 'points': 5}

# 値を取り出すときは、辞書の名前の後ろに、[]でキーを囲う
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"あなたは{new_points}点獲得しました！")

# 新しく辞書を追加する場合、キーを作り、値を代入する
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# -> {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"最初のx座標： {alien_0['x_position']}")

#エイリアンは右に移動します
#現在のスピードによってエイリアンの移動距離を決定します
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 素早いエイリアン
    x_increment = 3

# 新しい位置は元の位置に移動距離を加算します
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"新しいx座標： {alien_0['x_position']}")

# キーと値を削除するときは delを使う
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
