# Partez d'une image Python officielle
FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

# Mettre à jour les paquets et installer cron
RUN apt-get update && apt-get install -y cron

# Définir le répertoire de travail
WORKDIR /app

# Ajouter les fichiers de l'application

COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN pip install -r requirements.txt

COPY . /app

# Ajouter le script cron au bon dossier
COPY crontab /etc/cron.d/my-cron-file
RUN chmod 0644 /etc/cron.d/my-cron-file
RUN crontab /etc/cron.d/my-cron-file

# Donner les droits d'exécution au script de démarrage
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Exposer le port sur lequel Django va s'exécuter
EXPOSE 8000

# Commande de lancement
CMD ["/entrypoint.sh"]