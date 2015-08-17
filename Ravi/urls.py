from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView, eventsType, create_event,edit_event,delete_events,subtypes,subtype,delete_tickets
from account.views import create_account,login_to_site, eventsSub, log_out
from ticket.views import show_cart, delete_cart
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
    url(r'^category/([a-zA-Z0-9]+)', subtypes),
    url(r'^cat/([a-zA-Z0-9]+)', subtype),
    url(r'^(?P<e_type>[a-zA-Z]+)/(?P<subtype>[a-zA-Z]+)', eventsSub),
    url(r'^events/', include('event.urls')),
    url(r'^add-event/', create_event),
    url(r'^sign-up/', views.signup),
    url(r'^signed-up/', create_account),
    url(r'^cart/$', show_cart),
    url(r'^cart-delete/([0-9]+)/$', delete_cart),
    url(r'^addtocart/',include('ticket.urls')),
    url(r'^my-admin/', include('account.urls')),
    url(r'^edit-event/([0-9]+)', edit_event),
    url(r'^login/',login_to_site),
    url(r'^exit/',log_out),
    url(r'^events-delete/([a-zA-Z0-9]+)',delete_events),
    url(r'^tickets-delete/([a-zA-Z0-9]+)/', delete_tickets),
    url(r'^profile/$', views.profile),
    url(r'^settings/$', views.profile_settings),
    url(r'^event-add/([0-9]+)', create_event),
    url(r'^search/', views.search_event),
)



