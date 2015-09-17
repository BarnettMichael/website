from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rwc_home, name='rwc_home'),
    url(r'^/guesses$', views.rwc_guesses, name='rwc_guesses')
]