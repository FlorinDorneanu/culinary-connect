# Generated by Django 3.2.22 on 2023-10-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Recipe Share', 'Recipe Share'), ('Cooking Challenge', 'Cooking Challenge'), ('Food Photography', 'Food Photography'), ('Restaurant Review', 'Restaurant Review'), ('Cooking Tips', 'Cooking Tips'), ('Food Event', 'Food Event'), ('Culinary Workshop', 'Culinary Workshop'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]