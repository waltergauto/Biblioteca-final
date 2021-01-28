# Generated by Django 3.1.5 on 2021-01-20 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellido',
            field=models.CharField(max_length=255, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=100, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicacion')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libro.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
