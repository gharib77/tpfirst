# Generated by Django 3.2 on 2021-04-22 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0016_article_facture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='facture',
        ),
    ]
