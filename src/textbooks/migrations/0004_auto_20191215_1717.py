# Generated by Django 3.0 on 2019-12-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0003_textbook_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]