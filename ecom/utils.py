from enum import Enum

class OrderTypeEnum(Enum):
    
    PREPLCED="pre_placed"
    Instant="instant"
    InstantOrder="instantorder"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class DiscountTypeEnum(Enum):
    
    Fixed = "fixed"
    Percentage = "percentage"
    FirstOrder = "firstorder"
    CategoryDiscout = "categorydiscount"
    ReferralDiscount = "referraldiscount"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class UserGenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class TypeEnum(Enum):
    contactus ="contact us"
    query="query"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
