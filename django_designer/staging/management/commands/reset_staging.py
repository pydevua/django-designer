import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        db_file = settings.DATABASES['default']['NAME']
        if os.path.exists(db_file):
            os.unlink(db_file)
        call_command('syncdb', interactive=False)
        call_command('load_staging')
        