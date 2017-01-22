from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^dock/(?P<id>[0-9]+)/$', dock_detail, name='dock_detail'),
]