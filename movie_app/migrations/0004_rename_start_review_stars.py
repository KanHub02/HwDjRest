# Generated by Django 4.0.5 on 2022-06-25 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='start',
            new_name='stars',
        ),
    ]