# Generated by Django 4.0.1 on 2023-03-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='team_badge',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
