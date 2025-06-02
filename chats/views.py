from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        other_user_id = self.kwargs['user_id']
        return Message.objects.filter(
            sender=user, receiver_id=other_user_id
        ) | Message.objects.filter(
            sender_id=other_user_id, receiver=user
        ).order_by('timestamp')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
