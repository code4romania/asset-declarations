import random
import datetime
from unittest.mock import MagicMock

from moonsheep.tasks import AbstractTask
from moonsheep import verifiers
from moonsheep.decorators import register

import project_template.models as models
import project_template.views
import project_template.forms as forms


@register()
class TaskGetInitialInformation(AbstractTask):
    task_form = forms.TranscribeInitialInformation
    template_name = 'tasks/general_information_task.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskGetInitialInformation, self).get_presenter()

    def save_verified_data(self, verified_data):
        print('[!] VERIFIED DATA: {}'.format(verified_data))
        politician, created = models.Politician.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )
        print("[!] FULL NAME: {}".format(politician.full_name))

    def after_save(self, verified_data):
        print("[!] YOU'RE DONE")
        # self.create_new_task(TaskWithTemplate, {'page': 11})


# @register()
class TaskToGetNumberOfTableRows(AbstractTask):
    task_form = forms.TranscribeNumberOfRowsPerTableForm
    template_name = 'num_of_rows_task.html'

    def create_mocked_task(self, task_data):

        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def save_verified_data(self, verified_data):
        print(verified_data)
        # self.create_new_task(TaskToGetNumberOfTableRows, {})

