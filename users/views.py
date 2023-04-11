from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView, Response, Request
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, 200)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 201)
