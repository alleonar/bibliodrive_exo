# Generated by Django 5.1.2 on 2024-11-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='author',
            field=models.ManyToManyField(related_name='titles', to='backoffice.authors'),
        ),
    ]
