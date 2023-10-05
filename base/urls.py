from django.urls import path
from django.urls import path
from .views import (
    ProductCategoryListView,
    ProductCategoryDetailView,
    ProductListView,
    ProductDetailView,
    PartiesListView,
    PartiesDetailView,
    ExpenseCategoryListView,
    ExpenseCategoryDetailView,
    ExpenseListView,
    ExpenseDetailView,
)




urlpatterns = [
    path('product-categories/', ProductCategoryListView.as_view(), name='product-category-list-create'),
    path('product-categories/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('products/', ProductListView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('parties/', PartiesListView.as_view(), name='parties-list-create'),
    path('parties/<int:pk>/', PartiesDetailView.as_view(), name='parties-detail'),
    path('expense-categories/', ExpenseCategoryListView.as_view(), name='expense-category-list-create'),
    path('expense-categories/<int:pk>/', ExpenseCategoryDetailView.as_view(), name='expense-category-detail'),
    path('expenses/', ExpenseListView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
]