from .models import Parking
from django.contrib import messages

def delete_parking_data(id, request):
    d = Parking.objects.get(id=id)
    d.delete()
    messages.error(request, "Data Deleted Successfully", extra_tags='danger')
