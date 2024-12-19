point = int(input("試験の点数を入力してください："))
if point > 100:
    print("入力エラーです")
elif point >= 50:
    print(f"{point}点：合格です")
elif point >= 0:
    print(f"{point}点:追試です")
else:
    print(f"入力エラーです")