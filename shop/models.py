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

    def create(self):
        self.publish_date = timezone.now()
        self.save()


class WebRequest(models.Model):
    method = models.CharField(max_length=20)
    status_code = models.IntegerField()
    path = models.CharField(max_length=500)
    uri = models.CharField(max_length=500)

    def __str__(self):
        return '[{}] {} {} {}'.format(self.method, self.path, self.uri, self.status_code)

    def create(self):
        self.save()
