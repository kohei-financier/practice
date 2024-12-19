# *argsと書くと、下記場合だと、２個目以降の要素をため込める
def make_pizza(size, *toppings):
    print("\n{size}インチのピザを、以下のトッピングで作ります")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'ペパロニ')
make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')
