from src.low_level_design.atm_design.exceptions import InvalidCashException, InvalidPinGeneration

class Account:

     def __init__ (self,card_number : str,account_holder : str, card_pin : int, mobile_number : int,account_type : str):
         self.card_number = card_number
         self.account_holder = account_holder
         self.card_pin = card_pin
         self.mobile_number = mobile_number
         self.account_type = account_type
         self.account_balance = 1000

     def get_account_balance(self):
          print(f"Your account balance is {self.account_balance}")

     def withdraw_cash(self,withdraw_amount):
         if withdraw_amount > self.account_balance :
             raise InvalidCashException(f"Your account has insufficient balance: {self.account_balance}")
         self.account_balance -= withdraw_amount
         print(f"Amount has been debited from account:{self.account_holder}")

     def  credit_cash(self,credit_amount):
          self.account_balance += credit_amount

     def change_pin(self,new_pin):
         if len(new_pin)!= 4 or not new_pin.isnumeric() :
             raise InvalidPinGeneration(f"Pin should be 4 digit numeric value")
         self.card_pin = new_pin