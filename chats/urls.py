from django.urls import path
from .views import MessageListCreateView

urlpatterns = [
    path('<int:user_id>/', MessageListCreateView.as_view(), name='message-thread'),
]
