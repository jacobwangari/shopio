from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<str:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('parties/', views.PartiesListCreateView.as_view(), name='parties-list-create'),
    path('parties/<int:pk>/', views.PartiesDetailView.as_view(), name='parties-detail'),
]


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<str:name>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<str:product_code>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('parties/', views.PartiesListView.as_view(), name='parties-list'),
    path('parties/<int:pk>/', views.PartiesDetailView.as_view(), name='parties-detail'),
]