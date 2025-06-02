from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDetailView, SubscriptionCancelView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
    path('<int:pk>/cancel/', SubscriptionCancelView.as_view(), name='subscription-cancel'),
]
