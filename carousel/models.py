from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Carousel(models.Model):
    # Definición de campos y métodos del modelo

    class Meta:
        db_table = 'carousel' 
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='carousel/images', null=True, blank=True , validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    image_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)