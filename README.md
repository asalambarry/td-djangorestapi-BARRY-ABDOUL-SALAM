# Application de Suivi de Projets de Recherche avec Django

## Introduction

Ce projet vise à créer une application pour le suivi de projets de recherche, utilisant Django et Django REST Framework. L'application facilite la gestion des informations détaillées sur les projets de recherche, les chercheurs impliqués, et les publications associées.

## Objectifs et Fonctionnalités

### Objectifs
- **API Backend :** Développer une API robuste permettant la gestion efficace des projets de recherche, des chercheurs et des publications.
- **Frontend :** Créer une interface utilisateur élégante et fonctionnelle pour interagir avec l'API.

## Installation et Configuration

### Prérequis
- Python 3.x
- pip
- Virtualenv (recommandé)

### Étapes d'installation

1. Clonez le dépôt :
    ```bash
    git clone td-djangorestapi-BARRY-ABDOUL-SALAM
    cd td-djangorestapi-BARRY-ABDOUL-SALAM
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations :
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Créez un superutilisateur :
    ```bash
    python manage.py createsuperuser
    ```

6. Démarrez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

## Utilisation

### Authentification

L'application utilise JSON Web Tokens (JWT) pour l'authentification. Pour obtenir un token, utilisez le endpoint `/api/token/`.

1. Obtenir un token JWT :
    ```http
    POST http://127.0.0.1:8000/api/token/
    Content-Type: application/json

    {
      "username": "admin",
      "password": "admin"
    }
    ```

2. Utiliser le token dans les requêtes :
    Ajoutez le token dans les en-têtes de vos requêtes pour accéder aux endpoints protégés.
    ```http
    Authorization: Bearer <votre_token>
    ```

### Endpoints de l'API

- **Chercheurs :**
  - `GET /api/chercheurs/` - Liste des chercheurs
  - `POST /api/chercheurs/` - Créer un nouveau chercheur
  - `GET /api/chercheurs/{id}/` - Détails d'un chercheur
  - `PUT /api/chercheurs/{id}/` - Mettre à jour un chercheur
  - `DELETE /api/chercheurs/{id}/` - Supprimer un chercheur

- **Projets de Recherche :**
  - `GET /api/projets/` - Liste des projets
  - `POST /api/projets/` - Créer un nouveau projet
  - `GET /api/projets/{id}/` - Détails d'un projet
  - `PUT /api/projets/{id}/` - Mettre à jour un projet
  - `DELETE /api/projets/{id}/` - Supprimer un projet

- **Publications :**
  - `GET /api/publications/` - Liste des publications
  - `POST /api/publications/` - Créer une nouvelle publication
  - `GET /api/publications/{id}/` - Détails d'une publication
  - `PUT /api/publications/{id}/` - Mettre à jour une publication
  - `DELETE /api/publications/{id}/` - Supprimer une publication

### Interface Utilisateur

#### Inscription

1. Accédez à la page d'inscription : `http://127.0.0.1:8000/signup/`
2. Remplissez le formulaire et soumettez-le.
3. Vous serez redirigé vers la page d'accueil après la création de votre compte.

#### Connexion

1. Accédez à la page de connexion : `http://127.0.0.1:8000/login/`
2. Remplissez le formulaire de connexion et soumettez-le.
3. Vous serez redirigé vers la page d'accueil après la connexion.

#### Liste et gestion des chercheurs, projets et publications

- **Chercheurs :**
  - Accédez à la liste des chercheurs : `http://127.0.0.1:8000/chercheurs/`
  - Ajouter un chercheur : `http://127.0.0.1:8000/chercheurs/new/`
  - Modifier un chercheur : `http://127.0.0.1:8000/chercheurs/{id}/edit/`
  - Supprimer un chercheur : `http://127.0.0.1:8000/chercheurs/{id}/delete/`

- **Projets :**
  - Accédez à la liste des projets : `http://127.0.0.1:8000/projets/`
  - Ajouter un projet : `http://127.0.0.1:8000/projets/new/`
  - Modifier un projet : `http://127.0.0.1:8000/projets/{id}/edit/`
  - Supprimer un projet : `http://127.0.0.1:8000/projets/{id}/delete/`

- **Publications :**
  - Accédez à la liste des publications : `http://127.0.0.1:8000/publications/`
  - Ajouter une publication : `http://127.0.0.1:8000/publications/new/`
  - Modifier une publication : `http://127.0.0.1:8000/publications/{id}/edit/`
  - Supprimer une publication : `http://127.0.0.1:8000/publications/{id}/delete/`

## Tests

Un fichier `test.http` est inclus pour tester les différentes fonctionnalités de l'API.

### Exemple de requêtes dans `test.http`

```http
### Obtenir un token JWT
POST http://127.0.0.1:8000/api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin"
}

### Lister les chercheurs
GET http://127.0.0.1:8000/api/chercheurs/
Authorization: Bearer {{token}}

### Créer un chercheur
POST http://127.0.0.1:8000/api/chercheurs/
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "nom": "Jean Dupont",
  "specialite": "Physique"
}
