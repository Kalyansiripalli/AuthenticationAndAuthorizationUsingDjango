# Generated by Django 5.0.2 on 2024-03-03 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipeApp', '0002_receipe_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='User',
            new_name='user',
        ),
    ]
