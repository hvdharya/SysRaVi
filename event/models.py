from django.db import models


# Create your models here.
#
# class Music(models.Model):
#
#     # name = models.CharField(max_length=100)
#     style = models.CharField(max_length=10)
#     # desc = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.name
#
#
# class Cinema(models.Model):
#
#     # name = models.CharField(max_length=100)
#     director = models.CharField(max_length=10)
#     genre = models.CharField(max_length=10)
#     producer = models.CharField(max_length=10)
#     # desc = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.name

# class Sport(object):


# class IndividualSport(object):

# class Theater(models.Model):


# class Place(models.Model):
#
#     name = models.CharField(max_length=100)
#     addr = models.CharField(max_length=100)
#     capacity = models.IntegerField()
#     placeType = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.name


class Type(models.Model):

    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Subtype (models.Model):

    sub_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.ForeignKey('Type')

    def __str__(self):
        return self.name

class Event(models.Model):

    name = models.CharField(max_length=100)
    duration = models.FloatField()
    desc = models.CharField(max_length=100)
    date = models.DateField()
    deadline = models.DateField()
    picture = models.ImageField()
    place = models.CharField(max_length=100)
    ticket_num = models.IntegerField()
    type = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    ticket_price = models.CharField(max_length=8)
    rate = models.IntegerField()



    def __str__(self):
        return self.name

		
		