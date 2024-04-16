from django.core.management.base import BaseCommand
from main.models import ScrapedData
import requests
import json

class Command(BaseCommand):
    help = 'Fetches the most recent data entry and makes an API call'

    def handle(self, *args, **options):
        # Récupérer la dernière entrée ajoutée selon la date de création
        last_entry = ScrapedData.objects.latest('created_at')
        
        # Créer le payload pour l'appel API avec les données de la dernière entrée
        payload = {
            "sepal_length": last_entry.sepal_length,
            "sepal_width": last_entry.sepal_width,
            "petal_length": last_entry.petal_length,
            "petal_width": last_entry.petal_width
        }

        

        headers = {'Content-Type': 'application/json'}
        
        payload = json.dumps(payload)

        print(payload)

        ### Fonction de netttoyage à rajouter

        # Faire un seul appel API avec les données de la dernière entrée
        response = requests.post('http://127.0.0.1:8000/api/predict/',
                                data=payload,
                                headers=headers)
        
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(f"API call successful: {response.json()}"))
        else:
            self.stdout.write(self.style.ERROR(f"API call failed: HTTP {response.status_code}"))
            self.stdout.write(self.style.ERROR(f"Response body: {response.text}"))
