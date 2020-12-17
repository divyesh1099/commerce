from django.contrib.auth.models import AbstractUser
from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=1000)
    daycreated=models.DateTimeField()
    price=models.IntegerField()
    description=models.TextField(blank=True)
    image=models.CharField(max_length=1000)
    uploadimage=models.ImageField(upload_to='images', blank=True, help_text="OPTIONAL")

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    item=models.ManyToManyField(Item, related_name="itemofwatchlist", blank=True)
    def __str__(self):
        return "Watchlist"

class User(AbstractUser):
    # watchlist=models.ForeignKey(Watchlist, related_name="watchlistofuser", blank=True, on_delete=models.CASCADE)
    pass
class Bid(models.Model):
    user=models.ForeignKey(User, related_name="userofbid", on_delete=models.CASCADE, blank=True)
    minimumbid=models.IntegerField()
    maximumbid=models.IntegerField()
    def __str__(self):
        return self.user.username

class Listing(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    startingbid=models.ForeignKey(Bid, related_name="startingbidoflisting", on_delete=models.CASCADE, blank=True)
    image=models.CharField(max_length=1000)
    uploadimage=models.ImageField(upload_to='images', blank=True, help_text="OPTIONAL")
    def __str__(self):
        return self.title

class Comment(models.Model):
    username=models.ForeignKey(User, related_name="usernameofcomment", on_delete=models.CASCADE, blank=True)
    comment=models.TextField()
    def __str__(self):
        return self.username.username


