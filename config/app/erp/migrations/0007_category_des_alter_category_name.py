# Generated by Django 4.0.2 on 2022-03-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_category_client_detsale_product_sale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='des',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción de la categoria'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre categoria'),
        ),
    ]
