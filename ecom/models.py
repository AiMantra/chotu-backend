
from django.db import models
import uuid
from .utils import *
from datetime import datetime
from django.utils.timezone import now 
import random
from django.utils import timezone



class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    phone_number = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    #role = models.CharField(max_length=10, choices=User_Roles)
    created_at = models.DateTimeField(auto_now_add=True)
    user_roles = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=User_RolesStatusEnum.choices(),
        default="customer"
    )
    def __str__(self):
        return str(self.id)

   
class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self, otp):
        return self.otp_code == otp and timezone.now() < self.expires_at
     
    @staticmethod
    def generate_otp(user):
        code = str(random.randint(100000, 999999))
        return OTP.objects.create(
            user=user,
            otp_code=code,
            expires_at=timezone.now() + timezone.timedelta(minutes=5)
        )



class Society(models.Model):  # done
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    # company_logo = models.ImageField(
    #     upload_to="subcompanys_logo", blank=True, null=True
    # )

    def __str__(self):
        return str(self.id)


 # Vendor class for reference (already provided)
class Vendors(models.Model):       
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=250, blank=True,null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    alt_contact_number = models.CharField(max_length=15, null=True, blank=True)
    gstin_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)
    registration_certificate = models.FileField(
        upload_to="vendors", null=True, blank=True
    )
    latitude = models.FloatField(null=True, blank=True) # Geo-coordinates for delivery radius and mapping
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    store_type = models.CharField(max_length=50, null=True, blank=True)
    license = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to="vendor_logos/", blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    total_orders = models.IntegerField(default=0)
    approval=models.CharField(max_length=50,null=True,blank=True,choices=VendorApprovalStatusEnum.choices(),default="pending"),

    def __str__(self):
        return str(self.id)


# Bank details Of Vendors
class BankDetails(models.Model): 
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    vendor = models.ForeignKey(
        Vendors, on_delete=models.CASCADE, related_name="bank_details"
    )
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    ifsc_code = models.CharField(max_length=15, null=True, blank=True)
    account_holder_name = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   

    def __str__(self):
        return str(self.id)

# Product Of Vendors

class VendorProduct(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    vendor = models.ForeignKey(
        Vendors,
        on_delete=models.CASCADE,
        related_name="vendors_detail",
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="product_vendor",
        null=True,
        blank=True,
    )
    stock = models.IntegerField(default=0)
    unit = models.CharField(max_length=50, null=True, blank=True)
    vendor_sku = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
    

# Product Of Vendor_Product_Price


class Vendor_Product_Price(models.Model):   
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    product = models.ForeignKey(
        VendorProduct, on_delete=models.CASCADE, related_name="vendors_product"
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gst = models.CharField(max_length=50, null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)




 # Customer model to store basic details of the customer



class Customer(models.Model):      
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    coupon = models.ForeignKey(
        "Coupon",
        on_delete=models.CASCADE,
        related_name="customer_coupon",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    alternate_phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=UserGenderEnum.choices()
    )
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(
        upload_to="customers/profile/", null=True, blank=True
    )
    def __str__(self):
        return str(self.id)
    


    
 # ***********************ContactForm*******************************

class ContactForm(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    form_type = models.CharField(
        max_length=20, null=True, blank=True, choices=ContactFormTypeEnum.choices()
    )
    reply_remark = models.CharField(max_length=100, null=True, blank=True)
    reply_date = models.DateField(null=True, blank=True)
    reply_by = models.CharField(max_length=50, null=True, blank=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    

 # ***********************Address*******************************

class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    vendors = models.ForeignKey(
        "Vendors",
        on_delete=models.CASCADE,
        related_name="vendor_address",
        null=True,
        blank=True,
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        related_name="customer_address",   
        null=True,
        blank=True,
    )
    deliveryagent = models.ForeignKey(
        "DeliveryAgent",
        on_delete=models.CASCADE,
        related_name="deliveryagent_address",
        null=True,
        blank=True,
    )
    block_no = models.CharField(max_length=20, null=True, blank=True)
    house_flat_no = models.CharField(max_length=20, null=True, blank=True)
    house_floor_no = models.CharField(max_length=101, null=True, blank=True)
    street = models.CharField(max_length=150, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    address_type = models.CharField(max_length=20,null=True, blank=True)
    is_default = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.id)


# Services for grocery and food(types of services that we are provoding)


class Services(models.Model):      
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="services/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    society = models.ForeignKey(
        Society,
        on_delete=models.CASCADE,
        related_name="services_society",
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return str(self.id)





  # Categories for item inside Services
class Category(models.Model):        
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False )
    name = models.CharField(max_length=100, null=True, blank=True)
    coupon = models.ForeignKey("Coupon",on_delete=models.CASCADE,related_name="category_coupon",null=True,blank=True, )
    details = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="category", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)


# SubCategories for item inside Services

class SubCategory(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="subcategory/images", null=True, blank=True)
    is_active = models.BooleanField(default=True)  # soft enable/disable
    highlight = models.BooleanField(default=False)  # show on homepage/high priority
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    


 # ***********************Product*******************************

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    product_description = models.CharField(max_length=250, null=True, blank=True)
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name="vendors", null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category_product",null=True,blank=True,)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory_products', null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True, null=True)  # "organic,imported,new"
    is_featured = models.BooleanField(default=False)  # show on homepage/highlighted
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
    )
    discount = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id)


 # ***********************ProductVariant*******************************

class ProductVariant(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    product = models.ForeignKey( Product, on_delete=models.CASCADE, related_name="variants" )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  # in kg
    unit = models.CharField(max_length=50, null=True, blank=True)  # e.g., "kg", "ltr", "pcs"
    image = models.ImageField(upload_to="variants/", null=True, blank=True)  # optional thumbnail for this variant
    attributes = models.JSONField(null=True, blank=True)  # to hold size, color etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    


 # ************************************************ProductImage************************************************************


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name="product_images",)
    productvariant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,null=True,blank=True,related_name="productvariant_images",)
    vendorproduct = models.ForeignKey(VendorProduct,on_delete=models.CASCADE,null=True,blank=True,related_name="vendorproduct_images",)
    image = models.ImageField(upload_to="productimage", blank=True, null=True)
    def __str__(self):
        return str(self.id)

# ********************************************Inventory********************************************************************

class Inventory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE,related_name="inventory_items")  # Ensure Product model exists
    stock = models.IntegerField(default=0)
    current_stock = models.PositiveIntegerField(default=0)  # Remaining unsold stock
    low_stock_threshold = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    batch_no = models.CharField(max_length=100, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    warehouse_location = models.CharField(max_length=255, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)



#********************************CART*********************************

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name="carts" )
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="carts")
    is_active = models.BooleanField(default=True)  # helps retain past carts or abandoned ones
    Coupon = models.ForeignKey(
        "Coupon",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="applied_carts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return (self.id) 
        
#********************************CARTITEM*********************************
        
class CartItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="cart_items")
    variant = models.ForeignKey("ProductVariant", on_delete=models.SET_NULL, null=True, blank=True, related_name="cart_items")
    vendor = models.ForeignKey("Vendors", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    cart_total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return (self.id)
    


#Orders with types (pre-placed and instant)
class Order(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    order_type = models.CharField(
        max_length=20, choices=OrderTypeEnum.choices(), null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)



 # Order Items
class OrderItem(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id) 
    


#******************Discount and Coupon *************************

class Coupon(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    vendor = models.ForeignKey(
        Vendors,
        on_delete=models.CASCADE,
        related_name="vendors_coupon",
        null=True,
        blank=True,
    )
    discount_type = models.CharField(
        max_length=20, choices=DiscountTypeEnum.choices(), null=True, blank=True
    )
    discount_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    min_order_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Minimum order value required to apply the coupon.",
    )
    max_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Maximum discount allowed for percentage-based coupons.",
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)
    usage_limit = models.PositiveIntegerField(
        default=1, help_text="Total number of times this coupon can be used."
    )
    used_count = models.PositiveIntegerField(
        default=0, help_text="Number of times the coupon has been used."
    )
    is_active = models.BooleanField(default=True)

    def is_valid(self):
        """
        Checks if the coupon is still valid (within the date range and usage limit).
        """
       

        return (
            self.is_active
            and (self.valid_from <= now() <= self.valid_to)
            and (self.used_count < self.usage_limit)
        )

    def __str__(self):
        return str(self.id) 


#********************************Payment*********************************

class Payment(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="payments", null=True, blank=True)
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, related_name="payments", null=True, blank=True)
    wallet = models.ForeignKey("Wallet", on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")  #link to Wallet
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=PayStatusEnum.choices(),
        default=PayStatusEnum.PENDING.value
    )

    method = models.CharField(
        max_length=20,
        choices=PayMethodEnum.choices(),
        default=PayMethodEnum.CARD.value
    )
   
    payment_gateway = models.CharField(
        max_length=50, null=True, blank=True
    )  # e.g., Razorpay
    transaction_id = models.CharField(max_length=100, null=True, blank=True)  # Payment gateway ID
    gateway_response = models.JSONField(null=True, blank=True)  # Full response for debugging or audit
    is_refunded = models.BooleanField(default=False)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    initiated_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)  # When payment was made

    def __str__(self):
        return str(self.id)

#********************************Wallet*********************************


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.OneToOneField("Customer", on_delete=models.CASCADE, related_name="wallet")
    balance = models.PositiveIntegerField(default=0)  # Only coins
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    



#  Ledger for user transactions Tracks all financial transactions affecting a customer's balance
class Ledger(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="ledger", null=True, blank=True
    )
    order = models.ForeignKey(
        Order,on_delete=models.CASCADE,
        related_name="ledger_entries",
        null=True,
        blank=True,
    )
    transaction_type = models.CharField(
        max_length=50,
        choices=LedgerStatusEnum.choices(),default="pending",)
    reference_id = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Reference ID from payment gateway or other sources."
    )
    debit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )  # Amount deducted
    credit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )  # Amount added
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )  # Remaining balance
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)







#***************************************Delivery***********************************



class Delivery(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_time_slot = models.CharField(max_length=50, null=True, blank=True)
    delivery_status = models.CharField(
        max_length=30,
        choices=DeliveryStatusEnum.choices(),
        default="pending",
        null=True,
        blank=True
)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    payment_status = models.CharField(
    max_length=30,
    choices=DeliveryPaymentStatusEnum.choices(),
    default=DeliveryPaymentStatusEnum.PENDING.value,
    null=True,
    blank=True
)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    

#********************************DeliveryAgent*********************************

class DeliveryAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    assigned_pincode = models.CharField(max_length=10, null=True, blank=True)
    current_location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_location_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return str(self.id)


#********************************PincodeServiceability*********************************
class PincodeServiceability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    pincode = models.CharField(max_length=10)
    warehouse_id = models.UUIDField()  # Assuming warehouse is referenced by UUID
    is_active = models.BooleanField(default=True)
    delivery_charges = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    eta_minutes = models.PositiveIntegerField(help_text="Estimated time of arrival in minutes")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
#********************************LiveOrderTracking*********************************
class LiveOrderTracking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    order_id = models.UUIDField()  # Assuming orders are identified by UUID
    lat = models.DecimalField(max_digits=9, decimal_places=6)   # Latitude (e.g. 12.345678)
    lng = models.DecimalField(max_digits=9, decimal_places=6)   # Longitude (e.g. 98.765432)
    timestamp = models.DateTimeField(auto_now_add=True)
    eta = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)  # e.g., "en route", "delivered"

    def __str__(self):
        return str(self.id)

 



#*************************************Rating**********************************************



class Rating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    vendors = models.ForeignKey( Vendors, on_delete=models.CASCADE, related_name="ratings" )
    product = models.ForeignKey( Product, on_delete=models.CASCADE, related_name="ratings" )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField(null=True, blank=True)  # e.g., 1 to 5
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
 
#*************************************Review**********************************************

class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="reviews"
    )
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)



#*************************************CustomerSupport**********************************************

class CustomerSupport(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    
    customer_name = models.CharField(max_length=150, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)
    
    support_type = models.CharField(
        max_length=20,
        choices=SupportTypeEnum.choices(),
        null=True,
        blank=True
    )
    
    message = models.TextField(null=True, blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=SupportStatusEnum.choices(),
        default=SupportStatusEnum.OPEN,
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    resolution_remarks = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    

    

#*****************************************Return System*****************************************************


class ReturnSystem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    order_id = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=150, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)

    return_type = models.CharField(
        max_length=20,
        choices=ReturnTypeEnum.choices(),
        null=True,
        blank=True
    )

    return_reason = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=ReturnStatusEnum.choices(),
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    resolution_remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
    


 #******************ProductCoins**********************
  

class ProductCoins(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="coin_rewards"
    )

    coins = models.PositiveIntegerField(default=0, help_text="Coins/points earned on purchasing this product")
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id)


#******************VoiceOrder**********************

class VoiceOrderRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='voice_orders')
    audio_url = models.URLField(help_text="URL to the uploaded voice recording")
    transcription = models.TextField(blank=True, null=True)
    detected_intent = models.CharField(max_length=100, blank=True, null=True)
    products_requested = models.JSONField(blank=True, null=True, help_text="Parsed products from voice input")
    error_message = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)# Optional NLP/AI metadata
    confidence_score = models.FloatField(blank=True, null=True)
    ai_model_version = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=StatusEnum.choices(),default="pending",)

    def __str__(self):
        return str(self.id)   
    

#******************Referral**********************
    
class Referral(models.Model):
    referral = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='referrals')
    referral = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='referred_by')
    referral_code = models.CharField(max_length=20, unique=True)
    reward_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)   
    

