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

# Client model to store basic details of the client
class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Categories for grocery and food
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Products under categories
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Orders with types (pre-placed and instant)
class Order(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
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
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ledger")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ledger_entries", null=True, blank=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Amount deducted
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Amount added
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Remaining balance
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ledger Entry {self.id} for Client {self.client.name}"



