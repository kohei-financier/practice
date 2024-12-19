import math

r = input("円の面積を求めます。半径を入力してください：")
try:
    r = float(r)
    circle = r*r*math.pi
except ValueError:
    print("数字を入力してください")
else:
    print(circle)