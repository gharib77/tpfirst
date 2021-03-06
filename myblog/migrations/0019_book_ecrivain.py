# Generated by Django 3.2 on 2021-04-22 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_mouvement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecrivain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter field name', max_length=40)),
                ('age', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'ecrivains',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=13)),
                ('ecrivain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.ecrivain')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
