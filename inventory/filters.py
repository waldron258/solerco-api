from django_filters import rest_framework as filters
from .models import Product

class CaseInsensitiveSearchFilter(filters.CharFilter):
    def filter_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
            return queryset
        return queryset

    class Meta:
        model = Product
        fields = ['name']