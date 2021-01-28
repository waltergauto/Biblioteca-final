# Generated by Django 3.1.5 on 2021-01-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Autor')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido del Autor')),
                ('nacionalidad', models.CharField(max_length=100, verbose_name='Nacionalidad el autor')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
        ),
    ]
