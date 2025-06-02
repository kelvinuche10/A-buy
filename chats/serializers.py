from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['sender', 'timestamp']
