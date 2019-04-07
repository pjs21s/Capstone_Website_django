from . import forms
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.


class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"

def profile(request):
    return render(request, 'accounts/profile.html')