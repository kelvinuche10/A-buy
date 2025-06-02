from django.urls import path
from .views import AdminDashboardView
from .views import (
    ProductListCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView, 
    SubCategoryListView
)

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
]

