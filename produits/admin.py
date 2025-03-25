from django.contrib import admin
from produits.models import Produit

# Register your models here.
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')