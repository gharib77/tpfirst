# Generated by Django 3.2 on 2021-04-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_alter_produit_dateprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='dateprod',
            field=models.DateField(null=True),
        ),
    ]
