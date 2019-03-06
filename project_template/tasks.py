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
            position=verified_data['position']
        )

        politician.add_position(verified_data['position'])

        income_declaration, created = models.IncomeDeclaration.objects.get_or_create(
            url=self.url,
            politician=politician,
            date=verified_data['date']
        )


class TaskOwnedLandRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedLandSingleRowEntry
    template_name = "tasks/owned_land.html"

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

class TaskOwnedAutomobileRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedAutomobileSingleRowEntry
    template_name = "tasks/owned_automobile.html"
    
    def save_verified_data(self, verified_data):
        owned_automobile, created = models.OwnedAutomobileTableEntry.objects.get_or_create(
            car_type = verified_data['tip'],
            brand = verified_data['marca'],
            no_owned = verified_data['numar_bucati'],
            fabrication_year = verified_data['an_fabricatie'],
            attainment_type = verified_data['mod_dobandire'],
        )

class TaskOwnedDebtsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedDebtsSingleRowEntry
    template_name = "tasks/owned_debts.html"
        
    def save_verified_data(self, verified_data):
        if verified_data['nume_creditor'] and verified_data['prenume_creditor']:
            lender_identity = "Nume: {}, Prenume: {}".format(verified_data['nume_creditor'], verified_data['prenume_creditor'])
        else: 
            lender_identity = "Institutie: {}".format(verified_data['institutie'])
            
        owned_debts, created = models.OwnedDebtsTableEntry.objects.get_or_create(
                lender=lender_identity,
                debt_type = verified_data['tip_datorie'],
                acquirement_year = verified_data['an_contractare'],
                due_date = verified_data['scadenta'],
                value = verified_data['valoare'],
                currency = verified_data['moneda']
                )

class TaskOwnedIncomeFromPensionsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsSingleRowEntry
    template_name = "tasks/owned_income_from_pensions.html"
    
    def save_verified_data(self, verified_data):
        owned_income_from_pensions, created = models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
                income_provider_type = verified_data['beneficiar_pensie'],
                provider_name = "Nume:{}, Prenume:{}".format(verified_data['nume_beneficiar'], verified_data['prenume_beneficiar']),
                name_source_of_goods = verified_data['sursa_venit'],
                address_source_of_goods = "Judet: {}, Localitate: {}, Comuna: {}, Strainatate: {}".format(verified_data['judet'], verified_data['localitate'], verified_data['comuna'], verified_data['strainatate']),
                goods_name = verified_data['serviciu_prestat'],
                ex_position = verified_data['functie'],
                annual_income = verified_data['venit'],
                annual_income_currency = verified_data['moneda'])
    
@register()
class TaskOwnedGoodsOrServicesPerSpouse(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerSpouse
    storage_model = models.OwnedGoodsOrServicesPerSpouseTable
    # TODO - add child class
    child_class = None


@register()
class TaskTranscribeOwnedInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsTable
    storage_model = models.OwnedInvestmentsTable
    # TODO - add child_class
    child_class = None


@register()
class TaskTranscribeOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedJewelry(CountTableRowsTask):
    task_form = forms.TranscribeOwnedJewelry
    storage_model = models.OwnedJewelryTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedAutomobile(CountTableRowsTask):
    task_form = forms.TranscribeOwnedAutomobile
    storage_model = models.OwnedAutomobileTable
    child_class = TaskOwnedAutomobileRowEntry


@register()
class TaskTranscribeOwnedIncomeFromDeferredUseOfGoods(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoods
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    # TODO - add child_class
    child_class = None


@register()
class TaskTranscribeIndependentActivities(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivities
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    # TODO - add child_class
    child_class = None


@register()
class TaskGetDebtsTableRowsCount(CountTableRowsTask):
    task_form = forms.TranscribeDebtsTableRowsCount
    storage_model = models.OwnedDebtsTable
    child_class = TaskOwnedDebtsRowEntry


@register()
class TaskOwnedIncomeFromSalariesCount(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalaries
    storage_model = models.OwnedIncomeFromSalariesTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    child_class = TaskOwnedIncomeFromPensionsRowEntry


@register()
class TaskOwnedGoodsOrServicesPerChildTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerChildTable
    storage_model = models.OwnedGoodsOrServicesPerChildTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedGoodsOrServicesPerOwnerTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerOwnerTable
    storage_model = models.OwnedGoodsOrServicesPerOwnerTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedLandTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedLandTable
    storage_model = models.OwnedLandTable
    child_class = TaskOwnedLandRowEntry


@register()
class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    # TODO - add child_class
    child_class = None


@register()
class TaskOwnedBankAccountsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    storage_model = models.OwnedBankAccountsTable
    # TODO - add child_class
    child_class = None
