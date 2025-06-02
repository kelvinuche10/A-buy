from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer} for {self.recipient} - {self.rating}★"
