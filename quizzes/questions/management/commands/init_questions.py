from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from questions.models import Question

class Command(BaseCommand):
    help = 'Create infrastructure for questions'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='questions_moderators')
        permission = Permission.objects.get(codename='add_question')
        group.permissions.add(permission)
        group.save()
