from django.db import models


class Item(models.Model):
    item = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()


class Forum(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=3000)

class Comment(models.Model):
    name = models.CharField(max_length=64)
    text = models.CharField(max_length=200)
    last_updated = models.DateTimeField()
    forum = models.ForeignKey(Forum, models.CASCADE) 