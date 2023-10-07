from django.urls import path
from .views import yt_url

urlpatterns = [
    path('', yt_url, name='download_yt_video' )
]
