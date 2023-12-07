from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return self.name
