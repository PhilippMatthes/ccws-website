# Generated by Django 2.2.10 on 2020-02-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='authors',
            field=models.TextField(blank=True, null=True),
        ),
    ]
