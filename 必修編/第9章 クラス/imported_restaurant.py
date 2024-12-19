from restaurant import Restaurant

print("-----------------")
restaurant = Restaurant('malaychan', '東南アジア料理')
restaurant.describe_restaurant()

print(f"\n料理の提供数：{restaurant.number_served}")