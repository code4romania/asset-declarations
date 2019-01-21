from django import forms


class SimpleForm(forms.Form):
    title = forms.CharField(label="What is the title of the document?")
    non_readable = forms.BooleanField(label="I can't read it", required=False)
