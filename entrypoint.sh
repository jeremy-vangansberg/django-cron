#!/bin/bash

# Démarrer le service cron
cron

# Démarrer le serveur Django
python manage.py runserver 0.0.0.0:8000
