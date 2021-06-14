import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .notification import Notification


@csrf_exempt
def webhook(request):

    if request.method == 'POST':
        notification = Notification()
        json_data = json.loads(request.body)
        ticket = {
            'action': json_data['action'],
            'number': json_data['issue']['number'],
            'repository': json_data['repository']['full_name'],
        }
        action = json_data['action']
        message = notification.generate_message(action, json_data)

        if message is not None:
            notification.send(ticket['number'], message)

        return JsonResponse(ticket)

