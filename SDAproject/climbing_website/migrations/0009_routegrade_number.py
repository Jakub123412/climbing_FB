# Generated by Django 4.1.6 on 2023-03-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_website', '0008_alter_routereview_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='routegrade',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]