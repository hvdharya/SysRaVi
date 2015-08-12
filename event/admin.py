from django.contrib import admin
from event.models import  Event,Type,Subtype
# Register your models here.

admin.site.register(Event)
admin.site.register(Type)
admin.site.register(Subtype)

