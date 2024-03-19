from django.db import models
import datetime

class Request(models.Model):
    requestBy = models.IntegerField(null=True)
    requestType = models.TextField(null=True) 
    requestDetails = models.TextField()
    requestDate = models.DateField(default = datetime.datetime.now().date())
    requestImage = models.FileField(null=True)