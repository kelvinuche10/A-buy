from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from django.core.exceptions import PermissionDenied
from products.models import Product
from rest_framework.exceptions import ValidationError

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        if product.stock < quantity:
            raise ValidationError("Insufficient stock available.")

        total_price = product.price * quantity
        serializer.save(buyer=self.request.user, total_price=total_price)

        # Decrease stock
        product.stock -= quantity
        product.save()

class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.buyer:
            raise PermissionDenied("You are not allowed to update this order.")
        serializer.save()
