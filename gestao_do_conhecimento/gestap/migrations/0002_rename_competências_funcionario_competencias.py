# Generated by Django 4.2.2 on 2023-07-01 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='competências',
            new_name='competencias',
        ),
    ]
