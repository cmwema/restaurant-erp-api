from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create user groups'

    def handle(self, *args, **options):
        # Define the group names
        group_names = ['manager', 'customer', 'staff']

        # Create groups
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Group '{group_name}' already exists."))

        self.stdout.write(self.style.SUCCESS("User groups creation completed."))
