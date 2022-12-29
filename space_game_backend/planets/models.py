from django.db import models
from galaxy_map.models import System

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='planets')
    x = models.FloatField()
    y = models.FloatField()
    prefab = models.ForeignKey('PlanetPrefab', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    

class PlanetPrefab(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    