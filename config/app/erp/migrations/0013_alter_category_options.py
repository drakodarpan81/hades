# Generated by Django 4.0.2 on 2022-03-30 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_alter_category_options_historicalcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
