from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *

class UserRegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role='Customer')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsAPIView(APIView):
    permission_classes = [IsCustomer]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserDeleteAPIView(APIView):
    permission_classes = [IsCustomer]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserUpdateAPIView(APIView):
    queryset = Users.objects.all()
    permission_classes = []

    def put(self, request):
        user = request.user
        serializer = UserUpdateSerializer
        if serializer.is_valid:
            serializer.save(role='Customer')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)