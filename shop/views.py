from django.shortcuts import render
from django.utils import timezone
from .models import Book, WebRequest


# Create your views here.
def book_list(request):
    books = Book.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'shop/book_list.html', {'books': books})


def log_view(request):
    reqs = WebRequest.objects.all().order_by('-time')[:10]
    return render(request, 'shop/log_view.html', {'reqs': reqs})
