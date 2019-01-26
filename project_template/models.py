from django.db import models

from constants import DECLARATION_TABLES
from datamodels.building_type import BuildingType
from datamodels.attainment_type import AttainmentType
from datamodels.financial_institution import FinancialInstitution
from datamodels.currency import Currency
from datamodels.investment_type import InvestmentType
from datamodels.account_type import AccountType
from datamodels.real_estate_type import RealEstateType




class Politician(models.Model):
    __positions = []

    name = models.CharField("The name", max_length=128)
    surname = models.CharField("The surname", max_length=128)
    position = models.CharField("The current poition the politician holds", max_length=128)

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
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedBuildingsTableEntry(models.Model):
    address = models.CharField("Adresa", max_length=128)
    category = models.IntegerField("Categorie", choices=BuildingType.return_as_iterable())
    acquisition_year = models.DateField("Anul dobandirii")
    surface = models.IntegerField("Suprafata")
    share_ratio = models.DecimalField("Cota-parte", max_digits=3, decimal_places=2)
    attainment_type = models.CharField("Modul de dobandire", max_length=32, choices=AttainmentType.return_as_iterable())
    owner_name = models.CharField("Titular", max_length=128)

class OwnedAutomobileTable(models.Model):
    __full_name = DECLARATION_TABLES['automobiles']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedAutomobileTableEntry(models.Model):
    address = models.CharField("Adresa", max_length=128)
    brand = models.CharField("Marca", max_length=128)
    no_owned = models.PositiveSmallIntegerField("Numar de bucati")
    fabrication_year = models.DateField("Anul de fabricatie")
    attainment_type = models.CharField("Modul de dobandire",
                                       max_length=32,
                                       choices=AttainmentType.return_as_iterable())

class OwnedJewelryTable(models.Model):
    __full_name = DECLARATION_TABLES['jewelry']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedJewelryTableEntry(models.Model):
    summary_description = models.CharField("Descriere sumara", max_length=256)
    acquisition_year = models.DateField("Anul dobandirii")
    sum = models.IntegerField("Suma")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())

#TODO find where this table is
class OwnedExtraValuableTable(models.Model):
    __full_name = DECLARATION_TABLES['extra_valuable']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedBankAccountsTable(models.Model):
    __full_name = DECLARATION_TABLES['bank_accounts']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedBankAccountsTableEntry(models.Model):
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
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedInvestmentsTableEntry(models.Model):
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
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedLandTableEntry(models.Model):
    #TODO see how to model the Dragnea exception :/
    address = models.CharField("Adresa sau zona",
                               max_length=128)
    category = models.IntegerField("Categorie", choices=RealEstateType.return_as_iterable())
    acquisition_year = models.DateField("Anul dobandirii")
    surface = models.IntegerField("Suprafata mp")
    share_ratio = models.DecimalField("Cota-parte", max_digits=3, decimal_places=2)
    attainment_type = models.CharField("Modul de dobandire",
                                       max_length=32,
                                       choices=AttainmentType.return_as_iterable())

class OwnedDebtsTable(models.Model):
    __full_name = DECLARATION_TABLES['debts']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedGoodsOrServicesPerOwnerTable(models.Model):
    __full_name = DECLARATION_TABLES['goods']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")



class OwnedGoodsOrServicesPerSpouseTable(models.Model):
    __full_name = DECLARATION_TABLES['gifts_spouse']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")

class OwnedGoodsOrServicesPerChildTable(models.Model):
    __full_name = DECLARATION_TABLES['gifts_kids']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromSalariesTable(models.Model):
    __full_name = DECLARATION_TABLES['salaries']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromIndependentActivities(models.Model):
    __full_name = DECLARATION_TABLES['independent_activities']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromDeferredUseOfGoodsTable(models.Model):
    __full_name = DECLARATION_TABLES['deferred_use']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")



class OwnedIncomeFromInvestmentsTable(models.Model):
    __full_name = DECLARATION_TABLES['income_investments']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromPensionsTable(models.Model):
    __full_name = DECLARATION_TABLES['pensions']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromAgriculturalActivitiesTable(models.Model):
    __full_name = DECLARATION_TABLES['agriculture']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")




class OwnedIncomeFromGamblingTable(models.Model):
    __full_name = DECLARATION_TABLES['gambling']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedIncomeFromOtherSourcesTable(models.Model):
    __full_name = DECLARATION_TABLES['other_sources']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


