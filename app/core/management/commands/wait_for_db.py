"""
Django comand to wait for DB
"""
import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db connection"""

    def handle(self, *args, **options):
        """Entrypoint for commands"""
        self.stdout.write("waiting for response")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
            except(Psycopg2OperationalError, OperationalError):
                self.stdout.write('Database not ready, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCESS('darabase is ready...'))
