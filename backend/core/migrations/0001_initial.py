# Generated by Django 5.1.2 on 2024-10-17 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ITTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ITRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='core.itteam')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('office_location', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='core.itteam')),
            ],
        ),
    ]