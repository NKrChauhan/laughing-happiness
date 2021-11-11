from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse


@api_view(['GET'])
@permission_classes([AllowAny])
def hello_world_api(request, *args, **kwargs):
    message = "Hello world"
    return JsonResponse({"response": message})
