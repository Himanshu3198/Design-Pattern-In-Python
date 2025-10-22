from typing import Dict
from src.low_level_design.atm_design.account import Account

data : Dict[str,Account] = {"ABC123": Account("ABC123", "HS", 1234, 972524, "Saving",),
                                "CDE123": Account("CDE123", "RS", 4567, 243242, "Saving")}



def findByCardNumber(card_number : str) :
    if  card_number not in data:
        print("Invalid CardNumber or CardDetail not found")
        return None
    return data[card_number]