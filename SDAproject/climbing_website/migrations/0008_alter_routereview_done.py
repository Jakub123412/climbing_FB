# Generated by Django 4.1.6 on 2023-03-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_website', '0007_routereview_date_create_routereview_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routereview',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
