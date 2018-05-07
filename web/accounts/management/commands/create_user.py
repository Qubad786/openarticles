from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from web.accounts.models import User


class Command(BaseCommand):

    help = "Create Admin Accounts."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            user = User.objects.create_superuser(
                username='admin',
                gender='male',
                first_name='Site',
                last_name='Admin',
                role='editor',
                password='1234'
            )
            user.is_superuser = True
            user.save()
        except IntegrityError:
            self.stdout.write(self.style.WARNING(
                'A superuser with the same username="admin" is already there -- [SKIPPING]'
            ))

        self.stdout.write(
            self.style.SUCCESS("Super user has been setup successfully. Username: admin, password: 1234.")
        )