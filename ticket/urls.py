__author__ = 'Hvdh'
from django.conf.urls import patterns, include, url
from ticket.views import buy,add_to_cart

urlpatterns = patterns('',
                       url(r'^([0-9]+)/([0-9]+)', buy),
                       url(r'^([0-9]+)/', add_to_cart),
                       )