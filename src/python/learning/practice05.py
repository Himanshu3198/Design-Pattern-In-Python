class Account:
    def __init__(self,balance):
          self.__balance = balance


    def deposit_balance(self,amount):
         self.__balance += amount
         print("Amount deposit total balance",self.__balance)

    def withdraw_balance(self,w_amount):
        if w_amount > self.__balance:
            print("Insufficient amount",self.__balance)
            return
        self.__balance -= w_amount
        print("Withdraw complete curr balance",self.__balance)

    def get_balance(self):
        print("your current balance",self.__balance)



a=Account(1000)
a.get_balance()
a.deposit_balance(500)
a.get_balance()
a.withdraw_balance(12000)
a.withdraw_balance(500)