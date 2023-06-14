from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name= models.CharField(max_length=200)
    description= models.TextField(null=True, blank=True)
    # participants= 
    updated= models.DateTimeField(auto_now=True)#To note the data, when was a room updated last time. Whenenver we save()
    created= models.DateTimeField(auto_now_add=True)# when we created or saved first

    class Meta:#to order the rooms
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

#Django has built in user model
class Message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)#one to many
    room= models.ForeignKey(Room, on_delete=models.CASCADE)#One room can have many messages.
    body= models.TextField()
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]