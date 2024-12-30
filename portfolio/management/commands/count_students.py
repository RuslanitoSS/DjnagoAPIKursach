from django.core.management.base import BaseCommand
from portfolio.models import Student

class Command(BaseCommand):
    help = 'Counts the number of students'

    def handle(self, *args, **kwargs):
        count = Student.objects.count()
        self.stdout.write(f'Total number of students: {count}')
