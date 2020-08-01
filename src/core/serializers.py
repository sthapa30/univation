from rest_framework import serializers

from .models import Car

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id','name','brand','year'
        )