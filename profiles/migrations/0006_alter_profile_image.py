# Generated by Django 3.2.22 on 2023-10-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_btl0op', upload_to='images/'),
        ),
    ]
