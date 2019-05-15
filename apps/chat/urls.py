from django.urls import path

from .views import index


app_name = 'chat'
urlpatterns = [
    path('chat/', index, name='index'),
]
