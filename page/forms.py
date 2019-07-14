from django import forms



class HomeForm(forms.Form):

    Name = forms.CharField()
    SSN = forms.CharField()
