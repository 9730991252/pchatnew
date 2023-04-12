from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ac/<str:groupkaname>/',consumers.MyAsyncConsumer.as_asgi()),
]