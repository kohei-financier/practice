class BMI():

    def __init__(self, name, weight, height): #ここで全部の初期化をしてしまう！
        self.name = name
        self.weight = weight
        self.height = height
        self.bmi = 0
        self.himando = ""
    
    # 最終的な判断に必要なのは、それぞれのBMIと肥満度なので、そのメソッド（計算式）を定義しておく

    def set_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def set_himando(self):
        if self.bmi >= 30:
            self.himando = "重度の肥満"
        elif self.bmi >= 25:
            self.himando = "軽度の肥満"
        elif self.bmi >= 18.5:
            self.himando = "標準体型"
        else:
            self.himando = "痩せ型"

    def judge(self):
        print(f"{self.name}さんは{self.himando}です", end="")

tanaka = BMI('田中', 60, 175)
tanaka.set_bmi()
tanaka.set_himando()
tanaka.judge()