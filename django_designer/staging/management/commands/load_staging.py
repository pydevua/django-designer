from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.db.transaction import commit_on_success


class Command(BaseCommand):

    @commit_on_success
    def handle(self, *args, **kwargs):
        #NOTE: in order to avoid conflicts with other fixtures
        #      all fixtures in staging should starts with "staging_" prefix
        options = kwargs.get('options', {})
        call_command('loaddata', 'staging_admin', **options)
