from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={
		'autofocus': True,
		'class': 'w3-input',
		'placeholder': 'Нік на сервері'
		}))
	password = forms.CharField(
		strip=False,
		widget=forms.PasswordInput(attrs={
			'autocomplete': 'current-password',
			'class': 'w3-input',
			'placeholder': 'Пароль від магазину'
			}),
	)