from src.low_level_design.atm_design.account import Account
from src.low_level_design.atm_design.exceptions import InvalidCashException, InvalidPinGeneration
from src.low_level_design.atm_design.iaccount_service import IAccountService


class IAccountServiceImpl(IAccountService):
    def get_account_balance(self,account:Account)->float:
        print(f"Your account balance is {account.account_balance}")
        return account.account_balance

    def withdraw_cash(self, account:Account,withdraw_amount:float)->float:
        if account.account_balance is None or withdraw_amount > account.account_balance:
            raise InvalidCashException(f"Your account has insufficient balance: {account.account_balance}")
        account.account_balance -= withdraw_amount
        print(f"Amount has been debited from account:{account.account_holder}")
        return account.account_balance

    def credit_cash(self, account:Account,credit_amount:float)->float:
        account.account_balance += credit_amount
        return account.account_balance

    def change_pin(self, account:Account,new_pin:int)->None:
        new_pin_s = str(new_pin)
        if len(new_pin_s) != 4 or not new_pin_s.isnumeric():
            raise InvalidPinGeneration(f"Pin should be 4 digit numeric value")
        account.card_pin = new_pin
        print(f"Your pin has been changed to:{new_pin}")
