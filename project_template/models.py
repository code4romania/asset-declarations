from django.db import models

from .constants import DECLARATION_TABLES


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
    

class OwnedAutomobileTable(models.Model):
    __full_name = DECLARATION_TABLES['automobiles']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedJewelryTable(models.Model):
    __full_name = DECLARATION_TABLES['jewelry']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")
    

class OwnedExtraValuableTable(models.Model):
    __full_name = DECLARATION_TABLES['extra_valuable']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedBankAccountsTable(models.Model):
    __full_name = DECLARATION_TABLES['bank_accounts']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")
    

class OwnedInvestmentsTable(models.Model):
    __full_name = DECLARATION_TABLES['investments']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


class OwnedLandTable(models.Model):
    __full_name = DECLARATION_TABLES['land']
    declaration = models.ForeignKey(IncomeDeclaration, on_delete=models.CASCADE)
    count = models.IntegerField("The number of rows")


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
