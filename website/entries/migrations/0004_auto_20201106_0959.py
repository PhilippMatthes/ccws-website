# Generated by Django 3.0.8 on 2020-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_entry_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
