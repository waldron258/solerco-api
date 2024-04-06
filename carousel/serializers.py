from rest_framework import serializers
from .models import Carousel


class CarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carousel
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']