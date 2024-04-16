from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IrisFeaturesSerializer
import pickle
from pydantic import BaseModel, Field
from .models import Prediction

class IrisFeatures(BaseModel):
    petal_length: float = Field(..., gt=0)
    sepal_length: float = Field(..., gt=0)
    petal_width: float = Field(..., gt=0)
    sepal_width: float = Field(..., gt=0)

class PredictView(APIView):
    def post(self, request, format=None):
        # Utiliser DRF serializer pour valider les données
        serializer = IrisFeaturesSerializer(data=request.data)
        if serializer.is_valid():
            # Validation des données entrantes avec Pydantic
            try:
                features_data = IrisFeatures(**serializer.validated_data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # Charger le modèle (s'assurer que le chemin est correct)
            model = pickle.load(open('iris_model.pkl', 'rb'))

            # Préparer les données pour le modèle
            features = [features_data.sepal_length, features_data.sepal_width, features_data.petal_length, features_data.petal_width]

            # Faire la prédiction
            prediction = model.predict([features])[0]

            # Enregistrer la prédiction dans la base de données
            prediction_record = Prediction(
                petal_length=features_data.petal_length,
                sepal_length=features_data.sepal_length,
                petal_width=features_data.petal_width,
                sepal_width=features_data.sepal_width,
                predicted_class=prediction
            )
            prediction_record.save()

            # Renvoyer la prédiction
            return Response({'predicted_class': prediction}, status=status.HTTP_200_OK)
        else:
            # Si les données ne sont pas valides, renvoyer une erreur
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
