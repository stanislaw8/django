# Generated by Django 3.2.3 on 2021-06-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210601_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
