# Generated by Django 3.2 on 2021-04-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_grade_personne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lib_unt', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'unites',
            },
        ),
    ]
