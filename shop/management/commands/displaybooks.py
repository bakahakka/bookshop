from django.core.management.base import BaseCommand
from ...models import Book


class Command(BaseCommand):
    args = '<--sort asc | desc ...>'
    help = 'Displays a list of books created. Sorts by publish date'

    def add_arguments(self, parser):
        parser.add_argument(
            '--sort',
            action='store',
            dest='sort',
            help='order by: asc | desc',
            default='asc'
        )

    def print_out(self, items):
        """
        Prints out each item in a list or QuerySet
        :param items:
        :return:
        """
        for item in items:
            self.stdout.write('pk: #{}: {}, ISBN: {}, price: {}'
                              .format(item.pk, str(item), item.ISBN, item.price))

    def handle(self, *args, **options):
        if options['sort'] == 'asc':
            books = Book.objects.all().order_by('publish_date')
            self.print_out(books)
        elif options['sort'] == 'desc':
            books = Book.objects.all().order_by('-publish_date')
            self.print_out(books)
