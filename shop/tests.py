from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Book, WebRequest
from .forms import BookForm
from .middleware import TrackWebRequestsMiddleware
import shop.views as views


# Create your tests here.
class BookTest(TestCase):
    """
    Test case for Book model
    """
    def create_book(self):
        """
        Create mock Book instance
        :return: Book
        """
        return Book.objects.create(
            author='Benedict Combherwirtb',
            title='Y is mah name so messed up bruh',
            ISBN='848925742894',
            price=42.42,
            publish_date=timezone.now()
        )

    def test_book_creation(self):
        """
        Should create a Book
        :return:
        """
        book = self.create_book()
        self.assertTrue(isinstance(book, Book))

    def test_book_list_view(self):
        """
        Should list the Book models on the page
        :return:
        """
        book = self.create_book()
        url = reverse(views.book_list)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(book.title, str(resp.content))

    def test_valid_book_form(self):
        """
        Should be valid Book form
        :return:
        """
        data = {
            'author': 'Benedict Combherwirtb',
            'title': 'Y is mah name so messed up bruh',
            'ISBN': '848925742894',
            'price': 42.42,
            'publish_date': timezone.now()
        }
        form = BookForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_book_form(self):
        """
        Should be invalid book form
        :return:
        """
        data = {
            'author': '',
            'title': '',
            'ISBN': '',
            'price': '',
            'publish_date': ''
        }
        form = BookForm(data=data)

        self.assertFalse(form.is_valid())


class WebRequestTest(TestCase):
    """
    Test case for WebRequest model
    """
    def create_web_request(self):
        """
        Create mock WebRequest instance
        :return: WebRequest
        """
        return WebRequest.objects.create(
            path='/',
            method='GET',
            status_code=200,
            uri='http://benedictcomberwuyrtrpersonalwebpage.com',
            time=timezone.now()
        )

    def test_create_web_request(self):
        """
        Should create a WebRequest
        :return:
        """
        request = self.create_web_request()
        self.assertTrue(isinstance(request, WebRequest))

    def test_web_request_log_view(self):
        """
        Should have a list of WebRequest models on page
        :return:
        """
        request = self.create_web_request()
        url = reverse(views.log_view)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(request.uri, str(resp.content))


class TrackWebRequestsMiddlewareTest(TestCase):
    """
    Test case for TrackWebRequestsMiddleware
    """
    def test_middleware(self):
        """
        Should intercept a request and save it to DB
        :return:
        """
        url = reverse(views.book_list)
        TrackWebRequestsMiddleware(self.client.get(url))
        self.assertEqual(WebRequest.objects.all().count(), 1)
