from datetime import  datetime, timedelta
from typing import  List,Dict


class CouponType:
    PERCENTAGE = "PERCENTAGE"
    FIXED = "FIXED"
class Coupon:
    def __init__(self,coupon_code: str,
                 coupon_type: str,
                 start: datetime,
                 end: datetime,
                 value: float,
                 min_order_value: float,
                 max_uses: int,
                 redemption_per_user: int):
        self.coupon_code = coupon_code
        self.coupon_type = coupon_type
        self.start = start
        self.end = end
        self.value = value
        self.min_order_value = min_order_value
        self.max_uses = max_uses
        self.redemption_per_user = redemption_per_user

    user_redemption_lookup = Dict[str,int]
    total_redemption = 0

    def is_valid(self,user_id : str,order_value: float) ->(bool,str):

        now = datetime.now()

        if now < self.start or now > self.end:
            return False, "Coupon expired or not yet active"

        if order_value < self.min_order_value:
            return False, f"Order value must be greater than {self.min_order_value}"

        if self.total_redemption >=  self.max_uses:
            return False, f"Coupon redemption limit exceeded! {self.total_redemption}"

        if user_id in self.redemption_per_user and  self.redemption_per_user[user_id] >= self.redemption_per_user :
            return False, f"Coupon redemption per user limit exceeded! {self.redemption_per_user}"

        return True, "Coupon is Valid"


    def apply(self, user_id:str, order_value: float)->(float, str):
        pass


