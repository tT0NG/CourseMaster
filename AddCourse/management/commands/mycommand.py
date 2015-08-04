from django.core.management.base import BaseCommand

from SyncCourseData.catchcourse import add_class


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_class()

