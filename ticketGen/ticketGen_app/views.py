import uuid
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .ticketGenerator_utils import main as generate_qr_ticket
from .event_utils import create_event_in_firebase

def generate_qr_ticket_view(request):
    qr_code_url = generate_qr_ticket()
    response = {"qr_code_url": qr_code_url}
    return JsonResponse(response)

@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event_unique_id = str(uuid.uuid4())
            event_name = data.get('event_name')
            event_description = data.get('event_description')
            event_sections = data.get('event_sections')

            # Validate and process the event_sections array
            processed_tickets = []
            for ticket in event_sections:
                name = ticket.get('name')
                description = ticket.get('description')
                price = ticket.get('price')
                available_seats = ticket.get('available_seats')

                # Perform validation and processing for each ticket, e.g., save to the database
                processed_ticket = {
                    "name": name,
                    "description": description,
                    "price": price,
                    "available_seats": available_seats
                }
                processed_tickets.append(processed_ticket)

            event_details = {
                "event_id": event_unique_id,
                "event_name": event_name,
                "event_description": event_description,
                "event_sections": processed_tickets,
                "event_key": event_key,
            }
            
            event_key = create_event_in_firebase(event_details)

            response = {
                "event_name": event_name,
                "event_description": event_description,
                "event_sections": processed_tickets,
                "event_key": event_key,
                "status": "success",
            }
            return JsonResponse(response)

        except Exception as e:
            return HttpResponseBadRequest(str(e))

    else:
        return HttpResponseBadRequest("Invalid request method")