from rest_framework import serializers

class IrisFeaturesSerializer(serializers.Serializer):
    petal_length = serializers.FloatField()
    sepal_length = serializers.FloatField()
    petal_width = serializers.FloatField()
    sepal_width = serializers.FloatField()