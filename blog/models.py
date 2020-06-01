from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    postmedia = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:80]

    def pubdate_pretty(self):
        return self.pubdate.strftime('%b %e %Y')
