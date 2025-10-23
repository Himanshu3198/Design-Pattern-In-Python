from typing import Dict
from src.low_level_design.atm_design.account import Account

class AccountRepository:
    def __init__(self):
        self.data: Dict[str, Account] = {
            "ABC123": Account("ABC123", "HS", 1234, "972524", "Saving",1200.0),
            "CDE123": Account("CDE123", "RS", 4567, "243242", "Saving",1340.0)
        }

    def find_by_card_number(self, card_number: str):
        if card_number not in self.data:
            print("Invalid CardNumber or CardDetail not found")
            return None
        return self.data[card_number]
