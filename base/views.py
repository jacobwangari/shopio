from rest_framework import generics
from .models import Category, Product, Parties
from .serializers import CategorySerializer, ProductSerializer, PartiesSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PartiesListCreateView(generics.ListCreateAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer

class PartiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer
