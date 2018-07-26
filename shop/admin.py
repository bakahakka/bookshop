from django.contrib import admin
from django.contrib.admin.utils import flatten_fieldsets
from .models import Book, WebRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(WebRequest)

