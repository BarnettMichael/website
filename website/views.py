from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth import logout

import datetime

# Create your views here.

def home(request):
    today = datetime.date.today()
    return render(request, "website/index.html", {'today': today,
                                                  'now': now(),
                                                  }
                  )

def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html", {})