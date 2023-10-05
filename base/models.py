from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ProductCategory"
        


class Product(models.Model):
    product_code = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    units = models.CharField(max_length=10,default = "units")
    stock = models.IntegerField()
    purchase_price = models.FloatField()
    selling_price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"


class Parties(models.Model):
    ROLE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
    )

    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Parties"


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "ExpenseCategory"


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    expense = models.CharField(max_length=25)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    note = models.CharField(max_length=25)



    def __str__(self):
        return self.expense

    class Meta:
        db_table = "Expense"