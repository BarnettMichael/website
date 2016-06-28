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

def project_test(request):
    return render(request, "website/project_template.html", {})

def project_score_predictor(request):
    return render(request, "website/project_score_predictor.html", {})

def project_ffhelper(request):
    return render(request, "website/project_ffhelper.html", {})

def project_lootfilter(request):
    return render(request, "website/project_lootfilter.html", {})

def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html", {})