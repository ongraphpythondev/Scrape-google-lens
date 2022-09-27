from django.urls import path
from .views import AllImages


urlpatterns = [
    path('image/', AllImages.as_view(), name='myImage'),
    # path('process_image/', processimage),
]