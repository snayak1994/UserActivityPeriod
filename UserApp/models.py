from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=200,primary_key=True)
    userName = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

class ActivityPeriod(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

