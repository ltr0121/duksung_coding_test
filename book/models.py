from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.title