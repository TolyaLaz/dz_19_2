from django.core.management import BaseCommand
from django.core.management import call_command
from catalog.models import Product,Category

class Command(BaseCommand):
    class Command(BaseCommand):
        help = 'Initialize database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', './catalog_data.json')
