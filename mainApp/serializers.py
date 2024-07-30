
from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product = super(ProductSerializer, self).to_representation(instance)
        images = Image.objects.filter(product_id=instance)
        images_serializer = ImageSerializer(images, many=True)

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'stock_quantity')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
