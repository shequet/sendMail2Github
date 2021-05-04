"""
Urls for the website app
"""

from django.contrib import admin
from django.urls import include, path
from .views import register, profile
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
