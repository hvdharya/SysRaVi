from django.db import models


# Create your models here.


# class TicketEvent(models.Model):
#
#
# 	event = models.ForeignKey('event.Event')




class Ticket(models.Model):

    price = models.FloatField()
    type = models.CharField(max_length=100)
    seat_num = models.CharField(max_length=10)
    event = models.ForeignKey('event.Event')
    buy = models.ForeignKey('Buy',null=True)
    free = models.IntegerField()


class Buy(models.Model):

    user = models.ForeignKey('account.User',unique=False)
    event = models.ForeignKey('event.Event',unique=False)
    date = models.DateField()
    purchase_id = models.IntegerField()
    trace_id = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey('account.User')
    event = models.ForeignKey('event.Event')
    number = models.IntegerField()