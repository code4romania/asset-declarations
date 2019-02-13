from django import forms
from django.utils.translation import ugettext_lazy as _
from project_template import constants
from .datamodels.real_estate_type import RealEstateType
from .datamodels.attainment_type import AttainmentType

YEAR_CHOICES = ('2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')


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
    address = forms.CharField(
        label="What is the address of the building?"
    )
    category = forms.CharField(
        label="What is the category of the building?"
    )
    attainment_year = forms.CharField(
        label="What is the attainment year of the building?"
    )
    surface = forms.CharField(
        label="What is the surface of the building?"
    )
    share = forms.CharField(
        label="What is the share in the building?"
    )
    attainment_type = forms.CharField(
        label="What is the way the building was attained?"
    )
    holder = forms.CharField(
        label="Who is the holder of the building?"
    )

class TranscribeOwnedBankAccountsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['bank_accounts']))

class TranscribeOwnedLandSingleRowEntry(forms.Form):
    judet = forms.CharField(label="Care este judetul in care se gaseste terenul detinut?")
    localitate = forms.CharField(label="Care este localitatea in care se gaseste terenul detinut?")
    comuna = forms.CharField(label="Care este comuna in care se gaseste terenul detinut?")
    categorie = forms.ChoiceField(label="Care este categoria de teren?", choices=RealEstateType.return_as_iterable())
    an_dobandire = forms.DateField(label="Care este anul cand terenul a fost dobandit?", widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    mod_dobandire = forms.ChoiceField(label="Care este modul in care terenul a fost dobandit?", choices=AttainmentType.return_as_iterable())
    suprafata = forms.CharField(label="Care este suprafata terenului? (mp)")
    cota_parte = forms.IntegerField(label="Care este cota parte din acest teren? (in procente)", max_value=100, min_value=0)
    nume_proprietar = forms.CharField(label="Care este numele proprietarului?")
    prenume_proprietar = forms.CharField(label="Care este prenumele proprietarului")