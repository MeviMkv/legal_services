# Generated by Django 4.2 on 2023-05-12 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_advocate_public_pro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocate',
            old_name='public_pro',
            new_name='public',
        ),
    ]
