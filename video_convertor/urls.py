from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<str:mp3_filename>/', views.download_mp3, name='download_mp3'),
]
