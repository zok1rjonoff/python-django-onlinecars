# Generated by Django 5.0.4 on 2024-04-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='made_in',
            field=models.CharField(max_length=50),
        ),
    ]
