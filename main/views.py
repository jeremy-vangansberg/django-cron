from django.shortcuts import render
from prediction.models import Prediction

def prediction_list_view(request):
    # Récupérer toutes les prédictions de la base de données
    predictions = Prediction.objects.all()
    # Renvoyer une réponse HTML en utilisant un template
    return render(request, 'main/prediction_page.html', {'predictions': predictions})
