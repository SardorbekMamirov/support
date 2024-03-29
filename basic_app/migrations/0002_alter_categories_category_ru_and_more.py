# Generated by Django 4.0.4 on 2022-05-30 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_ru',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_uz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='basic_app.categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='complekt_ru',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='complekt_uz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='dis_price',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='ramka_ru',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='ramka_uz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='razmer_m',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='razmer_sm',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='recommendation_ru',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='recommendation_uz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='site',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='site',
            name='time_ru',
            field=models.CharField(blank=True, max_length=100, verbose_name='Рабочее времяxx'),
        ),
        migrations.AlterField(
            model_name='site',
            name='time_uz',
            field=models.CharField(blank=True, max_length=100, verbose_name='Рабочее времяxx'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='count',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='money',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='pool_frame',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='product_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
