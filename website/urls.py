"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^rwc', include('rwc.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^project_test/?$', views.project_test, name='project_test'),
    url(r'^projects/score_predictor/?$', views.project_score_predictor, name='project_score_predictor'),
    url(r'^projects/ffhelper/?$', views.project_ffhelper, name='project_ffhelper'),
    url(r'^projects/lootfilter/?$', views.project_lootfilter, name='project_lootfilter'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
