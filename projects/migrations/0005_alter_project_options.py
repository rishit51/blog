# Generated by Django 3.2.4 on 2023-07-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
