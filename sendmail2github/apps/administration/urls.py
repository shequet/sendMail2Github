"""
Urls for the website app
"""
from django.urls import path
from .views import register, users, user_show
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', users, name='users'),
    path('<int:user_id>', user_show, name='user_show'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
