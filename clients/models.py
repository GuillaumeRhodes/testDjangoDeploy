from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name