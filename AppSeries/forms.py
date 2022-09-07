from django import forms

class HBOForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()

class DisneyForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()