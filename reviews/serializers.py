from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.username')

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['reviewer', 'created_at']
