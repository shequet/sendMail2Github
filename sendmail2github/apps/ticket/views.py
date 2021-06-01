"""
ticket app views document
"""
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .ticket_api import TicketApi


def ticket_show(request, ticket_id):
    ticket_api = TicketApi()
    comment = request.POST.get('comment', '')

    if comment != '':
        ticket_api.create_comment(id=ticket_id, comment='User: {mail}<br><br>{comment}'.format(mail=request.user.email, comment=comment))

    return render(
        request,
        'repository_ticket_show.html', {
            'issue': ticket_api.get_ticket(id=ticket_id)
        })


def tickets(request):
    state = 'open'
    if request.path == '/ticket/close':
        state = 'closed'

    ticket_api = TicketApi()
    labels = []

    status = request.POST.get('status', '')
    if status != '':
        labels.append(status)

    user = request.POST.get('user', '')
    if user != '':
        labels.append(user)
    elif user != 'all':
        user = 'User: {mail}'.format(mail=request.user.email)
        labels.append(user)

    return render(
        request,
        'repository_tickets.html', {
            'tickets': ticket_api.get_tickets(
                labels=labels,
                state=state
            ),
            'filters': {
                'status': status,
                'user': user,
            }
        })

