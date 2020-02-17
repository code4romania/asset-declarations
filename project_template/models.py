from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from moonsheep.models import DocumentModel

from project_template.datamodels.account_type import AccountType
from project_template.datamodels.attainment_type import AttainmentType
from project_template.datamodels.building_type import BuildingType
from project_template.datamodels.currency import Currency
from project_template.datamodels.financial_institution import FinancialInstitution
from project_template.datamodels.holder_relationship import HolderRelationship
from project_template.datamodels.holder_type import HolderType
from project_template.datamodels.investment_type import InvestmentType
from project_template.datamodels.real_estate_type import RealEstateType
from project_template.datamodels.mobile_goods_type import MobileGoodsType
from project_template.datamodels.estranged_goods_type import EstrangedGoodsType
from project_template.datamodels.goods_separation_type import GoodsSeparationType
from project_template.datamodels.debt_type import DebtType
from project_template.datamodels.position import Position
from project_template.datamodels.institution import Institution
from project_template.datamodels.counties import Counties

from .constants import DECLARATION_TABLES
from .utils import AutoCleanModelMixin, XORModelMixin

FIRST_2_TYPES = 2

# TODO remove null=True from all ForeignKey fields. Temporary fix for Django dev mode.
# Reference: https://stackoverflow.com/questions/46088488/django-db-utils-integrityerror-not-null-constraint-failed-app-area-id


def validate_percentage(value):
    """
    Validates that a percentage value, if given, is between 0 and 100

    :param value: Percentage value to be checked
    :return:
    """
    if not value:
        return

    if value > 100:
        raise ValidationError(
            _('%(value)s is greater than 100%'),
            params={'value': value},
        )
    elif value < 0:
        raise ValidationError(
            _('%(value)s is lower than 0%'),
            params={'value': value},
        )


class Politician(models.Model):
    all_positions = None

    name = models.CharField(_("Name"), max_length=128)
    surname = models.CharField(_("Surname"), max_length=128)
    initials = models.CharField(_("Initials"), max_length=20)
    previous_name = models.CharField(_("Previous Name"), max_length=128, blank=True)

    # Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps.
    # Note that the current date is always used; it’s not just a default value that you can override.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically set the field to now when the object is first created. Useful for creation of timestamps.
    # Note that the current date is always used; it’s not just a default value that you can override.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Name: {} {}\nPositions: {}\nCreated at: {}\nUpdated at {}".format(
            self.surname, self.name, self.all_positions, self.created_at, self.updated_at
        )

    def add_position(self, position):
        if not self.all_positions:
            self.all_positions = []
        self.all_positions.append(position)

    @property
    def __full_name(self):
        return "{} {}".format(self.name, self.surname)


class Declaration(DocumentModel):
    url = models.URLField(max_length=500)
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE, null=True)
    position = models.CharField(_("Functie"), max_length=128, choices=Position.return_as_iterable())
    date = models.DateField(_("Data completare"))
    institution = models.CharField(_("Institutie"), max_length=128, choices=Institution.return_as_iterable())
    declaration_type = models.CharField(_("Tip declaratie"), max_length=128, choices=Institution.return_as_iterable())

    def __str__(self):
        return "Income declaration, url: {}\ndate: {}\nfor politician:\n{}".format(
            self.url, self.date, str(self.politician)
        )


class Person(models.Model):
    name = models.CharField("Nume persoana", max_length=128)
    previous_name = models.CharField("Nume anterior", max_length=128, null=True, blank=True)
    initials = models.CharField("Initiale", max_length=10, null=True, blank=True)
    surname = models.CharField("Prenume", max_length=128)


class CommonInfo(AutoCleanModelMixin, XORModelMixin, models.Model):
    XOR_FIELDS = [
        {
            "commune": _("commune"),
            "city": _("city"),
        }
    ]

    county = models.CharField("Judet", max_length=32, choices=Counties.return_counties())
    city = models.CharField("Localitate", max_length=32, null=True, blank=True)
    commune = models.CharField("Comuna", max_length=32, null=True, blank=True)
    address = models.CharField("Adresa", max_length=64, null=True, blank=True)

    class Meta:
        abstract = True


class CommonIncomeFields(CommonInfo):
    holder_relationship = models.CharField("Cine a realizat venitul", max_length=128, choices=HolderRelationship.return_as_iterable())
    source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    service = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128, null=True, blank=True)
    annual_income = models.FloatField("Venitul anual incasat")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())

    class Meta:
        abstract = True


# Tabel Terenuri - row numbers
class OwnedLandTable(models.Model):
    __full_name = DECLARATION_TABLES['land']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Terenuri - actual row information
class OwnedLandTableEntry(CommonInfo):
    table = models.ForeignKey(OwnedLandTable, on_delete=models.CASCADE, null=True)
    coowner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    category = models.CharField("Categorie", max_length=32, choices=RealEstateType.return_as_iterable())
    acquisition_year = models.IntegerField("Anul dobandirii")
    surface = models.FloatField("Suprafata mp")
    share_ratio = models.DecimalField("Cota-parte", max_digits=5, decimal_places=2, validators=[validate_percentage])
    taxable_value = models.FloatField('Valoarea de impozitare', blank=True)
    taxable_value_currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())
    attainment_type = models.CharField("Modul de dobandire", max_length=32, choices=AttainmentType.return_as_iterable(), blank=True)
    observations = models.CharField("Observatii", max_length=256, blank=True)


# Tabel Cladiri - row numbers
class OwnedBuildingsTable(models.Model):
    __full_name = DECLARATION_TABLES['buildings']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Cladiri - actual row information
class OwnedBuildingsTableEntry(CommonInfo):
    table = models.ForeignKey(OwnedBuildingsTable, on_delete=models.CASCADE, null=True)
    coowner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    category = models.IntegerField("Categorie", choices=BuildingType.return_as_iterable())
    acquisition_year = models.IntegerField("Anul dobandirii")
    surface = models.FloatField("Suprafata", blank=True)
    share_ratio = models.DecimalField("Cota-parte", max_digits=5, decimal_places=2, blank=True, validators=[validate_percentage])
    taxable_value = models.FloatField('Valoarea de impozitare', blank=True)
    taxable_value_currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())
    attainment_type = models.CharField("Modul de dobandire", max_length=32, choices=AttainmentType.return_as_iterable(), blank=True)
    observations = models.CharField("Observatii", max_length=256, blank=True)


# Tabel Bunuri Mobile - row numbers
class OwnedAutomobileTable(models.Model):
    __full_name = DECLARATION_TABLES['automobiles']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Bunuri Mobile - actual row information
class OwnedAutomobileTableEntry(models.Model):
    table = models.ForeignKey(OwnedAutomobileTable, on_delete=models.CASCADE, null=True)
    goods_type = models.CharField("Tipul vehiculului", max_length=32, choices=MobileGoodsType.return_as_iterable())
    brand = models.CharField("Marca", max_length=128)
    no_owned = models.PositiveSmallIntegerField("Numar de bucati")
    fabrication_year = models.IntegerField("Anul de fabricatie")
    attainment_type = models.CharField("Modul de dobandire", max_length=32, choices=AttainmentType.return_as_iterable())


# Tabel Bunuri Imobile - row numbers
class OwnedJewelryTable(models.Model):
    __full_name = DECLARATION_TABLES['jewelry']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Bunuri Imobile - actual row information
class OwnedJewelryTableEntry(models.Model):
    table = models.ForeignKey(OwnedJewelryTable, on_delete=models.CASCADE, null=True)
    summary_description = models.CharField("Descriere sumara", max_length=256)
    acquisition_year = models.IntegerField("Anul dobandirii")
    goods_value = models.IntegerField("Suma")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())


# Tabel Bunuri Mobile Instrainate, Valoare peste 3000EUR - row numbers
class OwnedExtraValuableTable(models.Model):
    __full_name = DECLARATION_TABLES['extra_valuable']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Bunuri Mobile Instrainate, Valoare peste 3000EUR - actual row information
class OwnedExtraValuableTableEntry(CommonInfo):
    table = models.ForeignKey(OwnedExtraValuableTable, on_delete=models.CASCADE, null=True)
    receiver_of_goods = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    estrangement_goods_type = models.CharField("Natura bunului instrainat", max_length=128, choices=EstrangedGoodsType.return_as_iterable())
    estrangement_date = models.DateField("Data instrainarii")
    goods_separation_type = models.CharField("Forma instrainarii", max_length=64, choices=GoodsSeparationType.return_as_iterable())
    value = models.IntegerField("Valoare")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())


# Tabel Conturi - row numbers
class OwnedBankAccountsTable(models.Model):
    __full_name = DECLARATION_TABLES['bank_accounts']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Conturi - actual row information
class OwnedBankAccountsTableEntry(models.Model):
    table = models.ForeignKey(OwnedBankAccountsTable, on_delete=models.CASCADE, null=True)
    institution = models.CharField("Instituția", max_length=128, choices=FinancialInstitution.return_as_iterable())
    account_type = models.IntegerField("Tipul", choices=AccountType.return_as_iterable())
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())
    opening_year = models.IntegerField("Deschis in anul")
    account_balance = models.DecimalField("Soldul", decimal_places=2, max_digits=10)


# Tabel Plasamente, Investitii - row numbers
class OwnedInvestmentsOver5KTable(models.Model):
    __full_name = DECLARATION_TABLES['investments']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Plasamente, Investitii - actual row information
class OwnedInvestmentsOver5KTableEntry(models.Model):
    table = models.ForeignKey(OwnedInvestmentsOver5KTable, on_delete=models.CASCADE, null=True)
    loan_beneficiary = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    issue_title = models.CharField("Emitent titlu", max_length=128, null=True, blank=True)
    shareholder_society = models.CharField("Societate in care persoana este actionar sau asociat", max_length=128, null=True, blank=True)
    type_of_investment = models.CharField("Tipul", max_length=128, choices=InvestmentType.return_as_iterable())
    number_of_stocks = models.IntegerField("Numar de titluri", null=True, blank=True)
    share_ratio = models.DecimalField("Cota de participare", max_digits=5, decimal_places=2, null=True, blank=True, validators=[validate_percentage])
    total_value = models.FloatField("Valoare totala la zi")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())


# Tabel Alte active - row numbers
class OtherActivesTable(models.Model):
    __full_name = DECLARATION_TABLES['other_actives']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Alte active - actual row information
class OtherActivesTableEntry(models.Model):
    table = models.ForeignKey(OtherActivesTable, on_delete=models.CASCADE, null=True)
    active_type = models.CharField("Tipul activului", max_length=128)
    active_value = models.FloatField("Valoarea activului")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())


# Tabel Datorii - row numbers
class OwnedDebtsTable(models.Model):
    __full_name = DECLARATION_TABLES['debts']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Datorii - actual row information
class OwnedDebtsTableEntry(models.Model):
    XOR_FIELDS = [
        {
            "person": _("person"),
            "lender": _("lender"),
        }
    ]

    table = models.ForeignKey(OwnedDebtsTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    lender = models.CharField("Creditor", max_length=128, choices=FinancialInstitution.return_as_iterable(), null=True, blank=True)
    debt_type = models.CharField("Tip datorie", max_length=30, choices=DebtType.return_as_iterable())
    acquirement_year = models.IntegerField("Contractat in anul")
    due_date = models.IntegerField("Scadent la")
    value = models.FloatField("Valoare")
    currency = models.CharField("Valuta", max_length=16, choices=Currency.return_as_iterable())


# Tabel Cadouri Servicii - row number
class OwnedGoodsOrServicesTable(models.Model):
    __full_name = DECLARATION_TABLES['goods']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Cadouri Servicii - actual row information
class OwnedGoodsOrServicesTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedGoodsOrServicesTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri salarii - row number
class OwnedIncomeFromSalariesTable(models.Model):
    __full_name = DECLARATION_TABLES['salaries']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri salarii - actual row information
class OwnedIncomeFromSalariesTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromSalariesTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri activitati independente - row number
class OwnedIncomeFromIndependentActivitiesTable(models.Model):
    __full_name = DECLARATION_TABLES['independent_activities']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri activitati independente - actual row information
class OwnedIncomeFromIndependentActivitiesTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromIndependentActivitiesTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri cedarea folosintei bunurilor - row number
class OwnedIncomeFromDeferredUseOfGoodsTable(models.Model):
    __full_name = DECLARATION_TABLES['deferred_use']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri cedarea folosintei bunurilor - actual row information
class OwnedIncomeFromDeferredUseOfGoodsTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromDeferredUseOfGoodsTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri investitii - row number
class OwnedIncomeFromInvestmentsTable(models.Model):
    __full_name = DECLARATION_TABLES['income_investments']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri investitii - actual row information
class OwnedIncomeFromInvestmentsTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromInvestmentsTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri pensii - row number
class OwnedIncomeFromPensionsTable(models.Model):
    __full_name = DECLARATION_TABLES['pensions']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri pensii - actual row information
class OwnedIncomeFromPensionsTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromPensionsTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    ex_position = models.CharField("Pozitia detinuta", max_length=128)


# Tabel Venituri activitati agricole - row number
class OwnedIncomeFromAgriculturalActivitiesTable(models.Model):
    __full_name = DECLARATION_TABLES['agriculture']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(_("The number of rows"))


# Tabel Venituri activitati agricole - actual row information
class OwnedIncomeFromAgriculturalActivitiesTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromAgriculturalActivitiesTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    holder_type = models.CharField("Tipul detinatorului", max_length=120, choices=HolderType.return_as_iterable())


# Tabel Venituri premii jocuri noroc - row numbers
class OwnedIncomeFromGamblingTable(models.Model):
    __full_name = DECLARATION_TABLES['gambling']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Venituri premii jocuri noroc - actual row information
class OwnedIncomeFromGamblingTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromGamblingTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


# Tabel Venituri din alte surse - row numbers
class OwnedIncomeFromOtherSourcesTable(models.Model):
    __full_name = DECLARATION_TABLES['other_sources']
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True)
    count = models.IntegerField("The number of rows")


# Tabel Venituri din alte surse - actual row information
class OwnedIncomeFromOtherSourcesTableEntry(CommonIncomeFields):
    table = models.ForeignKey(OwnedIncomeFromOtherSourcesTable, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
