from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ProductCategory, Product, Parties,ExpenseCategory,Expense,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'mobile')
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id':representation['id'],
            'email': representation['email'],
            # 'password': representation['password'],
            'first_name': representation['first_name'],
            'last_name': representation['last_name'],
            'mobile': representation['mobile'],
        }

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


        