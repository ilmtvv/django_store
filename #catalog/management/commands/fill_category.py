from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categorys = [
            {"category_name": "qweqweqweqw"},
            {"category_description": "qweqweqweqweqwe"},
        ]
        Category.objects.all().delete()

        for category in categorys:
            Category.objects.create(**category)



