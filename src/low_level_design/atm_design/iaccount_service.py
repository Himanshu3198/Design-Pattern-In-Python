from abc import abstractmethod

from src.low_level_design.atm_design.account import Account


class IAccountService:

    @abstractmethod
    def withdraw_cash(self, account:Account,amount:float): pass

    @abstractmethod
    def get_account_balance(self,account:Account): pass

    @abstractmethod
    def credit_cash(self,account:Account,credit_amount:float): pass

    @abstractmethod
    def change_pin(self,account:Account, new_pin:int): pass
