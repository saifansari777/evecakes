from django.shortcuts import render
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm
from .forms import Newloginform


class Userlogin(LoginView):
	template_name = 'user/login.html'
	form = Newloginform