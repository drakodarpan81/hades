# Generated by Django 4.0.2 on 2022-03-23 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0010_alter_category_id_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='fec',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id_nombre',
        ),
        migrations.DeleteModel(
            name='Nombre',
        ),
    ]
