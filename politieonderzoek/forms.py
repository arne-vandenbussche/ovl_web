from django import forms
from .models import Politieterm, Auto, Persoon

class PolitietermSearchForm(forms.Form):
    afkorting = forms.CharField(label="zoekwaardafkorting", max_length=10)

class AutoSearchForm(forms.Form):
    nummerplaat = forms.CharField(label="nummerplaat", max_length=20)

class PersoonSearchForm(forms.Form):
    zoektermpersoon = forms.CharField(label="zoektermpersoon", max_length=150)
