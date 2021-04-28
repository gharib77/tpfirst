# Generated by Django 3.2 on 2021-04-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_alter_produit_dateprod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('date_entr', models.DateField()),
            ],
            options={
                'db_table': 'etudients',
            },
        ),
    ]