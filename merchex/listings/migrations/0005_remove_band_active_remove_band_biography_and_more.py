# Generated by Django 4.0.2 on 2022-02-28 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_band_fichier_a_mordre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='active',
        ),
        migrations.RemoveField(
            model_name='band',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='band',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='band',
            name='official_homepage',
        ),
        migrations.RemoveField(
            model_name='band',
            name='year_formed',
        ),
    ]