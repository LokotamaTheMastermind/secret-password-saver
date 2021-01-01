from django import forms
from .models import Passwords


class PasswordsForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))
    website_url = forms.CharField(widget=forms.URLInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))
    website_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-form-width-large uk-input uk-width-expand'}))

    class Meta:
        model = Passwords
        fields = ['username', 'password', 'email',
                  'website_name', 'website_url']
