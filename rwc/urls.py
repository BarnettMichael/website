from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rwc_home, name='rwc_home'),
    url(r'^/$', views.rwc_home, name='rwc_home'),
    url(r'^/guesses$', views.rwc_guesses, name='rwc_guesses'),
    url(r'^/results$', views.rwc_results, name='rwc_results'),
    url(r'^/guesses/(?P<pk>[0-9]+)$', views.rwc_guesses_more, name='rwc_guesses_more'),
]