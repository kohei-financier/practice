class Average():

    def __init__(self, name, japanese, english):
        self.name = name
        self.japanese = japanese
        self.english = english

    def average(self):
        return (self.japanese + self.english) / 2
    
    def get_name(self):
        return self.name
    
    def get_avarage(self):
        return self.average
    
man1 = Average("Taro", 60, 30)
man2 = Average("Jiro", 80, 90)

print(f"{man1.name}は、日本語が{man1.japanese}点で、英語は{man1.english}点で、平均点が{man1.average()}です")
print(f"{man2.name}は、日本語が{man2.japanese}点で、英語は{man2.english}点で、平均点が{man2.average()}です")
