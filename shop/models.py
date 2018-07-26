from django.db import models
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=150)
    ISBN = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "{} by {}".format(self.title, self.author)
