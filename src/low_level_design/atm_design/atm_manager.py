from src.low_level_design.atm_design import account_repository


class AtmManager:
    def __init__(self, card_number: str):
        self.card_number = card_number
        self.account = account_repository.findByCardNumber(card_number)

    def display_menu(self)->None:
        print("\n=== Please Select Option ===")
        print("1. Withdraw Cash")
        print("2. Check Account Balance")
        print("3. Change PIN")
        print("4. Exit")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                pin = input("Please enter your PIN: ").strip()
                if int(pin) != self.account.card_pin:
                    print("Invalid PIN. Transaction aborted.")
                    continue

                try:
                    withdraw_amount = int(input("Please enter amount to withdraw: "))
                    self.account.withdraw_cash(withdraw_amount)
                except ValueError:
                    print("Invalid amount entered.")
                    continue

            elif choice == "2":
                self.account.get_account_balance()

            elif choice == "3":
                try:
                    new_pin = int(input("Please enter new PIN: ").strip())
                    self.account.change_pin(new_pin)
                    print("PIN changed successfully.")
                except ValueError:
                    print(" Invalid PIN entered.")

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
