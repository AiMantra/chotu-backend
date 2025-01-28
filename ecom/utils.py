from enum import Enum

class OrderTypeEnum(Enum):
    
    PREPLCED="pre_placed"
    Instant="instant"
    InstantOrder="instantorder"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]