from django.shortcuts import render
from django.utils import timezone
from .models import Book


# Create your views here.
def book_list(request):
    books = Book.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'shop/book_list.html', {'books': books})
