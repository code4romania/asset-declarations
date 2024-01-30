from django.core.management.base import BaseCommand

from moonsheep.models import Task
from moonsheep.settings import MOONSHEEP

from project_template.models import Declaration


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for url in [
            "http://cdep.ro/declaratii/deputati/2016/avere/002a.pdf",
            "http://cdep.ro/declaratii/deputati/2016/avere/003c.pdf",
            "http://cdep.ro/declaratii/deputati/2016/avere/004e.pdf",
            "http://cdep.ro/declaratii/deputati/2016/avere/005c.pdf",
            "http://cdep.ro/declaratii/deputati/2016/avere/006d.pdf",
        ]:
            declaration, _ = Declaration.objects.get_or_create(url=url)

            for task_type in MOONSHEEP["DOCUMENT_INITIAL_TASKS"]:
                Task.objects.get_or_create(type=task_type, doc_id=declaration.id, params={"url": url,})
