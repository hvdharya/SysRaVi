from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):

    user = models.OneToOneField(User)
    address = models.CharField(max_length=100,null=True)
    phone_num = models.CharField(max_length=12,null=True)
    gender = models.CharField(max_length=5)
    avatar = models.ImageField(null=True,default='528675-roger-federer.jpg')
    userType = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username


