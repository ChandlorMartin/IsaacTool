# Generated by Django 5.0.1 on 2024-02-10 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IsaacTool', '0002_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='session_id',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
