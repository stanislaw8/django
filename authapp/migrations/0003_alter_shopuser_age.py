# Generated by Django 3.2.3 on 2021-06-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='возраст'),
        ),
    ]
