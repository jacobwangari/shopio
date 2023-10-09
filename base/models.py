from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
       
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile):
        return self._create_user(email, password, first_name, last_name, mobile)


# Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','first_name','last_name','mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.email

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ProductCategory"
        


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    units = models.CharField(max_length=10,default = "units")
    stock = models.IntegerField()
    purchase_price = models.FloatField()
    selling_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "Parties"


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.expense

    class Meta:
        db_table = "Expense"