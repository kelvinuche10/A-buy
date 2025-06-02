from django.urls import path
from .views import ReviewCreateView, UserReviewListView

urlpatterns = [
    path('', ReviewCreateView.as_view(), name='create-review'),
    path('user/<int:user_id>/', UserReviewListView.as_view(), name='user-reviews'),
]
