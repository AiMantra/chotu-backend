from django.db import models
import uuid
from .utils import *
from datetime import datetime


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
    name = models.CharField(max_length=250, null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    alt_contact_number = models.CharField(max_length=15, null=True, blank=True)
    gstin_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)
    registration_certificate = models.FileField(
        upload_to="vendors", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ContactForm(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    form_type = models.CharField(
        max_length=20, null=True, blank=True, choices=TypeEnum.choices()
    )
    reply_remark = models.CharField(max_length=100, null=True, blank=True)
    reply_date = models.DateField(null=True, blank=True)
    reply_by = models.CharField(max_length=50, null=True, blank=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    block_no = models.CharField(max_length=10, null=True, blank=True)
    house_flat_no = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=150, null=True, blank=True)
    landmark = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)


# Customer model to store basic details of the customer
class Customer(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    alternate_phone_number = models.CharField(
        max_length=15, unique=True, null=True, blank=True
    )
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=UserGenderEnum.choices()
    )
    dob = models.DateField(null=True, blank=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="customer_address",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# Services for grocery and food
class Services(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
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
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    pic = models.ImageField(upload_to="category", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Coupon(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    discount_type = models.CharField(
        max_length=20, choices=DiscountTypeEnum.choices(), null=True, blank=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="customer_coupan",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category_coupan",
        null=True,
        blank=True,
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
        from django.utils.timezone import now

        return (
            self.is_active
            and (self.valid_from <= now() <= self.valid_to)
            and (self.used_count < self.usage_limit)
        )

    def __str__(self):
        return f"{self.code} - {self.discount_type} ({self.discount_value})"


class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=250, null=True, blank=True)
    product_description = models.CharField(max_length=250, null=True, blank=True)
    vendors = models.ForeignKey(
        Vendors, on_delete=models.CASCADE, related_name="vendors", null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category_product",
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)
    discount = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    gst = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ProductImage(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="product_images",
    )
    image = models.ImageField(upload_to="productimage", blank=True, null=True)

    def __str__(self):
        return str(self.id)


# Orders with types (pre-placed and instant)
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
        return f"Order {self.id} ({self.order_type})"


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
        return f"{self.product.name} (x{self.quantity})"


# Ledger for user transactions
class Ledger(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="ledger", null=True, blank=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="ledger_entries",
        null=True,
        blank=True,
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
        return f"Ledger Entry {self.id} for Customer {self.customer.name}"
