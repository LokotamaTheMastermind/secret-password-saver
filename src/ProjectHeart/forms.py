from django import forms
from .models import Passwords


class PasswordsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))
    website_url = forms.CharField(widget=forms.URLInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))
    website_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))

    class Meta:
        model = Passwords
        fields = ['password', 'website_name', 'website_url']
