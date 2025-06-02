from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    REPORT_TYPES = [
        ('product', 'Product'),
        ('user', 'User'),
        ('gig', 'Gig'),
        ('order', 'Order'),
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=10, choices=REPORT_TYPES)
    object_id = models.PositiveIntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} - {self.object_id}"

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
