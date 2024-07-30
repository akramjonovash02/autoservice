from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from userApp.permissions import IsCustomer
from .models import OrderProduct, OrderService, Product, Service, Users
from .serializers import OrderProductSerializer, OrderServiceSerializer


class OrderProductCreateView(APIView):
    permission_classes = [IsCustomer]

    def post(self, request):
        serializer = OrderProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderServiceCreateView(APIView):
    permission_classes = [IsCustomer]

    def post(self, request):
        serializer = OrderServiceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)