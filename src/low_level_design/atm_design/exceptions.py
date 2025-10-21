class InvalidCashException(Exception):
    """Raised when an account has insufficient balance"""
    def __init__(self,message):
        super().__init__(message)


class InvalidPinGeneration(Exception):
    """Raised when creating invalid pin"""
    def __init__(self,message):
        super().__init__(message)