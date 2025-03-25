# Generated by Django 5.1.7 on 2025-03-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('environnement', models.CharField(choices=[('IFS', 'IFS'), ('CFG', 'CFG')], default='IFS', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
