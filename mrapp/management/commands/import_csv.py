import csv
from django.core.management.base import BaseCommand
from mrapp.models import Movie


class Command(BaseCommand):
    help = 'Import movie from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                year = row['Year']
                if year.isdigit():
                    year = int(year)
                else:
                    year = None
                movie = Movie(
                    Movie_Title=row['Movie_Title'],
                    Director=row['Director'],
                    Year=year,
                    Actors=row['Actors'],
                    Rating=row['Rating'],
                    Runtime=row['Runtime'],
                    Censor=row['Censor'],
                    Total_Gross=row['Total_Gross'],
                    main_genre=row['main_genre'],
                    side_genre=row['side_genre']
                )
                movie.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported'))