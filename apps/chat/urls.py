from django.urls import path

from .views import index, room


app_name = 'chat'
urlpatterns = [
    path('chat/', index, name='index'),
    path('chat/<str:room_name>/', room, name='room'),
]
