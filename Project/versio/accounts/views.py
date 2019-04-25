from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
class Register(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"

class Profile(generic.DetailView):
    model = User
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/profile.html"


# def profile(request):
#     return render(request, 'accounts/profile.html')

# 회원가입 함수형_미완성
# def signup(request):
# ​    if request.method == 'POST':
# ​        form = SignUpForm(request.POST)
# ​        if form.is_valid():
# ​            form.save()
# ​            username = form.cleaned_data.get('username')
# ​            password = form.cleaned_data.get('password1')
# ​            user = authenticate(username = username, password = password)
# ​            login(request, user)
# ​            return redirect('index')
# ​    else:
# ​        form = SignUpForm()
# ​    return render(request, 'accounts/register.html', {'form':form})