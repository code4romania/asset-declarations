import datetime

from moonsheep import verifiers
from moonsheep.decorators import register

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
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['owner_name'],
            surname=verified_data['owner_surname']
        )

        owned_land, created = models.OwnedLandTableEntry.objects.get_or_create(
            coowner=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            category=verified_data['real_estate_type'],
            acquisition_year=verified_data['ownership_start_year'],
            surface=verified_data['surface_area'],
            share_ratio=verified_data['percent_of_ownership'],
            taxable_value=verified_data['taxable_value'],
            taxable_value_currency=verified_data['taxable_value_currency'],
            attainment_type=verified_data['attainment_type'],
            observations=verified_data.get('observations', '')
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
            goods_type=verified_data['automobile_type'],
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
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        income_declaration, created = models.OwnedIncomeFromAgriculturalActivitiesTableEntry.objects.get_or_create(
            person=owner_person,
            source_of_goods=verified_data['source'],
            holder_relationship=verified_data['holder_relationship'],
            holder_type=verified_data['holder_type'],
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            service=verified_data['offered_service'],
            annual_income=verified_data['income_amount'],
            currency=verified_data['currency']
        )


class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    child_class = TaskOwnedIncomeFromAgriculturalActivitiesRowEntry


class TaskOwnedDebtsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedDebtsRowEntry
    template_name = "tasks/owned_debts.html"

    def save_verified_data(self, verified_data):
        if verified_data['loaner_name'] and verified_data['loaner_surname']:
            loaner_person, created = models.Person.objects.get_or_create(
                name=verified_data['loaner_name'],
                surname=verified_data['loaner_surname']
            )
            owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                person=loaner_person,
                debt_type=verified_data['type_of_debt'],
                acquirement_year=verified_data['loan_start_year'],
                due_date=verified_data['loan_maturity'],
                value=verified_data['loan_amount'],
                currency=verified_data['currency']
            )
        elif verified_data['institution']:
            owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                lender=verified_data['institution'],
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
    task_form = forms.TranscribeOwnedIncomeFromPensionsRowEntry
    template_name = "tasks/owned_income_from_pensions.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            surname=verified_data['beneficiary_surname'],
            name=verified_data['beneficiary_name']
        )

        owned_income_from_pensions, created = models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
            person=owner_person,
            holder_relationship=verified_data['beneficiary_relationship'],
            source_of_goods=verified_data['income_source'],
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            service=verified_data['offered_service'],
            ex_position=verified_data['position'],
            annual_income=verified_data['income_amount'],
            currency=verified_data['currency'])


class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    child_class = TaskOwnedIncomeFromPensionsRowEntry


class TaskOwnedGoodsOrServicesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesRowEntry
    template_name = "tasks/owned_goods_or_services.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_goods_or_services, created = models.OwnedGoodsOrServicesTableEntry.objects.get_or_create(
            person=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            address=verified_data['address'],
            holder_relationship=verified_data['holder_relationship'],
            source_of_goods=verified_data['source_of_goods'],
            service=verified_data['service'],
            annual_income=verified_data['annual_income'],
            currency=verified_data['currency'],
        )


class TaskOwnedGoodsOrServicesPerSpouseTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesTable
    storage_model = models.OwnedGoodsOrServicesTable
    child_class = TaskOwnedGoodsOrServicesRowEntry


class TaskOwnedInvestmentsOver5KRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KRowEntry
    template_name = "tasks/owned_investments_over_5k.html"

    def save_verified_data(self, verified_data):
        loan_beneficiary, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_investments_over_5k, created = models.OwnedInvestmentsOver5KTableEntry.objects.get_or_create(
            loan_beneficiary=loan_beneficiary,
            issue_title=verified_data['issue_title'],
            shareholder_society=verified_data['shareholder_society'],
            type_of_investment=verified_data['type_of_investment'],
            number_of_stocks=verified_data['number_of_stocks'],
            share_ratio=verified_data['share_ratio'],
            total_value=verified_data['total_value'],
            currency=verified_data['currency']
        )


class TaskOwnedInvestmentsOver5KTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KTable
    storage_model = models.OwnedInvestmentsOver5KTable
    child_class = TaskOwnedInvestmentsOver5KRowEntry


class TaskOwnedIncomeFromOtherSourcesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesRowEntry
    template_name = "tasks/owned_income_other_sources.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_income_other_sources, created = models.OwnedIncomeFromOtherSourcesTableEntry.objects.get_or_create(
            person=owner_person,
            holder_relationship=verified_data['holder_relationship'],
            source_of_goods=verified_data['source_of_goods'],
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            address=verified_data['address'],
            service=verified_data['service'],
            annual_income=verified_data['annual_income'],
            currency=verified_data['currency'],
            )


class TaskOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    child_class = TaskOwnedIncomeFromOtherSourcesRowEntry


class TaskOwnedJewelryRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedJewelryRowEntry
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
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['owner_name'],
            surname=verified_data['owner_surname']
        )

        owned_extra_valuable, created = models.OwnedExtraValuableTableEntry.objects.get_or_create(
            receiver_of_goods=owner_person,
            estrangement_goods_type=verified_data['estrangement_goods_type'],
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            estrangement_date=verified_data['estranged_date'],
            goods_separation_type=verified_data['goods_separation_type'],
            value=verified_data['estimated_value'],
            currency=verified_data['currency']
        )


class TaskExtraValuableTable(CountTableRowsTask):
    task_form = forms.TranscribeExtraValuable
    storage_model = models.OwnedExtraValuableTable
    child_class = TaskExtraValuableRowEntry


class TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsRowEntry
    template_name = "tasks/owned_income_from_deferred_use_of_goods.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_income_from_deferred_use, created = models.OwnedIncomeFromDeferredUseOfGoodsTableEntry.objects.get_or_create(
            person=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            address=verified_data['address'],
            holder_relationship=verified_data['holder_relationship'],
            source_of_goods=verified_data['source_of_goods'],
            service=verified_data['service'],
            annual_income=verified_data['annual_income'],
            currency=verified_data['currency'],
        )


class TaskOwnedIncomeFromDeferredUseOfGoodsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsTable
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    child_class = TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry


class TaskOwnedIncomeFromIndependentActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivities
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    # TODO - add child_class
    child_class = None


class TaskOwnedIncomeFromGamblingRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingRowEntry
    template_name = "tasks/owned_income_from_gambling.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_income_from_gambling, created = models.OwnedIncomeFromGamblingTableEntry.objects.get_or_create(
            person=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            address=verified_data['address'],
            holder_relationship=verified_data['holder_relationship'],
            source_of_goods=verified_data['source_of_goods'],
            service=verified_data['service'],
            annual_income=verified_data['annual_income'],
            currency=verified_data['currency'],
        )


class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    child_class = TaskOwnedIncomeFromGamblingRowEntry


class TaskOwnedIncomeFromSalariesRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromSalariesRowEntry
    template_name = "tasks/owned_income_from_salaries.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        owned_salaries, created = models.OwnedIncomeFromSalariesTableEntry.objects.get_or_create(
            person=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            address=verified_data['address'],
            holder_relationship=verified_data['holder_relationship'],
            source_of_goods=verified_data['source_of_goods'],
            service=verified_data['service'],
            annual_income=verified_data['annual_income'],
            currency=verified_data['currency'],
        )


class TaskOwnedIncomeFromSalariesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalaries
    storage_model = models.OwnedIncomeFromSalariesTable
    child_class = TaskOwnedIncomeFromSalariesRowEntry


class TaskOwnedBuildingsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedBuildingsTableRowEntry
    template_name = "tasks/owned_buildings_task.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['owner_name'],
            surname=verified_data['owner_surname']
        )

        owned_buildings, created = models.OwnedBuildingsTableEntry.objects.get_or_create(
            coowner=owner_person,
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            category=verified_data['building_type'],
            acquisition_year=verified_data['ownership_start_year'],
            surface=verified_data['surface_area'],
            share_ratio=verified_data['percent_of_ownership'],
            taxable_value=verified_data['taxable_value'],
            taxable_value_currency=verified_data['taxable_value_currency'],
            attainment_type=verified_data['attainment_type'],
            observations=verified_data.get('observations', '')
        )


class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    child_class = TaskOwnedBuildingsRowEntry


class TaskOwnedIncomeFromInvestmentsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsRowEntry
    template_name = "tasks/owned_investments.html"

    def save_verified_data(self, verified_data):
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname']
        )

        income_declaration, created = models.OwnedIncomeFromInvestmentsTableEntry.objects.get_or_create(
            person=owner_person,
            holder_relationship=verified_data['holder_relationship'],
            county=verified_data['county'],
            city=verified_data['city'],
            commune=verified_data['commune'],
            service=verified_data['service'],
            source_of_goods=verified_data['source_of_goods'],
            annual_income=verified_data['income_amount'],
            currency=verified_data['currency']
        )


@register()
class TaskOwnedIncomeFromInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsTable
    storage_model = models.OwnedIncomeFromInvestmentsTable
    child_class = TaskOwnedIncomeFromInvestmentsRowEntry
