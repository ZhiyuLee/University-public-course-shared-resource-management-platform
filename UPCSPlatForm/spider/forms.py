# Begin
# auth:lby
# create date:7.18
# description: 爬取武大教务系统

from django import forms

class CookiesForm(forms.Form):
    Cookies = forms.CharField(label="cookies", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))