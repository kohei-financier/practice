from car import Car

class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"この車のバッテリーは{self.battery_size}-kWhです。")

    def get_range(self):
        if self.battery_size == 75:
            range = 420
        elif self.battery_size == 100:
            range = 510

        print(f"この車の満充電時の航続距離は約{range}kmです。")        

    def upgrade_battery(self):

        if self.battery_size == 75:
            self.battery_size = 100
            print("バッテリーを100kWhにアップグレードしました。")
        else:
            print("バッテリーはアップグレード済みです。")

    

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

print("電気自動車を作成し、航続距離を確認します。")
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()

print("\nバッテリーをアップグレードし、航続距離を再度確認します。")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

print("\nバッテリーを再度アップグレードします。")
my_tesla.battery.upgrade_battery()
