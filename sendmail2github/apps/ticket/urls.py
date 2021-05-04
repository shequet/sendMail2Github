"""
Urls for the ticket app
"""

from django.urls import include, path
from .views import repositories_index, repository_tickets

urlpatterns = [
    path('repository', repositories_index, name='repositories_index'),
    path('repository/<int:repository_id>', repository_tickets, name='repository_tickets'),
]
