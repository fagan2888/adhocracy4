from django.core.management.base import BaseCommand

from adhocracy4.modules.models import Module


class Command(BaseCommand):
    help = 'Migrate single modules.'

    def handle(self, *args, **options):
        modules = Module.objects.all()
        for module in modules:
            module.name = 'Onlinebeteiligung'
            module.description = module.project.description
            module.save()
