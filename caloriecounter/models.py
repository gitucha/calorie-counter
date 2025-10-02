from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.calories} calories"