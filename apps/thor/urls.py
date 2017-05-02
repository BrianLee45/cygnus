from django.conf.urls import url
from . import views

app_name = "thor"

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^show$', views.showAdd, name='showAdd'),
    url(r'^add$', views.addTrip, name='add'),
    url(r'^(?P<trip_id>\d+)/join$', views.joinTrip, name='join'),
    url(r'^(?P<trip_id>\d+)/destination$', views.showDestination, name='destination'),
]
