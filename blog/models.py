from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    postmedia = models.ImageField(upload_to='media/')
