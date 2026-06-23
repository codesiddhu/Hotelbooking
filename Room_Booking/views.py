from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import Room, RoomImage, OccupyDate, User
from .serializers import RoomSerializer,RoomImageSerializers,OccupySerializers,userSerializers



# ------------------ ROOM APIs ------------------

class RoomList(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCreate(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomImageView(RetrieveAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializers


# ------------------ BOOKING APIs ------------------

class OccupyListView(ListAPIView):
    queryset = OccupyDate.objects.all()
    serializer_class = OccupySerializers
    permission_classes = [IsAuthenticated]

class occupyRetriewView(RetrieveAPIView):
    queryset = OccupyDate.objects.all()
    serializer_class = OccupySerializers 
# ------------------ USER APIs ------------------

class UserListAPI(ListAPIView):
    serializer_class = userSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        if obj == user or user.is_staff or user.is_superuser:
            return obj
        raise PermissionDenied("Not allowed")


# ------------------ AUTH APIs ------------------

class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name
            },
            "token": token.key
        })


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name
            },
            "token": token.key
        })