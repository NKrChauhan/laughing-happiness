from django.urls import path
from .views import hello_world_api

urlpatterns = [
    path("helloWorld/", hello_world_api)
]
