from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.models import Product, Service
from mainApp.serializers import ProductSerializer, AddProductSerializer, ServiceSerializer
from userApp.permissions import IsEmployee


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailsAPIView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductCreateView(APIView):
    permission_classes = [IsEmployee]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdateView(APIView):
    permission_classes = [IsEmployee]

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)

class ProductDeleteView(APIView):
    permission_classes = [IsEmployee]

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddProductView(APIView):
    permission_classes = [IsEmployee]

    def post(self, request):
        serializer = AddProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['id']
            quantity = serializer.validated_data['stock_quantity']

            try:
                product = Product.objects.get(pk=product_id)
            except:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            product.stock_quantity += quantity
            product.save()

            return Response({'message': 'Stock updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceListView(APIView):
    permission_classes = [IsEmployee]

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetailView(APIView):
    permission_classes = [IsEmployee]

    def get(self, request, pk):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

class ServiceCreateView(APIView):
    permission_classes = [IsEmployee]

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceUpdateView(APIView):
    permission_classes = [IsEmployee]

    def put(self, request, pk):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDeleteView(APIView):
    permission_classes = [IsEmployee]

    def delete(self, request, pk):
        service = Service.objects.get(pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)