# Generated by Django 5.1.7 on 2025-03-25 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_produit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
    ]
