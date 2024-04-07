from rest_framework import viewsets, permissions, pagination, filters
from .models import Product, Kit
from .serializers import ProductSerializer, KitSerializer
from .permissions import IsProductAdminOrAdmin
from django_filters.rest_framework import  DjangoFilterBackend
from django.db.models import Q

class InventoryPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = InventoryPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains", "startswith"],
        # "author__email": ["icontains", ],  # ForeignKey
        # "is_active": ["exact", ],  # BooleanField
        # "created_at": ["date__exact", ]  # DateTimeField
    }
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name and name != '':
            queryset = queryset.filter(Q(name__icontains=name))
        return queryset
    
    # def filter_queryset(self):
    #     queryset = Product.objects.all()
    #     q = self.request.query_params.get('q')
    #     if q is not None:
    #         queryset = queryset.filter(name=q)
    #     return queryset
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsProductAdminOrAdmin]
        return [permission() for permission in permission_classes]

class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
    pagination_class = InventoryPagination
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsProductAdminOrAdmin]
        return [permission() for permission in permission_classes]