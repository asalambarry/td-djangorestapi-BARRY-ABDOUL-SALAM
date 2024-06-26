from django.shortcuts import render

# Create your views here.
# research/views.py

from rest_framework import viewsets
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer

from django.shortcuts import render, redirect
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

# research/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm
from .models import Chercheur, ProjetDeRecherche, Publication

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'research/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'research/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'research/login.html', {'form': form})

# Chercheur Views
def create_chercheur(request):
    if request.method == 'POST':
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chercheur_list')
    else:
        form = ChercheurForm()
    return render(request, 'research/chercheur_form.html', {'form': form})

def update_chercheur(request, pk):
    chercheur = get_object_or_404(Chercheur, pk=pk)
    if request.method == 'POST':
        form = ChercheurForm(request.POST, instance=chercheur)
        if form.is_valid():
            form.save()
            return redirect('chercheur_list')
    else:
        form = ChercheurForm(instance=chercheur)
    return render(request, 'research/chercheur_form.html', {'form': form})

def delete_chercheur(request, pk):
    chercheur = get_object_or_404(Chercheur, pk=pk)
    if request.method == 'POST':
        chercheur.delete()
        return redirect('chercheur_list')
    return render(request, 'research/chercheur_confirm_delete.html', {'chercheur': chercheur})

def list_chercheurs(request):
    chercheurs = Chercheur.objects.all()
    return render(request, 'research/chercheur_list.html', {'chercheurs': chercheurs})

# Projet Views
def create_projet(request):
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet_list')
    else:
        form = ProjetDeRechercheForm()
    return render(request, 'research/projet_form.html', {'form': form})

def update_projet(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet_list')
    else:
        form = ProjetDeRechercheForm(instance=projet)
    return render(request, 'research/projet_form.html', {'form': form})

def delete_projet(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('projet_list')
    return render(request, 'research/projet_confirm_delete.html', {'projet': projet})

def list_projets(request):
    projets = ProjetDeRecherche.objects.all()
    return render(request, 'research/projet_list.html', {'projets': projets})

# Publication Views
def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()
    return render(request, 'research/publication_form.html', {'form': form})

def update_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'research/publication_form.html', {'form': form})

def delete_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')
    return render(request, 'research/publication_confirm_delete.html', {'publication': publication})

def list_publications(request):
    publications = Publication.objects.all()
    return render(request, 'research/publication_list.html', {'publications': publications})
