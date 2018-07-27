from django.contrib import admin
from .models import Book, WebRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(WebRequest)
