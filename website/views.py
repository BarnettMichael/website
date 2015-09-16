from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.forms import AuthenticationForm

import datetime

# Create your views here.

def home(request):
    authform = AuthenticationForm()
    today = datetime.date.today()
    return render(request, "website/index.html", {'today': today,
                                                  'now': now(),
                                                  'authform': authform,
                                                  }
                  )

#def user_login(request):

    #if request.method == POST