# Generated by Django 4.0.2 on 2022-03-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_anniversaire_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversaire',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]