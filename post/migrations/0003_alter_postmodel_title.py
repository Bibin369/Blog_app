# Generated by Django 4.1.13 on 2023-11-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_postmodel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
