from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from products.models import Product
from orders.models import Order
from gigs.models import Gig
from transactions.models import Transaction
from products.serializers import ProductSerializer

from rest_framework import generics, permissions, filters
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework.backends import DjangoFilterBackend

from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer

User = get_user_model()

# 🔄 List all products or add a product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['subcategory', 'price']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# 📄 Get product details
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


# ✏️ Update a product (owner only)
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.seller:
            raise PermissionDenied("You can't edit this product.")
        serializer.save()


# ❌ Delete a product (owner only)
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.seller:
            raise PermissionDenied("You can't delete this product.")
        instance.delete()


# 📂 List all categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 🗂️ List all subcategories
class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.count()
        total_products = Product.objects.count()
        total_orders = Order.objects.count()
        total_gigs = Gig.objects.count()
        total_revenue = Transaction.objects.aggregate(total=Sum('amount'))['total'] or 0

        # Top 5 selling products by number of orders
        top_products = Product.objects.annotate(order_count=Count('order')).order_by('-order_count')[:5]
        top_products_data = ProductSerializer(top_products, many=True).data

        data = {
            "total_users": total_users,
            "total_products": total_products,
            "total_orders": total_orders,
            "total_gigs": total_gigs,
            "total_revenue": total_revenue,
            "top_selling_products": top_products_data,
        }
        return Response(data)
