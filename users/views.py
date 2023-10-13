from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User, Group, Permission
from .serializers import RegisterSerializer, UsersSerializers, GroupSerializer, PermissionSerializer,MyTokenObtainPairSerializer
from users.permissions import IsManagerUser

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializers

    permission_classes = [IsManagerUser]



class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = [IsManagerUser]


class PermissionsView(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    permission_classes = [IsManagerUser]