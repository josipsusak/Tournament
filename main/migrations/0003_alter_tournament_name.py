# Generated by Django 4.1.7 on 2025-02-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, unique=True),
        ),
    ]
