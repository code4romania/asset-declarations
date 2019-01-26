import random
import datetime
from unittest.mock import MagicMock

from moonsheep.tasks import AbstractTask
from moonsheep import verifiers
from moonsheep.decorators import register


import project_template.models as models
import project_template.views
import project_template.forms as forms


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
        politician, created = models.Politician.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname'],
            position=verified_data['position']
        )

        politician.add_position(verified_data['position'])

        income_declaration, created = models.IncomeDeclaration.objects.get_or_create(
            url=self.url,
            politician=politician,
            date=datetime.datetime.strptime(verified_data['date'], "%Y-%m-%d")
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedGoodsOrServicesPerSpouse(AbstractTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerSpouse
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedGoodsOrServicesPerSpouse, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_goods_or_services_per_spouse, created = models.OwnedGoodsOrServicesPerSpouseTable.objects.get_or_create(
            count=verified_data['count']
            )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskTranscribeOwnedInvestmentsTable(AbstractTask):
    task_form = forms.TranscribeOwnedInvestmentsTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskTranscribeOwnedInvestmentsTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_income_from_other_sources_table, created = models.OwnedInvestmentsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskTranscribeOwnedIncomeFromOtherSourcesTable(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskTranscribeOwnedIncomeFromOtherSourcesTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_income_from_other_sources_table, created = models.OwnedIncomeFromOtherSourcesTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedJewelry(AbstractTask):
    task_form = forms.TranscribeOwnedJewelry
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedJewelry, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedJewelryTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedAutomobile(AbstractTask):
    task_form = forms.TranscribeOwnedAutomobile
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedAutomobile, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedAutomobileTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskTranscribeOwnedIncomeFromDeferredUseOfGoods(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoods
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskTranscribeOwnedIncomeFromDeferredUseOfGoods, self).get_presenter()

    def save_verified_data(self, verified_data):
        count, created = models.OwnedIncomeFromDeferredUseOfGoodsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        pass


class TaskTranscribeIndependentActivities(AbstractTask):
    task_form = forms.TranscribeIndependentActivities
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskTranscribeIndependentActivities, self).get_presenter()

    def save_verified_data(self, verified_data):
        count, created = models.OwnedIncomeFromIndependentActivities.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        pass


class TaskOwnedIncomeFromGamblingTable(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedIncomeFromGamblingTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedIncomeFromGamblingTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass



class TaskOwnedIncomeFromAgriculturalActivitiesTable(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedIncomeFromAgriculturalActivitiesTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedIncomeFromAgriculturalActivitiesTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskGetDebtsTableRowsCount(AbstractTask):
    task_form = forms.TranscribeDebtsTableRowsCount
    template_name = 'tasks/debts_table_rows_count_task.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskGetDebtsTableRowsCount, self).get_presenter()

    def save_verified_data(self, verified_data):
        try:
            rows_count = verified_data['rows_count']
            models.OwnedDebtsTable.objects.get_or_create(count=rows_count)
        except Exception as error:
            print("Exception: ", error)

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedIncomeFromSalariesCount(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromSalaries
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedIncomeFromSalariesCount, self).get_presenter()

    def save_verified_data(self, verified_data):
        count, created = models.OwnedIncomeFromSalariesTable.objects.get_or_create(
            count=verified_data['count']
        )

    def after_save(self, verified_data):
        pass


class TaskOwnedIncomeFromPensionsTable(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedIncomeFromPensionsTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedIncomeFromPensionsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedIncomeFromInvestmentsTable(AbstractTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedIncomeFromInvestmentsTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedIncomeFromInvestmentsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


class TaskOwnedBuildingsTable(AbstractTask):
    task_form = forms.OwnedBuildings
    template_name = 'tasks/owned_buildings_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedBuildingsTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_building, created = models.OwnedBuildingsTable.objects.get_or_create(
            address=verified_data['adress'],
            category=verified_data['category'],
            attainment_year=verified_data['attainment_year'],
            surface=verified_data['surface'],
            share=verified_data['share'],
            attainment_type=verified_data['attainment_type'],
            holder=verified_data['holder']
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass
