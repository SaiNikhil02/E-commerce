from enum import Enum

class userType(Enum):
    CUSTOMER = 'Customer'
    MERCHANT = 'Merchant'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]
    