# API Django avec Prédictions Iris et Tâches Automatisées

Ce projet est une API Django qui combine un modèle de prédiction pour les fleurs d'iris avec des tâches automatisées via cron. Il permet de faire des prédictions en temps réel via une API REST et d'automatiser la collecte et le traitement des données.

## Fonctionnalités

- API REST pour les prédictions de fleurs d'iris
- Tâches cron automatisées pour la collecte de données
- Interface d'administration Django
- Stockage des prédictions dans une base de données
- Conteneurisation avec Docker

## Prérequis

- Python 3.9+
- Docker (optionnel)
- pip

## Installation

### Installation locale

1. Cloner le repository :
```bash
git clone https://github.com/jeremy-vangansberg/simplon-django-cron.git
cd simplon-django-cron
```

2. Créer un environnement virtuel et l'activer :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix
# ou
.\venv\Scripts\activate  # Sur Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Lancer le serveur :
```bash
python manage.py runserver
```

### Installation avec Docker

1. Construire l'image :
```bash
docker build -t iris-api .
```

2. Lancer le conteneur :
```bash
docker run -p 8000:8000 iris-api
```

## Utilisation

### API Endpoints

- `POST /api/predict/` : Faire une prédiction
  ```json
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
  ```

- `GET /prediction/` : Voir la liste des prédictions

### Interface d'administration

1. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

2. Accéder à l'interface d'administration :
   - URL : `http://localhost:8000/admin/`

## Structure du Projet

```
simplon-django-cron/
├── hybrid_api_django/     # Configuration principale
├── prediction/           # App de prédiction
├── main/                # App principale
├── requirements.txt     # Dépendances
├── Dockerfile          # Configuration Docker
├── crontab             # Configuration des tâches cron
└── iris_model.pkl      # Modèle ML pré-entraîné
```

## Tâches Automatisées

Le projet inclut une tâche cron qui s'exécute toutes les minutes pour :
1. Récupérer les dernières données
2. Faire une prédiction via l'API
3. Sauvegarder les résultats

## Dépendances Principales

- Django < 5.0
- Django REST Framework
- scikit-learn
- pydantic
- celery
- requests

## Sécurité

⚠️ Note : En production, assurez-vous de :
- Changer la clé secrète Django
- Désactiver le mode DEBUG
- Configurer correctement ALLOWED_HOSTS
- Utiliser un serveur WSGI approprié (comme Gunicorn) 