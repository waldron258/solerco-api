from rest_framework.routers import DefaultRouter
from carousel.viewsets import CarouselViewSet

router = DefaultRouter()
router.register(r'carousel', CarouselViewSet)

urlpatterns = router.urls

