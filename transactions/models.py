from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('product', 'Product'),
        ('gig', 'Gig'),
        ('subscription', 'Subscription'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    reference_id = models.CharField(max_length=100)  # ID of product/gig/subscription
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} by {self.user.username}"
