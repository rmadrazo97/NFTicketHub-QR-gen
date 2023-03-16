from django.urls import path
from . import views

urlpatterns = [
    path("generate-ticket/", views.generate_qr_ticket_view, name="generate-ticket"),
    path("create-event/", views.create_event, name="create_event"), 
]
