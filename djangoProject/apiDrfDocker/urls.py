from django.urls import path
from .views import hello_world_api


app_name = "apiDrfDocker"
urlpatterns = [
    path("helloWorld/", hello_world_api, name="hello_world")
]
