import os
import datetime
from django.core.management.base import BaseCommand

from letters_collection.models import Letter


class Command(BaseCommand):
    help = 'Import letters to database'

    def add_arguments(self, parser):
        parser.add_argument('path_to_letters', type=str)

    def handle(self, *args, **options):
        for root, dirs, files in os.walk(options['path_to_letters']):
            if root == options['path_to_letters']:
                self.stdout.write('Skipping root - %s' % root)
                continue
            try:
                self.stdout.write('Looking into %s' % root)
                self.stdout.write('Try to open the letter at %s' % os.path.join(root, 'letter.txt'))
                published_on = datetime.datetime.utcfromtimestamp(os.path.getmtime(root))
                read_the_letter = False
                letter = ''
                name = ''
                age = ''
                occupation = ''
                location = ''
                illustrator = ''
                with open(os.path.join(root, 'letter.txt'), 'r') as file:
                    for line in file:
                        if read_the_letter:
                            letter += unicode(line, 'utf-8')
                        if 'name:' in line.lower():
                            name_line = line.split(':')
                            name = name_line[1]
                            name = name.strip()
                        elif 'age:' in line.lower():
                            age_line = line.split(':')
                            age = age_line[1]
                            age = age.strip()
                        elif 'occupation:' in line.lower():
                            occupation_line = line.split(':')
                            occupation = occupation_line[1]
                            occupation = occupation.strip()
                        elif 'location:' in line.lower():
                            location_line = line.split(':')
                            location = location_line[1]
                            location = location.strip()
                        elif 'illustrator:' in line.lower():
                            illustrator_line = line.split(':')
                            illustrator = illustrator_line[1]
                            illustrator = illustrator.strip()
                        elif 'content:' in line.lower():
                            read_the_letter = True

                slug = root.split('/')[-1]
                slug = slug.split('.')[1]

                if not Letter.objects.filter(author=name).exists():
                    new_letter = Letter(
                        author=name,
                        age=age,
                        occupation=occupation,
                        location=location,
                        # illustrator=illustrator,
                        slug=slug,
                        letter=letter,
                        timestamp_published=published_on,
                        published=True
                        )
                    new_letter.save()
                else:
                    old_letter = Letter.objects.filter(author=name)[0]
                    old_letter.illustration.author = illustrator
                    old_letter.illustration.save()

            except Exception as e:
                self.stdout.write('Oops, some error: %s' % e)
                print 'name %s' % name
                print 'age %s' % age
                print 'occupation %s' % occupation
                print 'location %s' % location
                print 'slug %s' % slug

        self.stdout.write('Successfully finished importing letters')
