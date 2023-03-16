import firebase_admin
from firebase_admin import credentials, db
from .ticketGenerator_utils import create_qr_code_with_text
from firebase_config import firebase_app 

db = db.Database(firebase_app)


def create_event_in_firebase(event_details):
    ref = db.reference("/events")
    event_data = {
        "event_id": event_details.event_id,
        "event_name": event_details.event_name,
        "event_description": event_details.event_description,
        "event_sections": [],
    }

    for ticket in event_details.event_sections:
        name = ticket.get("name")
        price = ticket.get("price")
        available_seats = ticket.get("available_seats")

        ticket_ids = []
        for _ in range(available_seats):
            ticket_id = create_qr_code_with_text(name, price)
            ticket_ids.append(ticket_id)

        event_data["event_sections"].append({
            "name": name,
            "price": price,
            "available_seats": available_seats,
            "ticket_ids": ticket_ids,
        })

    event_ref = ref.push(event_data)
    return event_ref.key