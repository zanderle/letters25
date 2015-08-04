import csv
from django.core.management.base import BaseCommand

from letters_collection.models import Letter


class Command(BaseCommand):
    help = 'Import popularity indexes from file to database'

    def add_arguments(self, parser):
        parser.add_argument('path_to_file', type=str)

    def handle(self, *args, **options):
        with open(options['path_to_file'], 'rb') as ts:
            reader = csv.reader(ts, delimiter='\t')
            for row in reader:
                slug = row[0].split('letters/')[1][:-1]
                Letter.objects.filter(slug=slug).update(popularity_index=int(row[1]))

        self.stdout.write('Successfully finished importing popularity index')
