import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, Comment, Review
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        file_path = os.path.join(settings.BASE_DIR, 'static/data', 'users.csv')
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = User.objects.get_or_create(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6],
                )

        file_path = os.path.join(settings.BASE_DIR, 'static/data', 'genre.csv')
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Genre.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )

        file_path = os.path.join(
            settings.BASE_DIR,
            'static/data',
            'category.csv'
        )
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Category.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )

        file_path = os.path.join(
            settings.BASE_DIR,
            'static/data',
            'titles.csv'
        )
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Title.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category_id=row[3],
                )

        file_path = os.path.join(
            settings.BASE_DIR,
            'static/data',
            'genre_title.csv'
        )
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                Title.objects.get(id=row[1]).genre.add(
                    Genre.objects.get(id=row[2])
                )

        file_path = os.path.join(
            settings.BASE_DIR,
            'static/data',
            'review.csv'
        )
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Review.objects.get_or_create(
                    id=row[0],
                    title_id=row[1],
                    text=row[2],
                    author_id=row[3],
                    score=row[4],
                    pub_date=row[5],
                )

        file_path = os.path.join(
            settings.BASE_DIR,
            'static/data',
            'comments.csv'
        )
        with open(file_path, encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                _, created = Comment.objects.get_or_create(
                    id=row[0],
                    review_id=row[1],
                    text=row[2],
                    author_id=row[3],
                    pub_date=row[4],
                )
