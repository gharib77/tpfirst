# Generated by Django 3.2 on 2021-04-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_auto_20210422_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouvement',
            name='article',
        ),
        migrations.RemoveField(
            model_name='mouvement',
            name='facture',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Facture',
        ),
        migrations.DeleteModel(
            name='Mouvement',
        ),
    ]
