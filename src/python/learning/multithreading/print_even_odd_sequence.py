import threading

class PrintSequence:
    def __init__(self,limit):
        self.__limit = limit
        self.__counter = 0
        self.condition = threading.Condition()


    def  odd_print(self):
        while self.__counter < self.__limit:
            with self.condition:
              while self.__counter %2 == 0:
                   self.condition.wait()

              print(f"sequence {threading.current_thread().name} = {self.__counter}")
              self.__counter += 1
              self.condition.notify()

    def even_print(self):
        while self.__counter < self.__limit:
            with self.condition:
               while self.__counter %2 == 1:
                  self.condition.wait()

               print(f"sequence {threading.current_thread().name} ={self.__counter}")
               self.__counter += 1
               self.condition.notify()

p = PrintSequence(10)
t1 = threading.Thread(target=p.odd_print,name="oddThread")
t2 = threading.Thread(target=p.even_print,name="evenThread")
t1.start()
t2.start()
