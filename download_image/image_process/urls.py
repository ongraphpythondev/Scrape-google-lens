from django.urls import path
from .views import getimage,processimage


urlpatterns = [
    path('image/', getimage, name='myImage'),
    path('process_image/', processimage),
]