# Generated by Django 4.0.2 on 2022-03-18 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_category_fec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre categoria')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='id_nombre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='erp.nombre'),
            preserve_default=False,
        ),
    ]
