# Generated by Django 4.0.2 on 2022-03-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rename_fichier_a_mordre_band_fichier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
                ('cov', models.ImageField(blank=True, null=True, upload_to='books/covers')),
            ],
        ),
    ]
