from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView, eventsType,ticketmanager, create_event,edit_event,delete_events,addType,delType,showsubs,delSubType,edit_subtype
from Ravi import views
from account.views import allUsers, delUsers,eventsall,types,portal, logout
from ticket.views import buymanager,show_cart

urlpatterns = patterns('',

    url(r'^events/([a-zA-Z0-9]+)/', eventsType),
    url(r'^tickets/([a-zA-Z0-9]+)/', ticketmanager),
    url(r'^buys/([a-zA-Z0-9]+)/', buymanager),
    url(r'^([0-9]+)/([0-9]+)', portal),
    url(r'^settings/', views.adminSetting),
    url(r'^users/all', allUsers),
    url(r'^users/(?P<userid>[0-9]+)$/', delUsers),
    url(r'^$', views.modir),
    url(r'^add-event/([a-zA-Z0-9]+)', create_event),
    url(r'^edit-events/all/', eventsall),
    url(r'^types/all/', types),
    url(r'^addTypes/', addType),
    url(r'^deleteTypes/([a-zA-Z0-9]+)', delType),
    url(r'^SubTypes/([a-zA-Z0-9]+)', showsubs),
    url(r'^deleteSubTypes/([a-zA-Z0-9]+)', delSubType),
    url(r'^edit/([a-zA-Z0-9]+)',edit_subtype),
    url(r'^cart/',show_cart),



)



