from django.shortcuts import render
from django.http import JsonResponse
from .ticketGenerator_utils import main as generate_qr_ticket

def generate_qr_ticket(request):
    qr_code_url = generate_qr_ticket()
    response = {"qr_code_url": qr_code_url}
    return JsonResponse(response)
