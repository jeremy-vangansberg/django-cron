from django.db import models

class Prediction(models.Model):
    petal_length = models.FloatField()
    sepal_length = models.FloatField()
    petal_width = models.FloatField()
    sepal_width = models.FloatField()
    predicted_class = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prediction {self.predicted_class} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
