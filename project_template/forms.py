import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from project_template import constants
from project_template.datamodels.declaration_type import DeclarationType
from project_template.datamodels.institution import Institution
from project_template.datamodels.position import Position
from project_template import models


def calculate_year_choices():
    start_date = 1980
    end_date = datetime.datetime.now().year
    return tuple(map(str, range(start_date, end_date + 1)))


def get_dict_year_choices():
    return [(date, date) for date in calculate_year_choices()]


class PartialModelForm(forms.ModelForm):
    """
    A standard Django ModelForm but with no save action
    """
    def save(self, *args, **kwargs):
        raise NotImplemented


class TranscribeInitialInformation(forms.Form):
    # Form fields for identifying the politician
    name = forms.CharField(label=_("Care este numele politicianului?"))
    previous_name = forms.CharField(label=_("Care este numele anterior al politicianului? (in cazul in care se aplica)"), required=False)
    initials = forms.CharField(label=_("Care sunt initialele politicianului? (in cazul in care se aplica)"), required=False)
    surname = forms.CharField(label=_("Care este prenumele politicianului?"))
    # Form fields for identifying the declaration
    position = forms.ChoiceField(label=_("Care este pozitia politicianului?"), choices=Position.return_as_iterable())
    date = forms.DateField(label=_("Care este data completării declarației de avere?"), widget=forms.SelectDateWidget(years=calculate_year_choices()), input_formats=['%Y-%m-%d'])
    institution = forms.ChoiceField(label=_("Care este institutia in cadrul careia lucra politicianul la data completarii declaratiei de avere?"),
                                        choices=Institution.return_as_iterable())
    declaration_type = forms.ChoiceField(label=_("Ce tip de declaratie este completata?"), choices=DeclarationType.return_as_iterable())


class TranscribeOwnedLandTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['land']), min_value=0)


class TranscribeOwnedLandRowEntry(PartialModelForm):
    # Custom form fields not found in the Model
    owner_surname = forms.CharField(label=_("Care este numele proprietarului?"))
    owner_name = forms.CharField(label=_("Care este prenumele proprietarului?"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a specific form field for a model field
        self.fields['acquisition_year'] = forms.ChoiceField(
            label=self.fields['acquisition_year'].label,
            choices=get_dict_year_choices)

    class Meta:
        model = models.OwnedLandTableEntry
        # Exclude the Model's table and coowner fields because they will be handled separately by the Task
        exclude = ['table', 'coowner']


class TranscribeOwnedBuildingsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}".format(constants.DECLARATION_TABLES['buildings']), min_value=0)


class TranscribeOwnedBuildingsRowEntry(PartialModelForm):
    # Custom form fields not found in the Model
    owner_surname = forms.CharField(label=_("Care este numele proprietarului?"))
    owner_name = forms.CharField(label=_("Care este prenumele proprietarului?"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a specific form field for a model field
        self.fields['acquisition_year'] = forms.ChoiceField(
            label=self.fields['acquisition_year'].label,
            choices=get_dict_year_choices)

    class Meta:
        model = models.OwnedBuildingsTableEntry
        # Exclude the Model's table and coowner fields because they will be handled separately by the Task
        exclude = ['table', 'coowner']
        # TODO: The 'address' model field doesn't seem to be used by the old form. Is it an overlook?
        exclude += ['address']


class TranscribeOwnedAutomobileTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['automobiles']), min_value=0)


class TranscribeOwnedAutomobileRowEntry(PartialModelForm):
    # No custom form fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a specific form field for a model field
        # TODO: A fabrication_year can be much older than the current acquisition_year dropdown allows
        self.fields['fabrication_year'] = forms.ChoiceField(
            label=self.fields['fabrication_year'].label,
            choices=get_dict_year_choices)

    class Meta:
        model = models.OwnedAutomobileTableEntry
        # Exclude the Model's table field because they will be handled separately by the Task
        exclude = ['table', ]


class TranscribeOwnedJewelryTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['jewelry']), min_value=0)


class TranscribeOwnedJewelryRowEntry(PartialModelForm):
    # No custom form fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a specific form field for a model field
        self.fields['acquisition_year'] = forms.ChoiceField(
            label=self.fields['acquisition_year'].label,
            choices=get_dict_year_choices)

    class Meta:
        model = models.OwnedJewelryTableEntry
        # Exclude the Model's table field because they will be handled separately by the Task
        exclude = ['table', ]


class TranscribeExtraValuableTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['extra_valuable']), min_value=0)


class TranscribeExtraValuableRowEntry(PartialModelForm):
    # Custom form fields not found in the Model
    owner_surname = forms.CharField(label=_("Care este numele persoanei catre care s-a instrainat bunul?"))
    owner_name = forms.CharField(label=_("Care este prenumele persoanei catre care s-a instrainat bunul?"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customise some field widgets
        self.fields['estrangement_date'] = forms.DateField(
            label=self.fields['estrangement_date'].label,
            widget=forms.SelectDateWidget(years=calculate_year_choices()),  # cannot use a callable for 'years'
            input_formats=['%Y-%m-%d'])

    class Meta:
        model = models.OwnedExtraValuableTableEntry
        # Exclude the Model's table and receiver_of_goods fields because they will be handled separately by the Task
        exclude = ['table', 'receiver_of_goods']
        # TODO: The 'address' model field doesn't seem to be used by the old form. Is it an overlook?
        exclude += ['address']


class TranscribeOwnedBankAccountsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['bank_accounts']), min_value=0)


class TranscribeOwnedBankAccountsRowEntry(PartialModelForm):
    # No custom form fields

    class Meta:
        model = models.OwnedBankAccountsTableEntry
        exclude = ['table', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customise a Model form field widget
        self.fields['opening_year'] = forms.ChoiceField(
            label=self.fields['opening_year'].label,
            choices=get_dict_year_choices)


class TranscribeOwnedInvestmentsOver5KTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['investments']), min_value=0)


class TranscribeOwnedInvestmentsOver5KRowEntry(PartialModelForm):
    # Custom form fields not found in the Model
    beneficiary_surname = forms.CharField(label=_("Care este numele beneficiarului?"))
    beneficiary_name = forms.CharField(label=_("Care este prenumele beneficiarului?"))

    class Meta:
        model = models.OwnedInvestmentsOver5KTableEntry
        # Exclude the Model's table and loan_beneficiary fields because they will be handled separately by the Task
        exclude = ['table', 'loan_beneficiary']


class TranscribeOwnedDebtsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['debts']), min_value=0)


class TranscribeOwnedDebtsRowEntry(PartialModelForm):
    # Custom form fields not found in the Model
    loaner_surname = forms.CharField(label="Care este numele creditorului?", required=False)
    loaner_name = forms.CharField(label="Care este prenumele creditorului?", required=False)

    class Meta:
        model = models.OwnedDebtsTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customise some Model form field widgets
        self.fields['acquirement_year'] = forms.ChoiceField(
            label=self.fields['acquirement_year'].label,
            choices=get_dict_year_choices)
        # TODO: due_date can also be in the future
        self.fields['due_date'] = forms.ChoiceField(
            label=self.fields['due_date'].label,
            choices=get_dict_year_choices)


class TranscribeOwnedGoodsOrServicesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['goods']), min_value=0)


class TranscribeOwnedGoodsOrServicesRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care este numele titularului?"))
    name = forms.CharField(label=_("Care este prenumele titularului?"))

    class Meta:
        model = models.OwnedGoodsOrServicesTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromSalariesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['salaries']), min_value=0)


class TranscribeOwnedIncomeFromSalariesRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei?"))
    name = forms.CharField(label=_("Care e prenumele persoanei?"))

    class Meta:
        model = models.OwnedIncomeFromSalariesTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeIndependentActivitiesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['independent_activities']), min_value=0)


class TranscribeIndependentActivitiesRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei care a realizat venitul?"))
    name = forms.CharField(label=_("Care e prenumele persoanei care a realizat venitul?"))

    class Meta:
        model = models.OwnedIncomeFromIndependentActivitiesTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromDeferredUseOfGoodsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['deferred_use']), min_value=0)


class TranscribeOwnedIncomeFromDeferredUseOfGoodsRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei care a realizat venitul?"))
    name = forms.CharField(label=_("Care e prenumele persoanei care a realizat venitul?"))

    class Meta:
        model = models.OwnedIncomeFromDeferredUseOfGoodsTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['income_investments']), min_value=0)


class TranscribeOwnedIncomeFromInvestmentsRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei care a realizat venitul?"))
    name = forms.CharField(label=_("Care e prenumele persoanei care a realizat venitul?"))

    class Meta:
        model = models.OwnedIncomeFromInvestmentsTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromPensionsTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['pensions']), min_value=0)


class TranscribeOwnedIncomeFromPensionsRowEntry(PartialModelForm):
    beneficiary_surname = forms.CharField(label=_("Care este numele beneficiarului?"))
    beneficiary_name = forms.CharField(label=_("Care este prenumele beneficiarului?"))

    class Meta:
        model = models.OwnedIncomeFromPensionsTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromAgriculturalActivitiesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['agriculture']), min_value=0)


class TranscribeOwnedIncomeFromAgriculturalActivitiesRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei?"))
    name = forms.CharField(label=_("Care e prenumele persoanei?"))

    class Meta:
        model = models.OwnedIncomeFromAgriculturalActivitiesTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromGamblingTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['gambling']), min_value=0)


class TranscribeOwnedIncomeFromGamblingRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei care a realizat venitul?"))
    name = forms.CharField(label=_("Care e prenumele persoanei care a realizat venitul?"))

    class Meta:
        model = models.OwnedIncomeFromGamblingTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']


class TranscribeOwnedIncomeFromOtherSourcesTable(forms.Form):
    count = forms.IntegerField(label="Câte rânduri completate există în tabelul {}?".format(constants.DECLARATION_TABLES['other_sources']), min_value=0)


class TranscribeOwnedIncomeFromOtherSourcesRowEntry(PartialModelForm):
    surname = forms.CharField(label=_("Care e numele persoanei care a realizat venitul?"))
    name = forms.CharField(label=_("Care e prenumele persoanei care a realizat venitul?"))

    class Meta:
        model = models.OwnedIncomeFromOtherSourcesTableEntry
        # Exclude the Model's table and person fields because they will be handled separately by the Task
        exclude = ['table', 'person']

