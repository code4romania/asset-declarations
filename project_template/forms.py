from django import forms


class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(label="What is the name of the current politician?")
    surname = forms.CharField(label="What is the surname of the current politician?")


class SimpleForm(forms.Form):
    title = forms.CharField(label="What is the title of the document?")
    non_readable = forms.BooleanField(label="I can't read it", required=False)


class TranscribeNumberOfRowsPerTableForm(forms.Form):
    number_of_rows = forms.IntegerField(label="Cate randuri are acest tabel?")