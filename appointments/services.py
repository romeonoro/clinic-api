from .models import Appointment

def is_doctor_available(doctor, date):

    appointment_exists = Appointment.objects.filter(
        doctor=doctor,
        date=date
    ).exists()

    return not appointment_exists