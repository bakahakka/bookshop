from django.core.management.base import BaseCommand
from ...models import Book


class Command(BaseCommand):
    """
    This command displays a list of Book Models when called.
    When no arguments given, displays books in a default order.
    If argument `--sort` with value `asc` or `desc` is passed
    Displays sorted by publish date.
    """
    args = '<--sort asc | desc ...>'
    help = 'Displays a list of books created.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--sort',
            action='store',
            dest='sort',
            help='Value: asc | desc. Sorts the books '
                 'by publish date in ASC or DESC order.',
        )

    def print_out(self, items):
        """
        Prints out each item in a list or QuerySet
        :param items:
        :return:
        """
        for item in items:
            self.stdout.write('pk: #{}: {}, ISBN: {}, price: {}'.format(
                item.pk,
                str(item),
                item.ISBN,
                item.price))

    def handle(self, *args, **options):
        if options['sort'] == 'asc':
            books = Book.objects.all().order_by('publish_date')
            self.print_out(books)
        elif options['sort'] == 'desc':
            books = Book.objects.all().order_by('-publish_date')
            self.print_out(books)
        else:
            books = Book.objects.all()
            self.print_out(books)
