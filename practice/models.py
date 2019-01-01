from django.db import models
# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Subdomain(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Question(models.Model):
    subdomain = models.ForeignKey(Subdomain, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question
