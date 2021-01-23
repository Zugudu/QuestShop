from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={
		'autofocus': True,
		'class': 'w3-input',
		'placeholder': _('Username on server')
		}))
	password = forms.CharField(
		strip=False,
		widget=forms.PasswordInput(attrs={
			'autocomplete': 'current-password',
			'class': 'w3-input',
			'placeholder': _('Password from store')
			}),
	)