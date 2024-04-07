from django.db import models

class Kit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    likes = models.PositiveIntegerField()
    # Relación ManyToManyField con Product
    products = models.ManyToManyField('Product', related_name='kits', blank=True)
    # Atributos para imágenes
    # images = models.ManyToManyField('img', related_name='kits', blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    likes = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    # Atributos para imágenes
    # images = models.ManyToManyField('ProductImage', related_name='products', blank=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='inventory/product/images')
    
class KitImage(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='inventory/kit/images')