from rest_framework import generics
from django.urls import path
from .models import ProductCategory, Product, Parties, ExpenseCategory, Expense
from .serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    PartiesSerializer,
    ExpenseCategorySerializer,
    ExpenseSerializer,
)

class ProductCategoryListView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PartiesListView(generics.ListCreateAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer

class PartiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer

class ExpenseCategoryListView(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseListView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer