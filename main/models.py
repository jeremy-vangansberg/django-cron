from django.db import models

class ScrapedData(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {self.sepal_length}, {self.sepal_width}, {self.petal_length}, {self.petal_width}"
