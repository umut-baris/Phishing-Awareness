from django.db import models

from embed_video.fields import EmbedVideoField
# Create your models here.

class Question(models.Model):
    ID = models.IntegerField(primary_key=True)
    Phishing = models.BooleanField()
    Medium = models.CharField(max_length=10)
    Screenshot = models.CharField(max_length=150)
    URL = models.CharField(max_length=150)

    def __str__(self):
        return str(self.ID)

class Websites(models.Model):
    ID = models.IntegerField(primary_key=True)
    Phishing = models.BooleanField()
    Html_Name = models.CharField(max_length=150)
    URL = models.CharField(max_length=150)

    def __str__(self):
        return str(self.ID)

class Emails(models.Model):
    ID = models.IntegerField(primary_key=True)
    Phishing = models.BooleanField()
    Html_Name = models.CharField(max_length=150)
    URL = models.CharField(max_length=150)
    CUTE = models.CharField(max_length=7)

    def __str__(self):
        return str(self.ID)

class Answer(models.Model):
    ID = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return str(self.ID)

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-added']