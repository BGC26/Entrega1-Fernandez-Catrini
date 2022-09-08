from django import forms

class NetflixForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()

class PrimeForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()
    
class HBOForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()

class DisneyForm(forms.Form):
    title = forms.CharField(max_length=300)
    qualification = forms.IntegerField()
    photo = forms.URLField()