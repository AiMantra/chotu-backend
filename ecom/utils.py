from enum import Enum

class OrderTypeEnum(Enum):
    
    PREPLACED="pre_placed"
    Instant="instant"
    InstantOrder="instantorder"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class DiscountTypeEnum(Enum):
    
    Fixed = "fixed"
    Percentage = "percentage"
    FirstOrder = "firstorder"
    CategoryDiscount = "categorydiscount"  
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

class ContactFormTypeEnum(Enum):
    QUERY = "query"
    ISSUE = "issue"
    FEEDBACK = "feedback"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
        
class DeliveryStatusEnum(Enum):
    PENDING = "pending"
    PREPARING = "preparing"
    SHIPPED = "shipped"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    UNDELIVERED = "undelivered"
    RETURNED = "returned"
    CANCELLED = "cancelled"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class DeliveryPaymentStatusEnum(Enum):
    PENDING = "pending"
    PAID = "paid"
    COD = "cod"
    FAILED = "failed"
    REFUNDED = "refunded"
    PARTIALLY_REFUNDED = "partially_refunded"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class statusEnum(Enum):
    Pending="pending"
    Success="succees"
    Failed="failed"
    Refunded="refunded"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    

class SupportTypeEnum(Enum):
    QUERY = "query"
    ISSUE = "issue"
    FEEDBACK = "feedback"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class SupportStatusEnum(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class ReturnTypeEnum(Enum):
    REFUND = "refund"
    EXCHANGE = "exchange"
  

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
class ReturnStatusEnum(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    

# ***********payment***********

class PayStatusEnum(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    CANCELLED = "CANCELLED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class PayMethodEnum(Enum):
    CARD = "CARD"
    UPI = "UPI"
    NETBANKING = "NETBANKING"
    COD = "COD"
    WALLET = "WALLET"
    OTHER = "OTHER"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    
class StatusEnum(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]  

class LedgerStatusEnum(Enum):
    PAYMENT= "Payment Received"
    REFUND= "Refund Issued"
    ADJUSTMENT= "Adjustment"
    CHARGE= "Charge" 

    @classmethod
    def choices(cls):
        return[(key.value,key.name)for key in cls]
    
class VendorApprovalStatusEnum(Enum):
    PENDING="pending"
    APPROVED="approved"
    REJECTED="rejected"

    @classmethod
    def choices(cls):
        return[(key.value,key.name)for key in cls]


class User_RolesStatusEnum(Enum):
    VENDOR = "vendor"
    CUSTOMER = "customer"
    AGENT = "agent"

    @classmethod
    def choices(cls):
         return [(key.value, key.value.capitalize()) for key in cls]

     