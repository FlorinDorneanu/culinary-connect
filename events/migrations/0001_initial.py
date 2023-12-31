# Generated by Django 3.2.22 on 2023-10-17 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('recipe_share', 'Recipe Share'), ('cooking_challenge', 'Cooking Challenge'), ('food_photography', 'Food Photography'), ('restaurant_review', 'Restaurant Review'), ('cooking_tips', 'Cooking Tips'), ('food_event', 'Food Event'), ('culinary_workshop', 'Culinary Workshop'), ('other', 'Other')], default='Other', max_length=50)),
                ('image', models.ImageField(blank=True, default='../default_post_tiwu5f', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-event_date'],
            },
        ),
    ]
