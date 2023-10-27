import json
import os.path

from django.core.management import BaseCommand
from blog.models import Post
from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'posts.json')

        with open(path) as f:
            file_content = f.read()
            posts_info = json.loads(file_content)
            posts_for_create = []
            for info in posts_info:
                posts_for_create.append(
                    Post(**info["fields"])
                )
            Post.objects.all().delete()
            Post.objects.bulk_create(posts_for_create)

