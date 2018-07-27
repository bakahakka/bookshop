from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = ('author', 'title', 'ISBN', 'price', 'publish_date')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'publish_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publish date',
            })
        }
