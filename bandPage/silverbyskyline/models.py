from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.

class Post(models.Model): 
    # Default behaviour - Django creates primary keys for you
    title = models.CharField(max_length=140)    
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Adding the below to try and include video players

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True, null=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
