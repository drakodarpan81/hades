# Generated by Django 4.0.2 on 2022-03-20 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_nombre_category_id_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id_nombre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.nombre'),
        ),
    ]
