from moonsheep.tasks import register_task

import project_template.models as models
import project_template.forms as forms
from project_template.task_templates import DigitalizationTask, CountTableRowsTask


class TaskGetInitialInformation(DigitalizationTask):
    task_form = forms.TranscribeInitialInformation
    template_name = 'tasks/general_information_task.html'

    def save_verified_data(self, verified_data):
        politician, created = models.Politician.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname'],
            initials=verified_data['initials'],
            previous_name=verified_data['previous_name']
        )

        politician.add_position(verified_data['position'])

        processed_declaration, created = models.Declaration.objects.get_or_create(
            politician=politician,
            date=verified_data['date'],
            position=verified_data['position'],
            institution=verified_data['institution'],
            declaration_type=verified_data['declaration_type']
        )


class TaskOwnedLandRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedLandRowEntry
    template_name = "tasks/owned_land.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('owner_name'),
            surname=verified_data.get('owner_surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['owner_name']
        del verified_data['owner_surname']

        owned_land, created = models.OwnedLandTableEntry.objects.get_or_create(
            coowner=owner_person,
            **verified_data,
        )


class TaskOwnedLandTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedLandTable
    storage_model = models.OwnedLandTable
    child_class = TaskOwnedLandRowEntry


class TaskOwnedAutomobileRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedAutomobileRowEntry
    template_name = "tasks/owned_automobile.html"

    def save_verified_data(self, verified_data):
        owned_automobile, created = models.OwnedAutomobileTableEntry.objects.get_or_create(
            **verified_data
        )


class TaskOwnedAutomobileTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedAutomobileTable
    storage_model = models.OwnedAutomobileTable
    child_class = TaskOwnedAutomobileRowEntry


class TaskOwnedBankAccountsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedBankAccountsRowEntry
    template_name = "tasks/owned_bank_accounts.html"

    def save_verified_data(self, verified_data):
        owned_bank_accounts, created = models.OwnedBankAccountsTableEntry.objects.get_or_create(
            **verified_data,
        )


class TaskOwnedBankAccountsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    storage_model = models.OwnedBankAccountsTable
    child_class = TaskOwnedBankAccountsRowEntry


class TaskOwnedIncomeFromAgriculturalActivitiesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry
    template_name = "tasks/agricultural_activity.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_income_from_agriculture, created = models.OwnedIncomeFromAgriculturalActivitiesTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data
        )


class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    child_class = TaskOwnedIncomeFromAgriculturalActivitiesRowEntry


class TaskOwnedDebtsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedDebtsRowEntry
    template_name = "tasks/owned_debts.html"

    def save_verified_data(self, verified_data):
        if verified_data.get('loaner_name') and verified_data.get('loaner_surname'):
            # Use the custom form fields
            loaner_person, created = models.Person.objects.get_or_create(
                name=verified_data.get('loaner_name'),
                surname=verified_data.get('loaner_surname')
            )

            # Remove the custom form fields before saving the table entry
            del verified_data['loaner_name']
            del verified_data['loaner_surname']

            owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                person=loaner_person,
                **verified_data,
            )
        elif verified_data.get('institution'):
            owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                **verified_data,
            )


class TaskOwnedDebtsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedDebtsTable
    storage_model = models.OwnedDebtsTable
    child_class = TaskOwnedDebtsRowEntry


class TaskOwnedIncomeFromPensionsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsRowEntry
    template_name = "tasks/owned_income_from_pensions.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('beneficiary_name'),
            surname=verified_data.get('beneficiary_surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['beneficiary_name']
        del verified_data['beneficiary_surname']

        owned_income_from_pensions, created = models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data,
        )

class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    child_class = TaskOwnedIncomeFromPensionsRowEntry


class TaskOwnedGoodsOrServicesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesRowEntry
    template_name = "tasks/owned_goods_or_services.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_goods_or_services, created = models.OwnedGoodsOrServicesTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data
        )


class TaskOwnedGoodsOrServicesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesTable
    storage_model = models.OwnedGoodsOrServicesTable
    child_class = TaskOwnedGoodsOrServicesRowEntry


class TaskOwnedInvestmentsOver5KRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KRowEntry
    template_name = "tasks/owned_investments_over_5k.html"

    def save_verified_data(self, verified_data):
        loan_beneficiary, created = models.Person.objects.get_or_create(
            name=verified_data.get('beneficiary_name'),
            surname=verified_data.get('beneficiary_surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['beneficiary_name']
        del verified_data['beneficiary_surname']

        owned_investments_over_5k, created = models.OwnedInvestmentsOver5KTableEntry.objects.get_or_create(
            loan_beneficiary=loan_beneficiary,
            **verified_data,
        )


class TaskOwnedInvestmentsOver5KTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KTable
    storage_model = models.OwnedInvestmentsOver5KTable
    child_class = TaskOwnedInvestmentsOver5KRowEntry


class TaskOwnedIncomeFromOtherSourcesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesRowEntry
    template_name = "tasks/owned_income_other_sources.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_income_other_sources, created = models.OwnedIncomeFromOtherSourcesTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data
        )

@register_task()
class TaskOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    child_class = TaskOwnedIncomeFromOtherSourcesRowEntry


class TaskOwnedJewelryRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedJewelryRowEntry
    template_name = "tasks/owned_jewelry.html"

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedJewelryTableEntry.objects.get_or_create(
            **verified_data
        )


class TaskOwnedJewelryTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedJewelryTable
    storage_model = models.OwnedJewelryTable
    child_class = TaskOwnedJewelryRowEntry


class TaskExtraValuableRowEntry(DigitalizationTask):
    task_form = forms.TranscribeExtraValuableRowEntry
    template_name = "tasks/owned_extra_valuable.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('owner_name'),
            surname=verified_data.get('owner_surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['owner_name']
        del verified_data['owner_surname']

        owned_extra_valuable, created = models.OwnedExtraValuableTableEntry.objects.get_or_create(
            receiver_of_goods=owner_person,
            **verified_data,
        )


class TaskExtraValuableTable(CountTableRowsTask):
    task_form = forms.TranscribeExtraValuableTable
    storage_model = models.OwnedExtraValuableTable
    child_class = TaskExtraValuableRowEntry


class TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsRowEntry
    template_name = "tasks/owned_income_from_deferred_use_of_goods.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_income_from_deferred_use, created = models.OwnedIncomeFromDeferredUseOfGoodsTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data,
        )


class TaskOwnedIncomeFromDeferredUseOfGoodsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsTable
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    child_class = TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry


class TaskOwnedIncomeFromIndependentActivitiesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeIndependentActivitiesRowEntry
    template_name = "tasks/owned_income_from_independent_activities.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_income_from_independent_activities, created = models.OwnedIncomeFromIndependentActivitiesTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data
        )


class TaskOwnedIncomeFromIndependentActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivitiesTable
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    child_class = TaskOwnedIncomeFromIndependentActivitiesRowEntry


class TaskOwnedIncomeFromGamblingRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingRowEntry
    template_name = "tasks/owned_income_from_gambling.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_income_from_gambling, created = models.OwnedIncomeFromGamblingTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data
        )


class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    child_class = TaskOwnedIncomeFromGamblingRowEntry


class TaskOwnedIncomeFromSalariesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromSalariesRowEntry
    template_name = "tasks/owned_income_from_salaries.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        owned_salaries, created = models.OwnedIncomeFromSalariesTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data,
        )


class TaskOwnedIncomeFromSalariesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalariesTable
    storage_model = models.OwnedIncomeFromSalariesTable
    child_class = TaskOwnedIncomeFromSalariesRowEntry


class TaskOwnedBuildingsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedBuildingsRowEntry
    template_name = "tasks/owned_buildings_task.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('owner_name'),
            surname=verified_data.get('owner_surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['owner_name']
        del verified_data['owner_surname']

        owned_buildings, created = models.OwnedBuildingsTableEntry.objects.get_or_create(
            coowner=owner_person,
            **verified_data,
        )


class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    child_class = TaskOwnedBuildingsRowEntry


class TaskOwnedIncomeFromInvestmentsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsRowEntry
    template_name = "tasks/owned_investments.html"

    def save_verified_data(self, verified_data):
        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get('name'),
            surname=verified_data.get('surname')
        )

        # Remove the custom form fields before saving the table entry
        del verified_data['name']
        del verified_data['surname']

        income_from_investments, created = models.OwnedIncomeFromInvestmentsTableEntry.objects.get_or_create(
            person=owner_person,
            **verified_data,
        )


class TaskOwnedIncomeFromInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsTable
    storage_model = models.OwnedIncomeFromInvestmentsTable
    child_class = TaskOwnedIncomeFromInvestmentsRowEntry
