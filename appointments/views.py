from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Appointment
from .serializers import AppointmentSerializer
from .services import is_doctor_available


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):

        doctor = request.data.get("doctor")
        date = request.data.get("date")

        if not is_doctor_available(doctor, date):
            return Response(
                {"error": "Doctor already has an appointment at this time"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)