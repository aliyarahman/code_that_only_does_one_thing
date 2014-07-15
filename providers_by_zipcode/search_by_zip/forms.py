from django import forms

class ZipForm(forms.Form):
	zipentered = forms.IntegerField()