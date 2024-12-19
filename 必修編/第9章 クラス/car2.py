class Car():

    def __init__(self, model, speed, hour):
        self.model = model
        self.speed = speed
        self.hour = hour
        
    def run(self):
        mileage = self.hour * self.speed
        print(f"{self.model}は、時速{self.speed}km/hで{self.hour}時間走行し、{mileage}km移動しました")

prius = Car('プリウス', 200, 2)
prius.run()
