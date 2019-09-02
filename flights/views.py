from rest_framework.generics import ListAPIView
from django.utils import timezone
from .models import Flight, Booking

from .serializers import FlightSerializer, BookingSerializer

class FlightList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingList(ListAPIView):
	queryset = Booking.objects.filter(date__gte= timezone.now())
	serializer_class = BookingSerializer
