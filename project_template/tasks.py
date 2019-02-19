import datetime
from moonsheep.tasks import AbstractTask
from moonsheep import verifiers
from moonsheep.decorators import register


import project_template.models as models
import project_template.views
import project_template.forms as forms


# @register()
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
            date=verified_data['date']
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        # self.create_new_task()
        pass


# @register()
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
            count = verified_data['count']
            )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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
        owned_investments_table, created = models.OwnedInvestmentsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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


# @register()
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
        owned_jewelry_table, created = models.OwnedJewelryTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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
        owned_automobile_table, created = models.OwnedAutomobileTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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


# @register()
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
        owned_income_from_independent_activities, created = models.OwnedIncomeFromIndependentActivities.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        pass


# @register()
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
        owned_income_from_gambling_table, created = models.OwnedIncomeFromGamblingTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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
        owned_income_from_agricultural_activities_table, created = models.OwnedIncomeFromAgriculturalActivitiesTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
class TaskGetDebtsTableRowsCount(AbstractTask):
    task_form = forms.TranscribeDebtsTableRowsCount
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskGetDebtsTableRowsCount, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_debts_table, created = models.OwnedDebtsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
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
        owned_income_from_salaries_table, created = models.OwnedIncomeFromSalariesTable.objects.get_or_create(
            count=verified_data['count']
        )

    def after_save(self, verified_data):
        pass


# @register()
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
        owned_income_from_pensions_table, created = models.OwnedIncomeFromPensionsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
class TaskOwnedGoodsOrServicesPerChildTable(AbstractTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerChildTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedGoodsOrServicesPerChildTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_goods_or_services_per_child_table, created = models.OwnedGoodsOrServicesPerChildTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
class TaskOwnedGoodsOrServicesPerOwnerTable(AbstractTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerOwnerTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedGoodsOrServicesPerOwnerTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_goods_or_services_per_owner_table, created = models.OwnedGoodsOrServicesPerOwnerTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


@register()
class TaskOwnedLandTable(AbstractTask):
    task_form = forms.TranscribeOwnedLandTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedLandTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_land_table, created = models.OwnedLandTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        number_rows = int(verified_data['count'])
        for row_number in list(range(1, number_rows)):
            self.create_new_task(TaskOwnedLandRowEntry, {'row_number': row_number})

    def create_new_task(self, task, info):
        info['type'] = ".".join([task.__module__, task.__name__])
        from moonsheep.register import base_task
        base_task.register(task)


# @register()
class TaskOwnedBuildingsTable(AbstractTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    template_name = 'tasks/owned_buildings_task.html'

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
            count=verified_data['count']
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
class TaskOwnedBankAccountsTable(AbstractTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    template_name = 'tasks/row_count_template.html'

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })

        return task_data

    def get_presenter(self):
        return super(TaskOwnedBankAccountsTable, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_bank_accounts, created = models.OwnedBankAccountsTable.objects.get_or_create(
            count=verified_data['count'],
        )

    def after_save(self, verified_data):
        # Create a new task for each table, asking the user to transcribe the number of rows
        pass


# @register()
class TaskOwnedLandRowEntry(AbstractTask):
    task_form = forms.TranscribeOwnedLandSingleRowEntry
    template_name = "tasks/owned_land.html"

    def create_mocked_task(self, task_data):
        task_data['info'].update({
            'url': 'http://www.cdep.ro/declaratii/deputati/2016/avere/002a.pdf',
            'page': 10
        })
        return task_data

    def get_presenter(self):
        return super(TaskOwnedLandRowEntry, self).get_presenter()

    def save_verified_data(self, verified_data):
        owned_land, created = models.OwnedLandTableEntry.objects.get_or_create(
            address="Judet: {}, Localitate: {}, Comuna: {}".format(verified_data['judet'], verified_data['localitate'], verified_data['comuna']),
            category=verified_data['categorie'],
            acquisition_year=verified_data['an_dobandire'],
            surface=verified_data['suprafata'],
            share_ratio=verified_data['cota_parte'],
            attainment_type=verified_data['mod_dobandire'],
            owner="{} {}".format(verified_data['nume_proprietar'], verified_data['prenume_proprietar']),
            observations=""
        )

    def after_save(self, verified_data):
        pass






