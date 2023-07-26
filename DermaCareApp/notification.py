from .models import Appointment

def get_notification(request):
    count_accept = Appointment.objects.filter(accepted = False).count()
    notification_data = {
        'count_accept':count_accept
    }
    return count_accept