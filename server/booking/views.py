from django.http.response import HttpResponse
from django.shortcuts import render
from booking.models import Booking
from django.views.decorators.csrf import csrf_exempt

import booking.repository as repository

# Create your views here.

@csrf_exempt
def booking(request):
    # READ (all)
    if request.method == "GET":
        booking = repository.get_all(Booking)
        return HttpResponse(booking, content_type="text/json")
    # CREATE
    if request.method == "POST":
        response = repository.add(Booking, request)
        return HttpResponse(response, content_type="text/json")

@csrf_exempt
def booking_id(request, id):
    # READ (single)
    if request.method == "GET":
        booking = repository.get(Booking, id)
        return HttpResponse(booking, content_type="text/json")
    # EDIT
    if request.method == "PUT":
        booking = repository.edit(Booking, id, request)
        return HttpResponse(booking, content_type="text/json")
    # DELETE
    if request.method == "DELETE":
        booking = repository.delete(Booking, id)
        return HttpResponse(booking, content_type="text/json")
