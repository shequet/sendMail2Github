"""
Urls for the ticket app
"""

from django.urls import path
from .views import tickets, ticket_show

urlpatterns = [
    path('', tickets, name='tickets'),
    path('close', tickets, name='tickets_close'),
    path('<int:ticket_id>', ticket_show, name='ticket_show'),
]
