from django.urls import path
from .views import UserView

urlpatterns = [
    path('api/login/', UserView.as_view(), name='login'),
]