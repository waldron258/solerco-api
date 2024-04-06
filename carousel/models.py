from django.db import models

class Carousel(models.Model):
    # Definición de campos y métodos del modelo

    class Meta:
        db_table = 'carousel' 
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='images/carousel', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)