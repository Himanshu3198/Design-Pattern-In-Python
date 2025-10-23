from  dataclasses  import dataclass,field

@dataclass
class Account:
    card_number: str
    account_holder: str
    card_pin: int
    mobile_numer: str
    account_type : str
    account_balance: float


