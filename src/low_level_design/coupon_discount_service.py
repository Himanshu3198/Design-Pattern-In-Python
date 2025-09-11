from datetime import datetime, timedelta
from typing import Dict


class CouponType:
    PERCENTAGE = "PERCENTAGE"
    FIXED = "FIXED"


class Coupon:
    def __init__(self, coupon_code: str,
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

        # Proper initializations
        self.user_redemption_lookup: Dict[str, int] = {}
        self.total_redemption = 0

    def is_valid(self, user_id: str, order_value: float) -> (bool, str):
        now = datetime.now()

        if now < self.start or now > self.end:
            return False, "Coupon expired or not yet active"

        if order_value < self.min_order_value:
            return False, f"Order value must be greater than {self.min_order_value}"

        if self.total_redemption >= self.max_uses:
            return False, "Coupon redemption limit exceeded!"

        user_redemptions = self.user_redemption_lookup.get(user_id, 0)
        if user_redemptions >= self.redemption_per_user:
            return False, "Coupon redemption per user limit exceeded!"

        return True, "Coupon is Valid"

    def apply(self, user_id: str, order_value: float) -> float:
        valid, msg = self.is_valid(user_id, order_value)
        if not valid:
            raise Exception(msg)

        # Calculate discount
        if self.coupon_type == CouponType.FIXED:
            discount = self.value
        elif self.coupon_type == CouponType.PERCENTAGE:
            discount = (order_value * self.value) / 100
        else:
            raise Exception("Unsupported Coupon!")

        discount = min(discount, order_value)  # no negative final price

        # Update counters
        self.total_redemption += 1
        self.user_redemption_lookup[user_id] = self.user_redemption_lookup.get(user_id, 0) + 1

        final_price = order_value - discount
        return final_price


# -----------------demo------------
if __name__ == "__main__":
    coupon = Coupon(
        coupon_code="summer123",
        coupon_type=CouponType.FIXED,
        start=datetime.now() - timedelta(days=1),
        end=datetime.now() + timedelta(days=3),
        value=20,
        min_order_value=200,
        max_uses=5,
        redemption_per_user=3
    )

    try:
        after_discount = coupon.apply("user123", 250.0)
        print(f"Final order value after discount is: {after_discount}")
    except Exception as e:
        print("Error:", e)
