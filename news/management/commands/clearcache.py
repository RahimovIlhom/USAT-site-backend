from django.core.cache import cache
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Clears the cache'

    def handle(self, *args, **kwargs):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the cache'))
