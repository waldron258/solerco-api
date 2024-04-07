from rest_framework import viewsets, pagination
from rest_framework.permissions import AllowAny
from carousel.models import Carousel

from carousel.serializers import CarouselSerializer

class CarouselPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    pagination_class = CarouselPagination
    permission_classes = [AllowAny]