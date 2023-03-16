from django.urls import path
from . import views

urlpatterns = [
    path("generate-ticket/", views.generate_qr_ticket, name="generate-ticket"),
]
