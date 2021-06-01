# Generated by Django 3.2.3 on 2021-06-01 09:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=64, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество на складе'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_desc',
            field=models.CharField(blank=True, max_length=64, verbose_name='краткое описание'),
        ),
    ]
