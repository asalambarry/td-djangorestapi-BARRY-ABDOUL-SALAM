# research/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChercheurViewSet, ProjetDeRechercheViewSet, PublicationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    home,
    create_chercheur, update_chercheur, delete_chercheur, list_chercheurs,
    create_projet, update_projet, delete_projet, list_projets,
    create_publication, update_publication, delete_publication, list_publications
)
router = DefaultRouter()
router.register(r'chercheurs', ChercheurViewSet)
router.register(r'projets', ProjetDeRechercheViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(router.urls)),

    path('', home, name='home'),  # Route pour la page d'accueil
    path('chercheurs/', list_chercheurs, name='chercheur_list'),
    path('chercheurs/new/', create_chercheur, name='chercheur_create'),
    path('chercheurs/<int:pk>/edit/', update_chercheur, name='chercheur_update'),
    path('chercheurs/<int:pk>/delete/', delete_chercheur, name='chercheur_delete'),

    path('projets/', list_projets, name='projet_list'),
    path('projets/new/', create_projet, name='projet_create'),
    path('projets/<int:pk>/edit/', update_projet, name='projet_update'),
    path('projets/<int:pk>/delete/', delete_projet, name='projet_delete'),


    path('publications/', list_publications, name='publication_list'),
    path('publications/new/', create_publication, name='publication_create'),
    path('publications/<int:pk>/edit/', update_publication, name='publication_update'),
    path('publications/<int:pk>/delete/', delete_publication, name='publication_delete'),
]
