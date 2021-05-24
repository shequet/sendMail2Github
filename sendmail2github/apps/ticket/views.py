"""
ticket app views document
"""
from django.shortcuts import render
from .ticket_api import TicketApi


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

