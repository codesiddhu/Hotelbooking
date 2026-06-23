from django.urls import path
from Room_Booking import views
urlpatterns = [
    path("rooms/",views.RoomList.as_view(),name ="rooms"),
    path("rooms-create/",views.RoomCreate.as_view(),name="rooms-create"),
    path("room-details/<int:pk>/",views.RoomImageView.as_view(),name = "room-details"),
    path("occupy-dates/",views.OccupyListView.as_view()),
    path("occupy-dates/<int:pk>/",views.occupyRetriewView().as_view(),name = "room-dates"),
    path("users/",views.UserListAPI.as_view(),name = "user-list"),
    path("users/<int:pk>/",views.UserDetail.as_view()),
    path("login/",views.Login.as_view(),name = "login"),
    path("regester/",views.Register.as_view(),name = "regester")
    

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)