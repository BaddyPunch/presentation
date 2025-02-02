from django.http import JsonResponse
from django.urls import path
from . import views


urlpatterns = [
    path('api/upload/', views.upload_presentation, name='upload_presentation'),
    path('api/download/<int:presentation_id>/', views.download_presentation, name='download_presentation'),
    path('api/items', views.get_presentations, name='get_presentations')
]


