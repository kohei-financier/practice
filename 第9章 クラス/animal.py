class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("動物が鳴いています")

class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("ワンワン")
    
    def fetch(self):
        print("ボールを取りに行った！")

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("にゃー")
    
    def scratch(self):
        print("爪を研いでいる！")

dog1 = Dog('チワワ', 3)
cat1 = Cat('アメリカンショートヘアー', 2)

dog1.speak()
dog1.fetch()

cat1.speak()
cat1.scratch()