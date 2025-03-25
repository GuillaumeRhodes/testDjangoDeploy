from django.db import models

class Client(models.Model):
    ENV_CHOICES = [
        ('IFS', 'IFS'),
        ('CFG', 'CFG'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    environnement = models.CharField(max_length=3, choices=ENV_CHOICES, default='IFS')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
