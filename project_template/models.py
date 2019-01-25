from django.db import models


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


class OwnedAutomobileTable(models.Model):
    full_name = "Bunuri Mobile - Autovehicule/Autoturisme"
    count = models.IntegerField()


class OwnedJewelryTable(models.Model):
    full_name = "Bunuri Mobile - Metale pretioase, bijuterii, etc"
    count = models.IntegerField()


class OwnedExtraValuableTable(models.Model):
    full_name = "Bunuri Mobile - Valoare depaseste 3000euro"
    count = models.IntegerField()


class OwnedBankAccountsTable(models.Model):
    full_name = "Active Financiare - Conturi si depozite bancare"
    count = models.IntegerField()


class OwnedInvestmentsTable(models.Model):
    full_name = "Active Financiare - Plasamente/Investitii directe"
    count = models.IntegerField()


class OwnedLandTable(models.Model):
    full_name = "Bunuri Imobile - Terenuri"
    count = models.IntegerField()


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
