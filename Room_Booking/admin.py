from django.contrib import admin
from Room_Booking.models import Room,RoomImage,OccupyDate

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name',"type","pricePerNight","currency","maxOcupy","description"]
admin.site.register(Room,RoomAdmin)

class RoomAdminImages(admin.ModelAdmin):
    list_display = ['image',"caption","room"]
admin.site.register(RoomImage,RoomAdminImages)

class OccupyAdmin(admin.ModelAdmin):
    list_display = ["room","dateField"]
admin.site.register(OccupyDate,OccupyAdmin)