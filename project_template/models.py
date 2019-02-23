from django.db import models

from project_template.datamodels.account_type import AccountType
from project_template.datamodels.attainment_type import AttainmentType
from project_template.datamodels.building_type import BuildingType
from project_template.datamodels.currency import Currency
from project_template.datamodels.financial_institution import FinancialInstitution
from project_template.datamodels.investment_type import InvestmentType
from project_template.datamodels.real_estate_type import RealEstateType
from project_template.datamodels.mobile_goods_type import MobileGoodsType
from project_template.datamodels.income_provider_type import IncomeProviderType
from project_template.datamodels.estranged_goods_type import EstrangedGoodsType
from project_template.datamodels.goods_separation_type import GoodsSeparationType
from project_template.datamodels.debt_type import DebtType
from project_template.datamodels.position import Position


# More on lazy translations at https://docs.djangoproject.com/en/2.1/topics/i18n/translation/#lazy-translation
from django.utils.translation import ugettext_lazy as _
from .constants import DECLARATION_TABLES

FIRST_2_TYPES = 2


class Politician(models.Model):
    __positions = []

    name = models.CharField(_("The name"), max_length=128)
    surname = models.CharField(_("The surname"), max_length=128)
    position = models.CharField(_("The current poition the politician holds"), max_length=128)

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
        # the position might already be in the list, under a different form
        variations = [position, position.lower(), position.title()]
        if not any(variation in self.__positions for variation in variations):
            self.__positions.append(position.lower())

    @property
    def all_positions(self):
        if self.__positions:
            return ', '.join(self.__positions)
        else:
            return 'No positions have been entered yet.'

    @property
    def __full_name(self):
        return "{} {}".format(self.name, self.surname)


class IncomeDeclaration(models.Model):
    url = models.URLField(max_length=500)
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Income declaration, url: {}\ndate: {}\nfor politician:\n{}".format(
            self.url, self.date, str(self.politician)
        )


class OwnedBuildingsTable(models.Model):
    __full_name = DECLARATION_TABLES['buildings']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedBuildingsTableEntry(models.Model):
    table = models.ForeignKey(OwnedBuildingsTable, on_delete=models.CASCADE)
    address = models.CharField("Adresa", max_length=128)
    category = models.IntegerField("Categorie", choices=BuildingType.return_as_iterable())
    acquisition_year = models.DateField("Anul dobandirii")
    surface = models.IntegerField("Suprafata", blank=True)
    share_ratio = models.DecimalField("Cota-parte", max_digits=3, decimal_places=2, blank=True)
    attainment_type = models.CharField("Modul de dobandire", max_length=32,
                                       choices=AttainmentType.return_as_iterable(), blank=True)
    owner_name = models.CharField("Titular", max_length=128, blank=True)
    observations = models.CharField("Observatii", max_length=256, blank=True)


class OwnedAutomobileTable(models.Model):
    __full_name = DECLARATION_TABLES['automobiles']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedAutomobileTableEntry(models.Model):
    table = models.ForeignKey(OwnedAutomobileTable, on_delete=models.CASCADE)
    car_type = models.CharField("Natura",
                            max_length=32,
                            choices=MobileGoodsType.return_as_iterable())
    brand = models.CharField("Marca", max_length=128)
    no_owned = models.PositiveSmallIntegerField("Numar de bucati")
    fabrication_year = models.DateField("Anul de fabricatie")
    attainment_type = models.CharField("Modul de dobandire",
                                       max_length=32,
                                       choices=AttainmentType.return_as_iterable())


class OwnedJewelryTable(models.Model):
    __full_name = DECLARATION_TABLES['jewelry']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedJewelryTableEntry(models.Model):
    table = models.ForeignKey(OwnedJewelryTable, on_delete=models.CASCADE)
    summary_description = models.CharField("Descriere sumara", max_length=256)
    acquisition_year = models.DateField("Anul dobandirii")
    sum = models.IntegerField("Suma")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())


class OwnedExtraValuableTable(models.Model):
    __full_name = DECLARATION_TABLES['extra_valuable']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedExtraValuableTableEntry(models.Model):
    table = models.ForeignKey(OwnedExtraValuableTable, on_delete=models.CASCADE)
    estrangement_goods_type = models.CharField("Natura bunului instrainat",
                                               max_length=128,
                                               choices=EstrangedGoodsType.return_as_iterable())
    estrangement_date = models.DateField("Data instrainarii")
    receiver_of_goods = models.CharField("Persoana catre care s-a instrainat", max_length=128)
    goods_separation_type = models.CharField("Forma instrainarii",
                                             max_length=64,
                                             choices=GoodsSeparationType.return_as_iterable())
    value = models.IntegerField("Valoare")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())


class OwnedBankAccountsTable(models.Model):
    __full_name = DECLARATION_TABLES['bank_accounts']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedBankAccountsTableEntry(models.Model):
    table = models.ForeignKey(OwnedBankAccountsTable, on_delete=models.CASCADE)
    institution = models.CharField("Instituția",
                                   max_length=128,
                                   choices=FinancialInstitution.return_as_iterable())
    address = models.CharField("Adresa institutiei",
                               max_length=128)
    account_holder = models.CharField("Titular",
                                      max_length=128)
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())
    opening_year = models.DateField("Deschis in anul")
    account_type = models.IntegerField("Tipul",
                                       choices=AccountType.return_as_iterable())


class OwnedInvestmentsTable(models.Model):
    __full_name = DECLARATION_TABLES['investments']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedInvestmentsTableEntry(models.Model):
    table = models.ForeignKey(OwnedInvestmentsTable, on_delete=models.CASCADE)
    investment_issuer_name = models.CharField("Emitent titlu/societate in care persoana este actionar sau asociat"
                                              "/beneficiar de imprumut",
                                              max_length=128)
    type_of_investment = models.IntegerField("Tipul",
                                             choices=InvestmentType.return_as_iterable())
    number_of_stocks = models.IntegerField("Numar de titluri")
    share_ratio = models.DecimalField("Cota de participare", max_digits=3, decimal_places=2)
    total_value = models.IntegerField("Valoare totala la zi")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())


class OwnedLandTable(models.Model):
    __full_name = DECLARATION_TABLES['land']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedLandTableEntry(models.Model):
    table = models.ForeignKey(OwnedLandTable, on_delete=models.CASCADE)
    address = models.CharField("Adresa sau zona",
                               max_length=128)
    category = models.IntegerField("Categorie", choices=RealEstateType.return_as_iterable())
    acquisition_year = models.DateField("Anul dobandirii")
    surface = models.IntegerField("Suprafata mp")
    share_ratio = models.DecimalField("Cota-parte", max_digits=3, decimal_places=2)
    attainment_type = models.CharField("Modul de dobandire",
                                       max_length=32,
                                       choices=AttainmentType.return_as_iterable(),
                                       blank=True)
    owner = models.CharField("Titular", max_length=128, blank=True)
    observations = models.CharField("Observatii", max_length=256, blank=True)


class OwnedDebtsTable(models.Model):
    __full_name = DECLARATION_TABLES['debts']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedDebtsTableEntry(models.Model):
    table = models.ForeignKey(OwnedDebtsTable, on_delete=models.CASCADE)
    lender = models.CharField("Creditor", max_length=128,
                              choices=FinancialInstitution.return_as_iterable(),
                              blank=True)
    debt_type = models.CharField("Tip datorie", max_length=30,
                                 choices=DebtType.return_as_iterable())
    acquirement_year = models.DateField("Contractat in anul")
    due_date = models.DateField("Scadent la")
    value = models.IntegerField("Valoare")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())


class OwnedGoodsOrServicesPerOwnerTable(models.Model):
    __full_name = DECLARATION_TABLES['goods']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedGoodsOrServicesPerOwnerTableEntry(models.Model):
    table = models.ForeignKey(OwnedGoodsOrServicesPerOwnerTable, on_delete=models.CASCADE)
    holder = models.CharField("Cine a realizat venitul(Titular)", max_length=128)
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedGoodsOrServicesPerSpouseTable(models.Model):
    __full_name = DECLARATION_TABLES['gifts_spouse']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedGoodsOrServicesPerSpouseTableEntry(models.Model):
    table = models.ForeignKey(OwnedGoodsOrServicesPerSpouseTable, on_delete=models.CASCADE)
    holder = models.CharField("Cine a realizat venitul(Sot/sotie)", max_length=128)
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedGoodsOrServicesPerChildTable(models.Model):
    __full_name = DECLARATION_TABLES['gifts_kids']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedGoodsOrServicesPerChildTableEntry(models.Model):
    table = models.ForeignKey(OwnedGoodsOrServicesPerChildTable, on_delete=models.CASCADE)
    holder = models.CharField("Cine a realizat venitul(Copii)", max_length=128)
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromSalariesTable(models.Model):
    __full_name = DECLARATION_TABLES['salaries']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromSalariesTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromSalariesTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable())
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromIndependentActivitiesTable(models.Model):
    __full_name = DECLARATION_TABLES['independent_activities']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromIndependentActivitiesTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromIndependentActivitiesTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES])
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromDeferredUseOfGoodsTable(models.Model):
    __full_name = DECLARATION_TABLES['deferred_use']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromDeferredUseOfGoodsTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromDeferredUseOfGoodsTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES])
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromInvestmentsTable(models.Model):
    __full_name = DECLARATION_TABLES['income_investments']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromInvestmentsTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromInvestmentsTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES])
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromPensionsTable(models.Model):
    __full_name = DECLARATION_TABLES['pensions']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromPensionsTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromPensionsTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES])
    provider_name = models.CharField("Nume beneficiar")
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    ex_position = models.CharField("Functia", max_length = 128,
                                   choices=Position.return_as_iterable())
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromAgriculturalActivitiesTable(models.Model):
    __full_name = DECLARATION_TABLES['agriculture']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField(_("The number of rows"))


class OwnedIncomeFromAgriculturalActivitiesTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromAgriculturalActivitiesTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable()[0:FIRST_2_TYPES])
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())
    

class OwnedIncomeFromGamblingTable(models.Model):
    __full_name = DECLARATION_TABLES['gambling']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromGamblingTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromGamblingTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable())
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())


class OwnedIncomeFromOtherSourcesTable(models.Model):
    __full_name = DECLARATION_TABLES['other_sources']
    # declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromOtherSourcesTableEntry(models.Model):
    table = models.ForeignKey(OwnedIncomeFromOtherSourcesTable, on_delete=models.CASCADE)
    income_provider_type = models.CharField("Cine a realizat venitul",
                                            max_length=128,
                                            choices=IncomeProviderType.return_as_iterable())
    name_source_of_goods = models.CharField("Sursa venitului: nume", max_length=128)
    address_source_of_goods = models.CharField("Sursa venitului: adresa", max_length=128)
    goods_name = models.CharField("Serviciul prestat/Obiectul generator de venit", max_length=128)
    annual_income = models.IntegerField("Venitul anual incasat")
    annual_income_currency = models.CharField("Valuta",
                                              max_length=16,
                                              choices=Currency.return_as_iterable())
