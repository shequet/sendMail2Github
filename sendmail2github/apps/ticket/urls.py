"""
Urls for the ticket app
"""

from django.urls import include, path
from .views import tickets

urlpatterns = [
    path('', tickets, name='tickets'),
]
