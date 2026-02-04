from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Add logic to populate your database
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
