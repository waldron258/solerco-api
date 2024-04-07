from rest_framework import serializers
from .models import Product, Kit, ProductImage, KitImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')
        
class KitImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitImage
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'specs', 'likes', 'category', 'images','image_files')
        
    def create(self, validated_data):
        image_files=validated_data.pop('image_files')
        product = Product.objects.create(**validated_data)
        for image in image_files:
            ProductImage.objects.create(image=image, product=product)
    
        product.save()
        return product        

class KitSerializer(serializers.ModelSerializer):
    images = KitImageSerializer(many=True, read_only=True)

    class Meta:
        model = Kit
        fields = ('id', 'name', 'description', 'price', 'specs', 'likes', 'products', 'images', 'images_url')
        
    def create(self, validated_data):
        image_files=validated_data.pop('image_files')
        kit = Product.objects.create(**validated_data)
        for image in image_files:
            ProductImage.objects.create(image=image, kit=kit)
    
        kit.save()
        return kit