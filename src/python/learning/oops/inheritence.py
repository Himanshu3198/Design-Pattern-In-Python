class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"barking animal is={self.name}")


class Dog(Animal):

      def __init__(self,name1):
          super().__init__(name1)

      def sound(self):
          print(f"from dog barking animal is={self.name}")


d1 = Dog("kutta")
d1.sound()
