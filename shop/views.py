from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from .models import Book, WebRequest
from .forms import BookForm


# Create your views here.
def book_list(request):
    books = Book.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'shop/book_list.html', {'books': books})


def log_view(request):
    reqs = WebRequest.objects.all().order_by('-time')[:10]
    return render(request, 'shop/log_view.html', {'reqs': reqs})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'shop/create_edit_view.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)

    return render(request, 'shop/create_edit_view.html', {'form': form})
