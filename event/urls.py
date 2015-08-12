__author__ = 'Hvdh'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView, eventsType, eventsSubtype,subtypes
from account.views import events,eventsSub,eventsall

from Ravi import views
from django.views.generic import RedirectView

urlpatterns = patterns('',

        url(r'^(?P<e_type>[a-zA-Z]+)/$', events),
        url(r'^$', eventsall),
)
