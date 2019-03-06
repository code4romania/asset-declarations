import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from project_template import constants
from project_template.datamodels.debt_type import DebtType
from project_template.datamodels.holder_relationship import HolderRelationship
from project_template.datamodels.institution import Institution
from project_template.datamodels.position import Position
from project_template.datamodels.attainment_type import AttainmentType

from project_template.datamodels.mobile_goods_type import MobileGoodsType
from project_template.datamodels.financial_institution import FinancialInstitution
from project_template.datamodels.currency import Currency
from project_template.datamodels.debt_type import DebtType
from project_template.datamodels.income_provider_type import IncomeProviderType
from project_template.datamodels.position import Position
from project_template.datamodels.account_type import AccountType
from project_template.datamodels.counties import Counties
from project_template.datamodels.real_estate_type import RealEstateType


start_date = 1989
end_date = datetime.datetime.now().year
YEAR_CHOICES = tuple(map(str, range(start_date, end_date + 1)))
FIRST_2_TYPES = 2


class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(label=_("Care este prenumele politicianului?"))
    surname = forms.CharField(label=_("Care este numele politicianului?"))
    position = forms.CharField(label=_("Care este pozitia politicianului?"))
    date = forms.DateField(label=_("Care este data completării declarției de avere?"), widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])


class TranscribeDebtsTableRowsCount(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['debts']))


class TranscribeOwnedGoodsOrServicesPerSpouse(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['gifts_spouse']))


class TranscribeOwnedIncomeFromOtherSourcesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['other_sources']))


class TranscribeOwnedInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['bank_accounts']))


class TranscribeOwnedJewelry(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['jewelry']))


class TranscribeOwnedAutomobile(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['automobiles']))


class TranscribeOwnedIncomeFromSalaries(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['salaries']))


class TranscribeOwnedIncomeFromGamblingTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['gambling']))


class TranscribeOwnedIncomeFromAgriculturalActivitiesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['agriculture']))


class TranscribeIndependentActivities(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['independent_activities']))


class TranscribeOwnedIncomeFromDeferredUseOfGoods(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['deferred_use']))


class TranscribeOwnedIncomeFromPensionsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['pensions']))


class TranscribeOwnedIncomeFromInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['income_investments']))


class TranscribeOwnedGoodsOrServicesPerChildTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['gifts_kids']))


class TranscribeOwnedGoodsOrServicesPerOwnerTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['goods']))


class TranscribeOwnedLandTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['land']))


class TranscribeOwnedBuildingsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}".format(constants.DECLARATION_TABLES['buildings']))


class TranscribeOwnedBankAccountsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['bank_accounts']))


class TranscribeOwnedLandSingleRowEntry(forms.Form):
    county = forms.ChoiceField(label="Care este judetul in care se gaseste terenul detinut?", choices=Counties.return_counties())
    city = forms.CharField(label="Care este localitatea in care se gaseste terenul detinut?")
    commune = forms.CharField(label="Care este comuna in care se gaseste terenul detinut?")
    real_estate_type = forms.ChoiceField(label="Care este categoria de teren?", choices=RealEstateType.return_as_iterable())
    ownership_start_year = forms.DateField(label="Care este anul cand terenul a fost dobandit?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    attainment_type = forms.ChoiceField(label="Care este modul in care terenul a fost dobandit?", choices=AttainmentType.return_as_iterable())
    surface_area = forms.CharField(label="Care este suprafata terenului? (mp)")
    percent_of_ownership = forms.IntegerField(label="Care este cota parte din acest teren? (in procente)", max_value=100, min_value=0)
    owner_surname = forms.CharField(label="Care este numele proprietarului?")
    owner_name = forms.CharField(label="Care este prenumele proprietarului")


class TranscribeOwnedAutomobileSingleRowEntry(forms.Form):
    type = forms.CharField(label="Care este tipul autovehiculului?", widget=forms.Select(choices=MobileGoodsType.return_as_iterable()))
    manufacturer = forms.CharField(label="Care este marca autovehiculului?")
    num_of_automobiles = forms.IntegerField(label="Care este numarul de autovehicule detinute?")
    year_of_manufacture = forms.DateField(label="Care este anul de fabricatie al autovehiculului?")
    attainment_type = forms.CharField(label="Care este modul in care a fost dobandit autovehiculul?", widget=forms.Select(choices=AttainmentType.return_as_iterable()))


class TranscribeOwnedDebtsSingleRowEntry(forms.Form):
    loaner_surname = forms.CharField(label="Care este numele creditorului?")
    loaner_name = forms.CharField(label="Care este prenumele creditorului?")
    institution = forms.CharField(label="Care este numele institutiei creditoare?", widget=forms.Select(choices=FinancialInstitution.return_as_iterable()))
    type_of_debt = forms.CharField(label="Care este tipul de datorie?", widget=forms.Select(choices=DebtType.return_as_iterable()))
    loan_start_year = forms.DateField(label="Care este anul contractarii imprumutului?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    loan_maturity = forms.DateField(label="Care este data scadentei?", widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    loan_amount = forms.IntegerField(label="Care este valoarea imprumutului?")
    currency = forms.ChoiceField(label="Care este moneda in care s-a facut imprumutul?", choices=Currency.return_as_iterable())


class TranscribeOwnedIncomeFromPensionsSingleRowEntry(forms.Form):
    beneficiary_relationship = forms.CharField(label="Cine este beneficiarul pensiei?", widget=forms.Select(choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES]))
    beneficiary_surname = forms.CharField(label="Care este numele beneficiarului?")
    beneficiary_name = forms.CharField(label="Care este prenumele beneficiarului?")
    income_source = forms.CharField(label="Care este numele sursei de venit?")
    county = forms.CharField(label="Care este judetul de unde provine sursa de venit?")
    city = forms.CharField(label="Care este localitatea de unde provine sursa de venit?")
    commune = forms.CharField(label="Care este comuna de unde provine sursa de venit?")
    country = forms.CharField(label="Care este tara din care provine sursa de venit?")
    offered_service = forms.CharField(label="Care a fost serviciul prestat?")
    position = forms.ChoiceField(label="Care a fost functia detinuta?", choices=Position.return_as_iterable())
    income_amount = forms.IntegerField(label="Care este valoarea venitului?")
    currency = forms.ChoiceField(label="Care este moneda venitului?", choices=Currency.return_as_iterable())


class TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry(forms.Form):
    holder_relationship = forms.ChoiceField(label="Cine este beneficiarul venitului din activități agricole?", choices=HolderRelationship.return_as_iterable())
    holder_type = forms.ChoiceField(label="Optiune", choices=[(0, "Insitutie"), (1, "Persoana")], widget=forms.RadioSelect)
    surname = forms.CharField(label="Care e numele persoanei?")
    name = forms.CharField(label="Care e prenumele persoanei?")
    source = forms.CharField(label="Care este sursa?")
    county = forms.CharField(label="Care este judetul in care se gaseste terenul detinut?")
    city = forms.CharField(label="Care este localitatea in care se gaseste terenul detinut?")
    commune = forms.CharField(label="Care este comuna in care se gaseste terenul detinut?")
    # TODO - identify the reason for the form field below
    # foreign_residence_address = forms.CharField(label="Adresa strainatate?")
    offered_service = forms.CharField(label="Care e serviciul prestat?")
    position = forms.ChoiceField(label="Care e poziția?", choices=Position.return_as_iterable())
    income_amount = forms.IntegerField(label="Care este venitul anual incasat?", min_value=0)
    currency = forms.ChoiceField(label="Care este moneda venitului?", choices=Currency.return_as_iterable())


class TranscribeOwnedBankAccountsRowEntry(forms.Form):
    financial_institution = forms.ChoiceField(label="Care este institutia financiara?", choices=FinancialInstitution.return_as_iterable())
    account_type = forms.ChoiceField(label="Care este tipul contului?", choices=AccountType.return_as_iterable())
    currency = forms.ChoiceField(label="Care este valuta?", choices=Currency.return_as_iterable())
    account_start_date = forms.DateField(label="Care este anul deschiderii contului?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    balance = forms.DecimalField(label="Care este valoarea soldului?", decimal_places=2, max_digits=10)

