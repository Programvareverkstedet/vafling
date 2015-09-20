# Create your views here.
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from waffles.models import *


@login_required
def dashboard(request):
    events = Event.objects.filter(timeTo__gt=timezone.now()).all()
    return HttpResponse([e for e in events], content_type="text/plain")
