from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250),
    content = models.TextField()

    def _str_(self):
        return self.title

