# product/models.py
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    images = models.JSONField(default=list)  # Store Cloudinary URLs as list
    video = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title
