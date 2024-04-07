from rest_framework.routers import DefaultRouter
from carousel.viewsets import CarouselViewSet
from inventory.views import ProductViewSet, KitViewSet

router = DefaultRouter()
router.register(r'carousel', CarouselViewSet)
router.register(r'product', ProductViewSet)
router.register(r'kit', KitViewSet)

urlpatterns = router.urls

