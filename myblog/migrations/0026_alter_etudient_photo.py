# Generated by Django 3.2 on 2021-04-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_auto_20210424_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudient',
            name='photo',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
