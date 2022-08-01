
from django.urls import path
from . import views


urlpatterns = [
    path('', home),
    path('room/', room)
]