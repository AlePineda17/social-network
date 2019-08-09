from django.db import models
from user.models import User


class Activity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    picture = models.ImageField(upload_to='images')
    text = models.TextField(blank=True)


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
