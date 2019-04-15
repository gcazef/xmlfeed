from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch new orders from API'

    def handle(self, *args, **kwargs):
        self.stdout.write('This is the fetch command')