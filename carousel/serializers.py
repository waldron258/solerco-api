from rest_framework import serializers
from .models import Carousel


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id', 'title', 'description', 'image', 'image_url', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        carousel = Carousel.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            image=validated_data.get('image')
        )
        carousel.image_url = carousel.image.url
        carousel.save()
        return carousel