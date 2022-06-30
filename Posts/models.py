from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    slug = models.CharField(max_length=30)
