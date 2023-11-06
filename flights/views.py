from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    non_passengers = Passenger.objects.exclude(flights=flight).all()

    return render(request, "flights/flight.html", {
        'flights': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': non_passengers
    })

def book(request, flight_id):
    if request.method == "POST":
        passenger_id = request.POST['new_passenger']
        passenger_new = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
        passenger_new.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))



