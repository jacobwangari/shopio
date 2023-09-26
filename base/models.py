from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name
        


class Product(models.Model):
    product_code = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"




class Parties(models.Model):
    ROLE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Parties"
