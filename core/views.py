from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from . import models
from . import forms

# Create your views here.
class ArtifactList(ListView):
	model = models.Artifact


class Login(LoginView):
	authentication_form = forms.LoginForm
	template_name = 'core/login.html'

class Logout(LogoutView):
	next_page = '/'