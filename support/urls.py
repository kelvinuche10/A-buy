from django.urls import path
from .views import ReportCreateView, SupportTicketCreateView, SupportTicketListView

urlpatterns = [
    path('report/', ReportCreateView.as_view(), name='create-report'),
    path('ticket/', SupportTicketCreateView.as_view(), name='create-ticket'),
    path('ticket/all/', SupportTicketListView.as_view(), name='all-tickets'),  # Admin only
]
