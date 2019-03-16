import datetime

from moonsheep import verifiers
from moonsheep.decorators import register

import project_template.models as models
import project_template.forms as forms
from project_template.task_templates import DigitalizationTask, CountTableRowsTask


@register()
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
    task_form = forms.TranscribeOwnedLandSingleRowEntry
    template_name = "tasks/owned_land.html"

    def save_verified_data(self, verified_data):
        owned_land, created = models.OwnedLandTableEntry.objects.get_or_create(
            address="Judet: {}, Localitate: {}, Comuna: {}".format(verified_data['county'], verified_data['city'], verified_data['commune']),
            category=verified_data['real_estate_type'],
            acquisition_year=verified_data['ownership_start_year'],
            attainment_type=verified_data['attainment_type'],
            surface=verified_data['surface_area'],
            share_ratio=verified_data['percent_of_ownership'],
            owner="{} {}".format(verified_data['owner_surname'], verified_data['owner_name']),
            observations=verified_data.get('observations', '')
        )


class TaskOwnedLandTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedLandTable
    storage_model = models.OwnedLandTable
    child_class = TaskOwnedLandRowEntry


class TaskOwnedAutomobileRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedAutomobileSingleRowEntry
    template_name = "tasks/owned_automobile.html"

    def save_verified_data(self, verified_data):
        owned_automobile, created = models.OwnedAutomobileTableEntry.objects.get_or_create(
            car_type=verified_data['type'],
            brand=verified_data['manufacturer'],
            no_owned=verified_data['num_of_automobiles'],
            fabrication_year=verified_data['year_of_manufacture'],
            attainment_type=verified_data['attainment_type'],
        )


class TaskOwnedAutomobileTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedAutomobile
    storage_model = models.OwnedAutomobileTable
    child_class = TaskOwnedAutomobileRowEntry


class TaskOwnedBankAccountsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedBankAccountsRowEntry
    template_name = "tasks/owned_bank_accounts.html"

    def save_verified_data(self, verified_data):
        owned_bank_accounts, created = models.OwnedBankAccountsTableEntry.objects.get_or_create(
            institution=verified_data['financial_institution'],
            account_type=verified_data['account_type'],
            currency=verified_data['currency'],
            opening_year=verified_data['account_start_date'],
            account_balance=verified_data['balance'],
        )


class TaskOwnedBankAccountsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    storage_model = models.OwnedBankAccountsTable
    child_class = TaskOwnedBankAccountsRowEntry


class TaskOwnedIncomeFromAgriculturalActivitiesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry
    template_name = "tasks/agricultural_activity.html"

    def save_verified_data(self, verified_data):
        # Check if option is person or institution
        optiune=int(verified_data['optiune'])

        income_declaration, created = models.OwnedIncomeFromAgriculturalActivitiesTableEntry.objects.get_or_create(
            name_source_of_goods=verified_data['sursa'],
            holder_relationship=verified_data['relatie_titular'],
            address_source_of_goods="Judet: {}, Localitate: {}, Comuna: {}".format(verified_data['county'], verified_data['city'], verified_data['commune']),
            goods_name=verified_data['offered_service'],
            annual_income=verified_data['income_amount'],
            annual_income_currency=verified_data['currency']
        )


class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    child_class = TaskOwnedIncomeFromAgriculturalActivitiesRowEntry


class TaskOwnedDebtsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedDebtsSingleRowEntry
    template_name = "tasks/owned_debts.html"

    def save_verified_data(self, verified_data):
        if verified_data['nume_creditor'] and verified_data['prenume_creditor']:
            lender_identity = "Nume: {}, Prenume: {}".format(verified_data['loaner_surname'], verified_data['loaner_name'])
        else:
            lender_identity = "Institutie: {}".format(verified_data['institution'])

        owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                lender=lender_identity,
                debt_type=verified_data['type_of_debt'],
                acquirement_year=verified_data['loan_start_year'],
                due_date=verified_data['loan_maturity'],
                value=verified_data['loan_amount'],
                currency=verified_data['currency']
                )


class TaskOwnedDebtsTable(CountTableRowsTask):
    task_form = forms.TranscribeDebtsTableRowsCount
    storage_model = models.OwnedDebtsTable
    child_class = TaskOwnedDebtsRowEntry


class TaskOwnedIncomeFromPensionsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsSingleRowEntry
    template_name = "tasks/owned_income_from_pensions.html"

    def save_verified_data(self, verified_data):
        owned_income_from_pensions, created = models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
            income_provider_type=verified_data['beneficiary_relationship'],
            provider_name="Nume:{}, Prenume:{}".format(verified_data['beneficiary_surname'], verified_data['beneficiary_name']),
            name_source_of_goods=verified_data['income_source'],
            address_source_of_goods="Judet: {}, Localitate: {}, Comuna: {}, Strainatate: {}".format(verified_data['county'], verified_data['city'], verified_data['commune'], verified_data['country']),
            goods_name=verified_data['offered_service'],
            ex_position=verified_data['position'],
            annual_income=verified_data['income_amount'],
            annual_income_currency=verified_data['currency'])


class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    child_class = TaskOwnedIncomeFromPensionsRowEntry


class TaskOwnedGoodsOrServicesPerSpouseRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerSpouseRowEntry
    template_name = "tasks/owned_gifts_spouse.html"

    def save_verified_data(self, verified_data):
        owned_gifts_spouse, created = models.OwnedGoodsOrServicesPerSpouseTableEntry.objects.get_or_create(
            holder="Nume: {0}, Prenume: {1}".format(
                verified_data['holder_surname'],
                verified_data['holder_name']
            ),
            name_source_of_goods=verified_data['income_source'],
            address_source_of_goods="Judet: {}, Localitate: {}, Comuna: {}"
            .format(
                verified_data['county'],
                verified_data['city'],
                verified_data['commune']
            ),
            goods_name=verified_data['goods_name'],
            annual_income=verified_data['annual_income'],
            annual_income_currency=verified_data['currency']
        )


class TaskOwnedGoodsOrServicesPerSpouseTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerSpouse
    storage_model = models.OwnedGoodsOrServicesPerSpouseTable
    child_class = TaskOwnedGoodsOrServicesPerSpouseRowEntry


class TaskTranscribeOwnedInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsTable
    storage_model = models.OwnedInvestmentsTable
    # TODO - add child_class
    child_class = None


class TaskTranscribeOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    # TODO - add child_class
    child_class = None


class TaskOwnedJewelryRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedJewelrySingleRowEntry
    template_name = "tasks/owned_jewelry.html"

    def save_verified_data(self, verified_data):
        owned_jewelry, created = models.OwnedJewelryTableEntry.objects.get_or_create(
            summary_description=verified_data['description'],
            acquisition_year=verified_data['ownership_start_year'],
            goods_value=verified_data['estimated_value'],
            currency=verified_data['currency'])


class TaskOwnedJewelryTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedJewelry
    storage_model = models.OwnedJewelryTable
    child_class = TaskOwnedJewelryRowEntry


class TaskExtraValuableRowEntry(DigitalizationTask):
    task_form = forms.TranscribeExtraValuableRowEntry
    template_name = "tasks/owned_extra_valuable.html"

    def save_verified_data(self, verified_data):
        owned_extra_valuable, created = models.OwnedExtraValuableTableEntry.objects.get_or_create(
            estrangement_goods_type=verified_data['estranged_goods_type'],
            estragement_goods_address="{}, {}, {}".format(verified_data['goods_county'], verified_data['goods_town'], verified_data['goods_commune']),
            estrangement_date=verified_data['estranged_date'],
            receiver_of_goods="{} {}".format(verified_data['owner_name'], verified_data['owner_surname']),
            goods_separation_type=verified_data['estranged_goods_separation'],
            value=verified_data['estimated_value'],
            currency=verified_data['currency']
        )


class TaskExtraValuableTable(CountTableRowsTask):
    task_form = forms.TranscribeExtraValuable
    storage_model = models.OwnedExtraValuableTable
    child_class = TaskExtraValuableRowEntry


class TaskOwnedIncomeFromDeferredUseOfGoodsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoods
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    # TODO - add child_class
    child_class = None


class TaskOwnedIncomeFromIndependentActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivities
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    # TODO - add child_class
    child_class = None


class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    # TODO - add child_class
    child_class = None


class TaskOwnedIncomeFromSalariesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalaries
    storage_model = models.OwnedIncomeFromSalariesTable
    # TODO - add child_class
    child_class = None


class TaskOwnedGoodsOrServicesPerChildTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerChildTable
    storage_model = models.OwnedGoodsOrServicesPerChildTable
    # TODO - add child_class
    child_class = None


class TaskOwnedGoodsOrServicesPerOwnerTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerOwnerTable
    storage_model = models.OwnedGoodsOrServicesPerOwnerTable
    # TODO - add child_class
    child_class = None


class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    # TODO - add child_class
    child_class = None
