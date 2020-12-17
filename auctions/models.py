from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bid(models.Model):
    minimumbid=models.IntegerField()
    maximumbid=models.IntegerField()
    def __str__(self):
        return self.username.username

class Listing(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    startingbid=models.ForeignKey(Bid, related_name="startingbidoflisting", on_delete=models.CASCADE, blank=True)
    image=models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Comment(models.Model):
    username=models.ForeignKey(User, related_name="usernameofcomment", on_delete=models.CASCADE, blank=True)
    comment=models.TextField()
    def __str__(self):
        return self.username.username
