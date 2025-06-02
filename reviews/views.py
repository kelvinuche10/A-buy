from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

class UserReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        recipient_id = self.kwargs['user_id']
        return Review.objects.filter(recipient_id=recipient_id)
