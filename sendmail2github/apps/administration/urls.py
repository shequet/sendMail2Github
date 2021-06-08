"""
Urls for the website app
"""
from django.urls import path
from .views import user_add, users, user_show, user_edit, user_delete
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', users, name='users'),
    path('<int:user_id>', user_show, name='user_show'),
    path('add/', user_add, name='user_add'),
    path('edit/<int:user_id>', user_edit, name='user_edit'),
    path('delete/<int:user_id>', user_delete, name='user_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
