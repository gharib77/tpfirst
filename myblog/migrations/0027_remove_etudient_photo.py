# Generated by Django 3.2 on 2021-04-24 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_alter_etudient_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudient',
            name='photo',
        ),
    ]
