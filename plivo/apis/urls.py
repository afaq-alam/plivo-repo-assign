from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^inbound/sms/$', views.inbound),
    url(r'^outbound/sms/$', views.outbound),
]
