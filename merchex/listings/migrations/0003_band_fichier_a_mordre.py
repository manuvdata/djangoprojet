# Generated by Django 4.0.2 on 2022-02-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='Fichier_a_mordre',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
