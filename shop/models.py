from django.db import models
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class LogSaveOrDeleteMixin(models.Model):
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        super(LogSaveOrDeleteMixin, self).delete(*args, **kwargs)
        logger.info(" {} instance {} (pk {}) deleted".format(self._meta, self, self.pk))

    def save(self, *args, **kwargs):
        super(LogSaveOrDeleteMixin, self).save(*args, **kwargs)
        logger.info(" {} instance {} (pk {}) saved".format(self._meta, self, self.pk))


# Create your models here.
class Book(LogSaveOrDeleteMixin, models.Model):
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
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '[{}] {} {} {} {}'.format(
            self.method,
            self.path,
            self.uri,
            self.status_code,
            self.time)
