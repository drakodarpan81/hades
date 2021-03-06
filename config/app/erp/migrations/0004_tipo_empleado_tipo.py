# Generated by Django 4.0.2 on 2022-03-14 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_remove_empleado_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del tipo:')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'tipo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='erp.tipo'),
            preserve_default=False,
        ),
    ]
