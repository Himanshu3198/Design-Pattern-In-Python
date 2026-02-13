class Student:
    def __init__(self,marks):
        self.__marks = marks


    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        self.__marks = value


s = Student(80)
print(s.marks)
s.marks= 90
print(s.marks)