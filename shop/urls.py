from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^log$', views.log_view, name='log_view'),
    url(r'^books/new/$', views.add_book, name='add_book'),
    url(r'^books/(?P<pk>\d+)/edit/$', views.edit_book, name='edit_book'),
]
