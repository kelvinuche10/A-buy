from rest_framework import generics, permissions
from .models import Gig
from .serializers import GigSerializer
from rest_framework.exceptions import PermissionDenied

class GigListCreateView(generics.ListCreateAPIView):
    queryset = Gig.objects.all().order_by('-created_at')
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class GigDetailView(generics.RetrieveAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    permission_classes = [permissions.AllowAny]

class GigUpdateView(generics.UpdateAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.seller:
            raise PermissionDenied("You can't edit this gig.")
        serializer.save()

class GigDeleteView(generics.DestroyAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.seller:
            raise PermissionDenied("You can't delete this gig.")
        instance.delete()
