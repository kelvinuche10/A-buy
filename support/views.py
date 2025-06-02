from rest_framework import generics, permissions
from .models import Report, SupportTicket
from .serializers import ReportSerializer, SupportTicketSerializer

class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

class SupportTicketCreateView(generics.CreateAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SupportTicketListView(generics.ListAPIView):
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return SupportTicket.objects.all().order_by('-created_at')
