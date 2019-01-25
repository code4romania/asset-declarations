from django.db import models
from datamodels.building_type import BuildingType
from datamodels.attainment_type import AttainmentType
from datamodels.financial_institution import FinancialInstitution
from datamodels.currency import Currency
from datamodels.investment_type import InvestmentType
from datamodels.account_type import AccountType
from datamodels.real_estate_type import RealEstateType

class Politician(models.Model):
    name = models.CharField("The first name", max_length=128)
    surname = models.CharField("The surname", max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)


class IncomeDeclaration(models.Model):
    url = models.URLField(max_length=500)
    politician = models.ForeignKey("Politician", on_delete=models.PROTECT)
    year = models.IntegerField()

    def __str__(self):
        return "{}'s income declaration, dated {}".format(self.politician.full_name, self.year)


class OwnedBuildingsTable(models.Model):
    full_name = "Bunuri Imobile - Cladiri"
    count = models.IntegerField()

class OwnedBuildingsTableEntry(models.Model):
    address = models.CharField("Adresa", max_length=128)
    category = models.IntegerField("Categorie", choices=BuildingType.return_as_iterable())
    acquisition_year = models.DateField("Anul dobandirii")
    surface = models.IntegerField("Suprafata")
    share_ratio = models.DecimalField("Cota-parte", max_digits=3, decimal_places=2)
    attainment_type = models.CharField("Modul de dobandire", max_length=32, choices=AttainmentType.return_as_iterable())
    owner_name = models.CharField("Titular", max_length=128)

class OwnedAutomobileTable(models.Model):
    full_name = "Bunuri Mobile - Autovehicule/Autoturisme"
    count = models.IntegerField()

class OwnedAutomobileTableEntry(models.Model):
    address = models.CharField("Adresa", max_length=128)
    brand = models.CharField("Marca", max_length=128)
    no_owned = models.PositiveSmallIntegerField("Numar de bucati")
    fabrication_year = models.DateField("Anul de fabricatie")
    attainment_type = models.CharField("Modul de dobandire",
                                       max_length=32,
                                       choices=AttainmentType.return_as_iterable())

class OwnedJewelryTable(models.Model):
    full_name = "Bunuri Mobile - Metale pretioase, bijuterii, etc"
    count = models.IntegerField()

class OwnedJewelryTableEntry(models.Model):
    summary_description = models.CharField("Descriere sumara", max_length=256)
    acquisition_year = models.DateField("Anul dobandirii")
    sum = models.IntegerField("Suma")
    currency = models.CharField("Valuta",
                                max_length=16,
                                choices=Currency.return_as_iterable())

#TODO find where this table is
class OwnedExtraValuableTable(models.Model):
    full_name = "Bunuri Mobile - Valoare depaseste 3000euro"
    count = models.IntegerField()


class OwnedBankAccountsTable(models.Model):
    full_name = "Active Financiare - Conturi si depozite bancare"
    count = models.IntegerField()

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
    full_name = "Active Financiare - Plasamente/Investitii directe"
    count = models.IntegerField()

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
    full_name = "Bunuri Imobile - Terenuri"
    count = models.IntegerField()

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
    full_name = "Datorii"
    count = models.IntegerField()


class OwnedGoodsOrServicesPerOwnerTable(models.Model):
    full_name = "Cadouri/Servicii - Titular"
    count = models.IntegerField()


class OwnedGoodsOrServicesPerSpouseTable(models.Model):
    full_name = "Cadouri/Servicii - Sot/Sotie"
    count = models.IntegerField()


class OwnedGoodsOrServicesPerChildTable(models.Model):
    full_name = "Cadouri/Servicii - Copii"
    count = models.IntegerField()


class OwnedIncomeFromSalariesTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 1. Venituri din salarii"
    count = models.IntegerField()


class OwnedIncomeFromIndependentActivities(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 2. Venituri din activitati independente"
    count = models.IntegerField()


class OwnedIncomeFromDeferredUseOfGoodsTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 3. Venituri din cedarea folosintei bunurilor"
    count = models.IntegerField()


class OwnedIncomeFromInvestmentsTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 4. Venituri din investitii"
    count = models.IntegerField()


class OwnedIncomeFromPensionsTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 5. Venituri din pensii"
    count = models.IntegerField()


class OwnedIncomeFromAgriculturalActivitiesTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 6. Venituri din activitati agricole"
    count = models.IntegerField()


class OwnedIncomeFromGamblingTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 7. Venituri din premii si jocuri de noroc"
    count = models.IntegerField()


class OwnedIncomeFromOtherSourcesTable(models.Model):
    full_name = "Venituri ale declarantului si ale membrilor sai de familie - 8. Venituri din alte surse"
    count = models.IntegerField()
