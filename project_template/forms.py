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

import datetime
start_date = 2008
end_date = datetime.datetime.now().year
YEAR_CHOICES = tuple(map(str, range(start_date, end_date + 1)))
FIRST_2_TYPES = 2

class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(label=_("What is the name of the current politician?"))
    surname = forms.CharField(label=_("What is the surname of the current politician?"))
    position = forms.CharField(label=_("What is the position of the current politician?"))
    date = forms.DateField(label=_("Date"), widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])


class TranscribeDebtsTableRowsCount(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['debts']))


class TranscribeOwnedGoodsOrServicesPerSpouse(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gifts_spouse']))


class TranscribeOwnedIncomeFromOtherSourcesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['other_sources']))


class TranscribeOwnedInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['bank_accounts']))


class TranscribeOwnedJewelry(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['jewelry']))


class TranscribeOwnedAutomobile(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['automobiles']))


class TranscribeOwnedIncomeFromSalaries(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['salaries']))


class TranscribeOwnedIncomeFromGamblingTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gambling']))


class TranscribeOwnedIncomeFromAgriculturalActivitiesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['agriculture']))


class TranscribeIndependentActivities(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['independent_activities']))


class TranscribeOwnedIncomeFromDeferredUseOfGoods(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['deferred_use']))


class TranscribeOwnedIncomeFromPensionsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['pensions']))


class TranscribeOwnedIncomeFromInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['income_investments']))


class TranscribeOwnedGoodsOrServicesPerChildTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gifts_kids']))


class TranscribeOwnedGoodsOrServicesPerOwnerTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['goods']))


class TranscribeOwnedLandTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['land']))


class TranscribeOwnedBuildingsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}".format(constants.DECLARATION_TABLES['buildings']))


class TranscribeOwnedBankAccountsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['bank_accounts']))


class TranscribeOwnedLandSingleRowEntry(forms.Form):
    judet = forms.ChoiceField(label="Care este judetul in care se gaseste terenul detinut?", choices=Counties.return_counties())
    localitate = forms.CharField(label="Care este localitatea in care se gaseste terenul detinut?")
    comuna = forms.CharField(label="Care este comuna in care se gaseste terenul detinut?")
    categorie = forms.ChoiceField(label="Care este categoria de teren?", choices=RealEstateType.return_as_iterable())
    an_dobandire = forms.DateField(label="Care este anul cand terenul a fost dobandit?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    mod_dobandire = forms.ChoiceField(label="Care este modul in care terenul a fost dobandit?", choices=AttainmentType.return_as_iterable())
    suprafata = forms.CharField(label="Care este suprafata terenului? (mp)")
    cota_parte = forms.IntegerField(label="Care este cota parte din acest teren? (in procente)", max_value=100, min_value=0)
    nume_proprietar = forms.CharField(label="Care este numele proprietarului?")
    prenume_proprietar = forms.CharField(label="Care este prenumele proprietarului")
    
class TranscribeOwnedAutomobileSingleRowEntry(forms.Form):
    tip = forms.CharField(label="Care este tipul autovehiculului?", widget=forms.Select(choices=MobileGoodsType.return_as_iterable()))
    marca = forms.CharField(label="Care este marca autovehiculului?")
    numar_bucati = forms.IntegerField(label="Care este numarul de autovehicule detinute?")
    an_fabricatie = forms.DateField(label="Care este anul de fabricatie al autovehiculului?")
    mod_dobandire = forms.CharField(label="Care este modul in care a fost dobandit autovehiculul?", widget=forms.Select(choices=AttainmentType.return_as_iterable()))
    
class TranscribeOwnedDebtsSingleRowEntry(forms.Form):
    nume_creditor = forms.CharField(label="Care este numele creditorului?")
    prenume_creditor = forms.CharField(label="Care este prenumele creditorului?")
    institutie = forms.CharField(label="Care este numele institutiei creditoare?", widget=forms.Select(choices=FinancialInstitution.return_as_iterable()))
    tip_datorie = forms.CharField(label="Care este tipul de datorie?", widget=forms.Select(choices=DebtType.return_as_iterable()))
    an_contractare = forms.DateField(label="Care este anul contractarii imprumutului?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    scadenta = forms.DateField(label="Care este data scadentei?", widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    valoare = forms.IntegerField(label="Care este valoarea imprumutului?")
    moneda = forms.ChoiceField(label="Care este moneda in care s-a facut imprumutul?", choices=Currency.return_as_iterable())
    
class TranscribeOwnedIncomeFromPensionsSingleRowEntry(forms.Form):
    beneficiar_pensie = forms.CharField(label="Cine este beneficiarul pensiei?", widget=forms.Select(choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES]))
    nume_beneficiar = forms.CharField(label="Care este numele beneficiarului?")
    prenume_beneficiar = forms.CharField(label="Care este prenumele beneficiarului?")
    sursa_venit = forms.CharField(label="Care este numele sursei de venit?")
    judet = forms.CharField(label="Care este judetul de unde provine sursa de venit?")
    localitate = forms.CharField(label="Care este localitatea de unde provine sursa de venit?")
    comuna = forms.CharField(label="Care este comuna de unde provine sursa de venit?")
    strainatate = forms.CharField(label="Care este tara din care provine sursa de venit?")
    serviciu_prestat = forms.CharField(label="Care a fost serviciul prestat?")
    functie = forms.ChoiceField(label="Care a fost functia detinuta?", choices=Position.return_as_iterable())
    venit = forms.IntegerField(label="Care este valoarea venitului?")
    moneda = forms.ChoiceField(label="Care este moneda venitului?", choices=Currency.return_as_iterable())

class TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry(forms.Form):
    relatie_titular = forms.ChoiceField(label="Relatie titular", choices=HolderRelationship.return_as_iterable())
    optiune = forms.ChoiceField(label="Optiune", choices=[(0, "Insitutie"), (1, "Persoana")], widget=forms.RadioSelect)
    nume_persoana = forms.CharField(label="Nume Persoana")
    prenume_persoana = forms.CharField(label="Prenume Persoana")
    sursa = forms.CharField(label="Sursa")
    judet = forms.CharField(label="Care este judetul in care se gaseste terenul detinut?")
    localitate = forms.CharField(label="Care este localitatea in care se gaseste terenul detinut?")
    comuna = forms.CharField(label="Care este comuna in care se gaseste terenul detinut?")
    adresa_strainatate = forms.CharField(label="Adresa strainatate")
    serviciul_prestat = forms.CharField(label="Serviciul prestat")
    pozitie = forms.ChoiceField(label="Pozitie", choices=Position.return_as_iterable())
    venit_anual_incasat = forms.IntegerField(label="Venit anual incasat", min_value=0)
    valuta = forms.ChoiceField(label="Valuta", choices=Currency.return_as_iterable())

class TranscribeOwnedBankAccountsRowEntry(forms.Form):
    institutia_administrativa = forms.ChoiceField(label="Care este institutia financiara?", choices=FinancialInstitution.return_as_iterable())
    tip_cont = forms.ChoiceField(label="Care este tipul contului?", choices=AccountType.return_as_iterable())
    valuta = forms.ChoiceField(label="Care este valuta?", choices=Currency.return_as_iterable())
    # TODO might need to increase the range of YEAR_CHOICES since the account could have been opened in 1989 for all we know
    anul_deschiderii = forms.DateField(label="Care este anul deschiderii contului?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    sold = forms.DecimalField(label="Care este valoarea soldului?", decimal_places=2, max_digits=10)

