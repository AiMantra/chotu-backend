from .models import *
from rest_framework import serializers
from .models import User, OTP


class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = "__all__"

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = "__all__"
class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProduct
        fields = "__all__"        


class Vendor_Product_PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_Product_Price
        fields = "__all__"        

                


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class AllCustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "phone_number"]


class ServicesSerializer(serializers.ModelSerializer):

    society_name = serializers.CharField(
        source="society.name", read_only=True, default=None
    )

    class Meta:
        model = Services
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class AllCouponDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ["id", "discount_type", "code"]


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
    


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"        


class ProductByProductSerializer(serializers.ModelSerializer):
    product_images_product = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class DeliveryAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgent
        fields = "__all__"


class PincodeServiceabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PincodeServiceability
        fields = "__all__"


class LiveOrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveOrderTracking
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSupport
        fields = "__all__"


class ReturnSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnSystem
        fields = "__all__"


class ProductCoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCoins
        fields = "__all__"


class VoiceOrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceOrderRequest
        fields = "__all__"


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = "__all__"  

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"        


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"  



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"    


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"     

class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    role = serializers.ChoiceField(choices=[("vendor", "Vendor"), ("customer", "Customer"), ("agent", "Vendor Agent")])

class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"        