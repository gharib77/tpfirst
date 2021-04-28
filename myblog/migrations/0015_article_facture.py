# Generated by Django 3.2 on 2021-04-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_etudient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40)),
                ('prix', models.IntegerField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=45)),
                ('date_fact', models.DateField()),
            ],
            options={
                'db_table': 'factures',
            },
        ),
    ]
