# Generated by Django 4.0.2 on 2022-02-28 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_band_active_remove_band_biography_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='Fichier_a_mordre',
            new_name='Fichier',
        ),
    ]
