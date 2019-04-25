from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name ='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('profile/<int:pk>', views.Profile.as_view(), name="profile"),
]