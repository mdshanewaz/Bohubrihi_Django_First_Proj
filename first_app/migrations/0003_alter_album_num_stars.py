# Generated by Django 4.2.4 on 2023-08-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_rename_musicia_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Best'), (2, 'Better'), (3, 'Good'), (4, 'Bad'), (5, 'Worst')]),
        ),
    ]
