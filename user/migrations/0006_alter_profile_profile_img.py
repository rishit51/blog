# Generated by Django 3.2.4 on 2023-10-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_img',
            field=models.ImageField(default='profiles/default.png', upload_to='profiles'),
        ),
    ]