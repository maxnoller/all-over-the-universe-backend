from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class System(models.Model):
    name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    current_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class HyperspaceLane(models.Model):
    system_a = models.ForeignKey(System, on_delete=models.CASCADE, related_name='system_a')
    system_b = models.ForeignKey(System, on_delete=models.CASCADE, related_name='system_b')
    def __str__(self):
        return f'{self.system_a} - {self.system_b}'