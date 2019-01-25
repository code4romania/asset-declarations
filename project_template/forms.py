from django import forms

YEAR_CHOICES = ('2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')


class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(label="What is the name of the current politician?")
    surname = forms.CharField(label="What is the surname of the current politician?")
    position = forms.CharField(label="What is the position of the current politician?")
    date = forms.CharField(label="Date", widget=forms.SelectDateWidget(years=YEAR_CHOICES))