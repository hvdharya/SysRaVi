from django.db import models
from account.models import User
from event.models import Event

# Create your models here.
class Feedback(models.Model):

    rate = models.IntegerField()
    comment = models.CharField(max_length=160,null=True)

    user = models.ForeignKey(User,unique=False,null=True)
    event = models.ForeignKey(Event,unique=False)