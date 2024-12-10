# 9-4

class Restaurant():
    """レストランを表すクラス"""

    def __init__(self, name, cuisine_type):
        """レストランを初期化する"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """レストランについての情報を出力する"""
        msg = f"{self.name}は素晴らしい{self.cuisine_type}を提供します。"
        print(f"\n{msg}")

    def open_restaurant(self):
        """レストランが開店したことを知らせるメッセージを出力する"""
        msg = f"{self.name}が開店しました。ぜひご来店ください！"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='アイスクリーム'):
        super().__init__(name, cuisine_type) 
        self.flavors = []

    def show_flavors(self):
        print("\n以下のフレーバーが提供できます。")
        for flavor in self.flavors:
            print(f"-  {flavor.title()}")



restaurant = Restaurant('malaychan', '東南アジア料理')
restaurant.describe_restaurant()

print(f"\n料理の提供数：{restaurant.number_served}")
restaurant.set_number_served(46)
print(f"\n料理の提供数：{restaurant.number_served}")

restaurant.set_number_served(4567)
print(f"\n料理の提供数：{restaurant.number_served}")


restaurant.increment_number_served(164)
print(f"\n料理の提供数：{restaurant.number_served}")

blue_seal = IceCreamStand('ブルーシール')
blue_seal.flavors = ['バニラ', '抹茶', '紅イモ', 'ウベ']

blue_seal.describe_restaurant()
blue_seal.show_flavors()
