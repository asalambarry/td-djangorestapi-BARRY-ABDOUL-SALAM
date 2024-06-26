# research/forms.py

from django import forms
from .models import Chercheur, ProjetDeRecherche, Publication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class ChercheurForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        fields = '__all__'

class ProjetDeRechercheForm(forms.ModelForm):
    class Meta:
        model = ProjetDeRecherche
        fields = '__all__'

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
