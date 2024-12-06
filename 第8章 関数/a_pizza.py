def make_pizza(size, *toppings):
    print(f"\n{size}インチのピザを、以下のトッピングで作ります。")
    for topping in toppings:
        print(f"- {topping}")