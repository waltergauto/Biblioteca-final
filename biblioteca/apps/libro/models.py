from django.db import models

# Create your models here.

class Autor(models.Model):

    id = models.AutoField(primary_key = True)
    ###el campo blank hace referencia a si se puede dejar vacio el atributo nombre del modelo Autor
    ###el campo null hace referencia a si se puede colocar un valor null
    nombre = models.CharField('Nombre', max_length = 255, blank = False, null = False)
    apellido = models.CharField('Apellido', max_length=255, blank=False, null=False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripcion', blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length=255, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de Publicacion', blank = False, null = False)
    autor = models.ManyToManyField(Autor)
    ###el campo auto_now sirve para que se modifique el campo cada vez que se realice una creacion o modificacion
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

