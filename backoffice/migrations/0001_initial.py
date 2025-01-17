# Generated by Django 5.1.2 on 2024-10-16 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('au_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50, null=True)),
                ('year_born', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('pubid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('zip', models.CharField(max_length=15, null=True)),
                ('telephone', models.CharField(max_length=15, null=True)),
                ('fax', models.CharField(max_length=15, null=True)),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('title', models.CharField(max_length=255, null=True)),
                ('year_published', models.SmallIntegerField(null=True)),
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50, null=True)),
                ('notes', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('comments', models.TextField(null=True)),
                ('author', models.ManyToManyField(to='backoffice.authors')),
                ('pubid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.publishers')),
            ],
        ),
    ]
