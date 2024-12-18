class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

prius = Car('toyota', 'prius', 2010)
prius.display_info()
print("------------------------------------")
result = print("Hello World") # print関数の戻り値はnoneになるので、resultにはnoneが代入されている！
print(result)