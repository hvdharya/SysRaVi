from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView, eventsType, create_event,edit_event,delete_events,subtypes,subtype,delete_tickets
from account.views import create_account,login_to_site,allUsers,delUsers,eventsSub
from ticket.views import buy
from Ravi import views
from django.views.generic import RedirectView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.startPage),
    url(r'^main/', views.mainPage),
    url(r'^event/([0-9]+)', eventDetailedView),
    url(r'^buy/', include('ticket.urls')),
    url(r'^portal/', include('account.urls')),
    # url(r'^user/', views.user),
    url(r'^category/([a-zA-Z]+)', subtypes),
    url(r'^cat/([a-zA-Z]+)', subtype),
    url(r'^(?P<e_type>[a-zA-Z]+)/(?P<subtype>[a-zA-Z]+)', eventsSub),
    url(r'^events/', include('event.urls')),
    url(r'^add-event/', create_event),
    url(r'^sign-up/', views.signup),
    url(r'^signed-up/', create_account),
    url(r'^user/([0-9]+)/', views.edit_see),
    url(r'^my-admin/', include('account.urls')),
    url(r'^edit-event/([0-9]+)', edit_event),
    url(r'^login/',login_to_site),
    url(r'^events-delete/([a-zA-Z0-9]+)',delete_events),
    url(r'^users/all/',allUsers),
    url(r'^users-delete/([0-9]+)',delUsers),
    url(r'^tickets-delete/([a-zA-Z0-9]+)/', delete_tickets),
)



