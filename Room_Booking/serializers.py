from Room_Booking.models import Room
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from Room_Booking.models import RoomImage
from Room_Booking.models import OccupyDate
class RoomImageSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = RoomImage
        fields = "__all__"
class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializers(many = True,read_only=True)
    class Meta:
        model = Room
        fields = ["id","name","type","pricePerNight","currency","maxOcupy","description","images"]

class OccupySerializers(serializers.ModelSerializer):
    # room = serializers.HyperlinkedModelSerializer(
        
    #     queryset = Room.objects.all()
    # )
    class Meta:
        model = OccupyDate
        fields = ["id","room","dateField"]
        
from django.contrib.auth.hashers import make_password
from Room_Booking.models import User
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def validate_password(self, value):
        return make_password(value)