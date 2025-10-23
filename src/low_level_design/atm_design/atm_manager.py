from src.low_level_design.atm_design.account_repository import AccountRepository
from src.low_level_design.atm_design.iaccount_service import IAccountService
from src.low_level_design.atm_design.iaccount_service_impl import IAccountServiceImpl


class AtmManager:
    def __init__(self, card_number: str):
        self.card_number = card_number
        self.account_repository = AccountRepository()
        self.account_service = IAccountServiceImpl()

    def display_menu(self)->None:
        print("\n=== Please Select Option ===")
        print("1. Withdraw Cash")
        print("2. Check Account Balance")
        print("3. Change PIN")
        print("4. Deposit Cash")
        print("5. Exit")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                pin = input("Please enter your PIN: ").strip()
                account = self.account_repository.find_by_card_number(self.card_number)

                if int(pin) != account.card_pin:
                    print("Invalid PIN. Transaction aborted.")
                    continue

                try:
                    withdraw_amount = int(input("Please enter amount to withdraw: "))
                    account = self.account_repository.find_by_card_number(self.card_number)
                    current_balance = self.account_service.withdraw_cash(account,withdraw_amount)
                    print(f"Your current balance is: {current_balance}")
                except ValueError:
                    print("Invalid amount entered.")
                    continue

            elif choice == "2":
                account = self.account_repository.find_by_card_number(self.card_number)
                balance = self.account_service.get_account_balance(account)
                print(f"Account balance is:{balance}")

            elif choice == "3":
                try:
                    new_pin = int(input("Please enter new PIN: ").strip())
                    account = self.account_repository.find_by_card_number(self.card_number)
                    print(f"New pin is : {self.account_service.change_pin(account,new_pin)}")
                    self.account_service.change_pin(account, new_pin)
                except ValueError:
                    print(" Invalid PIN entered.")

            elif choice == "4":
                try:
                    deposit_amount = float(input("Please enter amount to deposit"))
                    account = self.account_repository.find_by_card_number(self.card_number)
                    latest_balance = self.account_service.credit_cash(account,deposit_amount)
                    print(f"Amount has been credited! your latest balance:{latest_balance}")
                except Exception as e:
                    print(e)
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
