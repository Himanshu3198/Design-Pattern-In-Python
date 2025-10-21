from src.low_level_design.atm_design.account import Account


class AtmManager:
    def __init__(self,card_number : str):
        self.card_number = card_number
        self.account = account_repo.findByCardNumber(card_number)


   def display(self):
    print("=== Please Select Option as Mentioned ===")
    print("1. Withdraw Cash")
    print("2. Check Account Balance")
    print("3. Change PIN")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Please enter pin")
        pin = input()
        if pin != self.account.card_pin:
            print("Please enter valid pin")
        print("Please enter amount to Withdraw")
        withdraw_amount = input()
        self.account.withdraw_cash(withdraw_amount)

    elif choice == "2":
        self.account.check_balance()

    elif choice == "3":
        print("Please enter new pin")
        new_pin = input()
        self.account.change_pin(new_pin)

    else:
        print("Invalid option. Please try again.")

