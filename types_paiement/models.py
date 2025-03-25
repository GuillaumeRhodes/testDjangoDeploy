from django.db import models

# Create your models here.
class TypePaiement(models.Model):
    ENV_CHOICES = [
        ('IFS', 'IFS'),
        ('CFG', 'CFG'),
    ]
    
    nom = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)
    environnement = models.CharField(max_length=3, choices=ENV_CHOICES, default='IFS')

    def __str__(self):
        return self.nom
