from django.db import models
import uuid
from .utils import*

# Vendor class for reference (already provided)
class Vendors(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    alt_contact_number = models.CharField(max_length=15, null=True, blank=True)
    gstin_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)
    registration_certificate = models.FileField(upload_to="vendors", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)

# Customer model to store basic details of the customer
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=UserGenderEnum.choices())   
    dob = models.DateField(null=True, blank=True)
    house_no = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=150,null=True,blank=True)
    landmark = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True) # ! not required in this project
    state = models.CharField(max_length=20, null=True, blank=True) # ! not required in this project
    pincode = models.IntegerField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Services for grocery and food
class Services(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Categories for item inside Services
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    code = models.CharField(max_length=50, unique=True, null=False, blank=False)
    discount_type =  models.CharField(max_length=20, choices = DiscountTypeEnum.choices(), null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_coupan")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="coupan")
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Minimum order value required to apply the coupon.")
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Maximum discount allowed for percentage-based coupons.")
    valid_from = models.DateTimeField(null=False, blank=False)
    valid_to = models.DateTimeField(null=False, blank=False)
    usage_limit = models.PositiveIntegerField(default=1, help_text="Total number of times this coupon can be used.")
    used_count = models.PositiveIntegerField(default=0, help_text="Number of times the coupon has been used.")
    is_active = models.BooleanField(default=True)

    def is_valid(self):
        """
        Checks if the coupon is still valid (within the date range and usage limit).
        """
        from django.utils.timezone import now
        return self.is_active and (self.valid_from <= now() <= self.valid_to) and (self.used_count < self.usage_limit)

    def __str__(self):
        return f"{self.code} - {self.discount_type} ({self.discount_value})"

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(default=0)
    discount = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name="orders")
    gst = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Orders with types (pre-placed and instant)
class Order(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_type = models.CharField(max_length=20, choices = OrderTypeEnum.choices(), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} ({self.order_type})"

# Order Items
class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

# Ledger for user transactions
class Ledger(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="ledger")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ledger_entries", null=True, blank=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Amount deducted
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Amount added
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Remaining balance
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ledger Entry {self.id} for Customer {self.customer.name}"



