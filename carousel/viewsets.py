from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from carousel.models import Carousel

from carousel.serializers import CarouselSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [AllowAny]