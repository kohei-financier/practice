class Car:
    # 自動車を表すシンプルな実装例

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"走行距離は{self.odometer_reading}kmです。")

    def update_odometer(self, km):
        
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("走行距離は減らせません。")

    def increment_odometer(self, km):
        self.odometer_reading += km

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())