from django import forms
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PeliculaForm (forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1"]

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]