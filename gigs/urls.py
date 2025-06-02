from django.urls import path
from .views import (
    GigListCreateView, GigDetailView,
    GigUpdateView, GigDeleteView
)

urlpatterns = [
    path('', GigListCreateView.as_view(), name='gig-list-create'),
    path('<int:pk>/', GigDetailView.as_view(), name='gig-detail'),
    path('<int:pk>/edit/', GigUpdateView.as_view(), name='gig-update'),
    path('<int:pk>/delete/', GigDeleteView.as_view(), name='gig-delete'),
]
