class Emp:
    def __init__(self,name):
        self.name = name

class Developer(Emp):
    def __init__(self,name,langauge):
        super().__init__(name)
        self.language = langauge

    def info(self):
        print(f"name is={self.name} and language is={self.language}")


d1 = Developer("himanshu","python")
d1.info()