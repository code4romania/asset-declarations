import datetime

from moonsheep.tasks import AbstractTask
from moonsheep import verifiers

from .forms import *
from .models import *

from unittest.mock import MagicMock


class TaskWithForm(AbstractTask):
    task_form = SimpleForm
    template_name = 'task.html'

    def create_mocked_task(self, task_data):
        """
        Return some mocked task data to ease development.

        In normal conditions tasks will be created based on imported documents
        or as a child-tasks of tasks verified by users.

        :param task_data: Prepared default data to be updated
        :return:
        """

        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        """
        Choosing how to render document to transcribe.

        If defined overrides the default behaviour that choose document based on:
        1. Known url templates for YouTube, Vimeo, etc.
        2. Url file extension: .pdf, .png, etc.

        :return: {
            'template': 'presenters/fancy.html',
            'url': self.url,
            'other_presenter_option': 'width: 110px'
        }
        """
        return super(TaskWithForm, self).get_presenter()

    def save_verified_data(self, verified_data):
        """
        Inputs provided by volunteers has been cross-checked.
        Please save them here to your data model

        :param verified_data: data as provided in the form
        :return:
        """

        if verified_data.get('non_readable', False):
            # Checkboxes won't be passed if not specified so we need default above
            pass
        else:
            Document = MagicMock()  # quick hack, instead of defining it in models.py

            Document.objects.get_or_create(
                title=verified_data['title'],
            )

    def after_save(self, verified_data):
        """
        After cross-checking and saving task data you can create descendent tasks based on this one.

        For example, if document contains multiple entries you can:
        - ask in the parent task to list entries identifiers
        - create here as many child-tasks as there are entries
        - in child-task you ask to transribe specific entry details

        :param verified_data:
        :return:
        """
        self.create_new_task(TaskWithTemplate, {'page': 11})


class TaskWithTemplate(AbstractTask):
    template_name = 'tasks/with_template.html'

    # verify_title = verifiers.equals
    # verifiers = [verifiers.GeoProximity(10, "lat", "long")]

    def save_verified_data(self, verified_data):
        """
        Inputs provided by volunteers has been cross-checked.
        Please save them here to your data model

        :param verified_data: data as provided in the form
        :return:
        """

        Document = MagicMock()  # quick hack, instead of defining it in models.py

        Document.objects.get_or_create(
            title=verified_data['title'],
            publisher=verified_data['publisher'],
            pages_total=verified_data['pages_total']
        )
