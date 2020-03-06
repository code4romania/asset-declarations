from moonsheep.tasks import register_task

import project_template.models as models
import project_template.forms as forms
from project_template.task_templates import DigitalizationTask, CountTableRowsTask, RowEntryTask


@register_task()
class TaskGetInitialInformation(DigitalizationTask):
    task_form = forms.TranscribeInitialInformation
    template_name = "tasks/general_information_task.html"

    child_tasks = [
        "TaskOwnedLandTable",
        "TaskOwnedAutomobileTable",
        "TaskOwnedBankAccountsTable",
        "TaskOwnedIncomeFromAgriculturalActivitiesTable",
        "TaskOwnedDebtsTable",
        "TaskOwnedIncomeFromPensionsTable",
        "TaskOwnedGoodsOrServicesTable",
        "TaskOwnedInvestmentsOver5KTable",
        "TaskOwnedIncomeFromOtherSourcesTable",
        "TaskOwnedJewelryTable",
        "TaskExtraValuableTable",
        "TaskOwnedIncomeFromDeferredUseOfGoodsTable",
        "TaskOwnedIncomeFromIndependentActivitiesTable",
        "TaskOwnedIncomeFromGamblingTable",
        "TaskOwnedIncomeFromSalariesTable",
        "TaskOwnedBuildingsTable",
        "TaskOwnedIncomeFromInvestmentsTable",
    ]

    def save_verified_data(self, verified_data):
        politician, created = models.Politician.objects.get_or_create(
            name=verified_data["name"],
            surname=verified_data["surname"],
            initials=verified_data["initials"],
            previous_name=verified_data["previous_name"],
        )

        politician.add_position(verified_data["position"])

        # should raise if not exist
        declaration = models.Declaration.objects.get(pk=self.instance.doc_id)

        declaration.politician = politician
        declaration.date = verified_data["date"]
        declaration.position = verified_data["position"]
        declaration.institution = verified_data["institution"]
        declaration.declaration_type = verified_data["declaration_type"]


@register_task()
class TaskOwnedLandRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedLandRowEntry
    template_name = "tasks/owned_land.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("owner_name"), surname=verified_data.get("owner_surname"),
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["owner_name"]
        del verified_data["owner_surname"]

        models.OwnedLandTableEntry.objects.get_or_create(
            coowner=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedLandTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedLandTable
    storage_model = models.OwnedLandTable
    child_tasks = [TaskOwnedLandRowEntry]


@register_task()
class TaskOwnedAutomobileRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedAutomobileRowEntry
    template_name = "tasks/owned_automobile.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        models.OwnedAutomobileTableEntry.objects.get_or_create(**verified_data)


@register_task()
class TaskOwnedAutomobileTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedAutomobileTable
    storage_model = models.OwnedAutomobileTable
    child_tasks = [TaskOwnedAutomobileRowEntry]


@register_task()
class TaskOwnedBankAccountsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedBankAccountsRowEntry
    template_name = "tasks/owned_bank_accounts.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        models.OwnedBankAccountsTableEntry.objects.get_or_create(**verified_data,)


@register_task()
class TaskOwnedBankAccountsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    storage_model = models.OwnedBankAccountsTable
    child_tasks = [TaskOwnedBankAccountsRowEntry]


@register_task()
class TaskOwnedIncomeFromAgriculturalActivitiesRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry
    template_name = "tasks/agricultural_activity.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromAgriculturalActivitiesTableEntry.objects.get_or_create(
            person=owner_person, **verified_data
        )


@register_task()
class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    child_tasks = [TaskOwnedIncomeFromAgriculturalActivitiesRowEntry]


@register_task()
class TaskOwnedDebtsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedDebtsRowEntry
    template_name = "tasks/owned_debts.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        if verified_data.get("loaner_name") and verified_data.get("loaner_surname"):
            # Use the custom form fields
            loaner_person, created = models.Person.objects.get_or_create(
                name=verified_data.get("loaner_name"), surname=verified_data.get("loaner_surname"),
            )

            # Remove the custom form fields before saving the table entry
            del verified_data["loaner_name"]
            del verified_data["loaner_surname"]

            models.OwnedDebtsTableEntry.objects.get_or_create(
                person=loaner_person, **verified_data,
            )
        elif verified_data.get("institution"):
            models.OwnedDebtsTableEntry.objects.get_or_create(**verified_data,)


@register_task()
class TaskOwnedDebtsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedDebtsTable
    storage_model = models.OwnedDebtsTable
    child_tasks = [TaskOwnedDebtsRowEntry]


@register_task()
class TaskOwnedIncomeFromPensionsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsRowEntry
    template_name = "tasks/owned_income_from_pensions.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("beneficiary_name"), surname=verified_data.get("beneficiary_surname"),
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["beneficiary_name"]
        del verified_data["beneficiary_surname"]

        models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
            person=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    child_tasks = [TaskOwnedIncomeFromPensionsRowEntry]


@register_task()
class TaskOwnedGoodsOrServicesRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesRowEntry
    template_name = "tasks/owned_goods_or_services.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedGoodsOrServicesTableEntry.objects.get_or_create(person=owner_person, **verified_data)


@register_task()
class TaskOwnedGoodsOrServicesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesTable
    storage_model = models.OwnedGoodsOrServicesTable
    child_tasks = [TaskOwnedGoodsOrServicesRowEntry]


@register_task()
class TaskOwnedInvestmentsOver5KRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KRowEntry
    template_name = "tasks/owned_investments_over_5k.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        loan_beneficiary, created = models.Person.objects.get_or_create(
            name=verified_data.get("beneficiary_name"), surname=verified_data.get("beneficiary_surname"),
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["beneficiary_name"]
        del verified_data["beneficiary_surname"]

        models.OwnedInvestmentsOver5KTableEntry.objects.get_or_create(
            loan_beneficiary=loan_beneficiary, **verified_data,
        )


@register_task()
class TaskOwnedInvestmentsOver5KTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsOver5KTable
    storage_model = models.OwnedInvestmentsOver5KTable
    child_tasks = [TaskOwnedInvestmentsOver5KRowEntry]


@register_task()
class TaskOwnedIncomeFromOtherSourcesRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesRowEntry
    template_name = "tasks/owned_income_other_sources.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromOtherSourcesTableEntry.objects.get_or_create(person=owner_person, **verified_data)


@register_task()
class TaskOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    child_tasks = [TaskOwnedIncomeFromOtherSourcesRowEntry]


@register_task()
class TaskOwnedJewelryRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedJewelryRowEntry
    template_name = "tasks/owned_jewelry.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        models.OwnedJewelryTableEntry.objects.get_or_create(**verified_data)


@register_task()
class TaskOwnedJewelryTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedJewelryTable
    storage_model = models.OwnedJewelryTable
    child_tasks = [TaskOwnedJewelryRowEntry]


@register_task()
class TaskExtraValuableRowEntry(RowEntryTask):
    task_form = forms.TranscribeExtraValuableRowEntry
    template_name = "tasks/owned_extra_valuable.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("owner_name"), surname=verified_data.get("owner_surname"),
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["owner_name"]
        del verified_data["owner_surname"]

        models.OwnedExtraValuableTableEntry.objects.get_or_create(
            receiver_of_goods=owner_person, **verified_data,
        )


@register_task()
class TaskExtraValuableTable(CountTableRowsTask):
    task_form = forms.TranscribeExtraValuableTable
    storage_model = models.OwnedExtraValuableTable
    child_tasks = [TaskExtraValuableRowEntry]


@register_task()
class TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsRowEntry
    template_name = "tasks/owned_income_from_deferred_use_of_goods.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromDeferredUseOfGoodsTableEntry.objects.get_or_create(
            person=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedIncomeFromDeferredUseOfGoodsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoodsTable
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    child_tasks = [TaskOwnedIncomeFromDeferredUseOfGoodsRowEntry]


@register_task()
class TaskOwnedIncomeFromIndependentActivitiesRowEntry(RowEntryTask):
    task_form = forms.TranscribeIndependentActivitiesRowEntry
    template_name = "tasks/owned_income_from_independent_activities.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromIndependentActivitiesTableEntry.objects.get_or_create(
            person=owner_person, **verified_data
        )


@register_task()
class TaskOwnedIncomeFromIndependentActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivitiesTable
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    child_tasks = [TaskOwnedIncomeFromIndependentActivitiesRowEntry]


@register_task()
class TaskOwnedIncomeFromGamblingRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingRowEntry
    template_name = "tasks/owned_income_from_gambling.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromGamblingTableEntry.objects.get_or_create(person=owner_person, **verified_data)


@register_task()
class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    child_tasks = [TaskOwnedIncomeFromGamblingRowEntry]


@register_task()
class TaskOwnedIncomeFromSalariesRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromSalariesRowEntry
    template_name = "tasks/owned_income_from_salaries.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromSalariesTableEntry.objects.get_or_create(
            person=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedIncomeFromSalariesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalariesTable
    storage_model = models.OwnedIncomeFromSalariesTable
    child_tasks = [TaskOwnedIncomeFromSalariesRowEntry]


@register_task()
class TaskOwnedBuildingsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedBuildingsRowEntry
    template_name = "tasks/owned_buildings_task.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("owner_name"), surname=verified_data.get("owner_surname"),
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["owner_name"]
        del verified_data["owner_surname"]

        models.OwnedBuildingsTableEntry.objects.get_or_create(
            coowner=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    child_tasks = [TaskOwnedBuildingsRowEntry]


@register_task()
class TaskOwnedIncomeFromInvestmentsRowEntry(RowEntryTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsRowEntry
    template_name = "tasks/owned_investments.html"

    def save_verified_data(self, verified_data):
        verified_data = super().save_verified_data(verified_data)

        # Use the custom form fields
        owner_person, created = models.Person.objects.get_or_create(
            name=verified_data.get("name"), surname=verified_data.get("surname")
        )

        # Remove the custom form fields before saving the table entry
        del verified_data["name"]
        del verified_data["surname"]

        models.OwnedIncomeFromInvestmentsTableEntry.objects.get_or_create(
            person=owner_person, **verified_data,
        )


@register_task()
class TaskOwnedIncomeFromInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromInvestmentsTable
    storage_model = models.OwnedIncomeFromInvestmentsTable
    child_tasks = [TaskOwnedIncomeFromInvestmentsRowEntry]
