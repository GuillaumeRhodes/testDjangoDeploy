from django.contrib import admin
from clients.models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'environnement', 'created_at')
