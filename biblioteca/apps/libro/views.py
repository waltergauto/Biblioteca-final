from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

#Importaciones para Vistas Basadas en Clases
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView

# Create your views here.

###VISTAS BASADAS EN FUNCIONES
"""
def index(request):
    return render(request, 'index.html')

def crearAutor(request):

    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        print(request.POST)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')

    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

def listarAutor(request):

    ###Trae todos los autores existentes en la base de datos
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autor.html', {'autores': autores})

def editarAutor(request, id):

    autor_form = None
    error = None

    try:
        autor = Autor.objects.get(id = id)
        
        #- Si el metodo es GET, estamos trayendo informacion de la base de datos, entonces para pintarlo
        #en el formulario con el form creado, le pasamos la instancia del modelo traido de la base de
        #datos, en este caso autor.      
        #- Si el metodo es POST, significa que ya se han hecho los cambios y se insertaran en la base de
        #datos, entonces se pasa el metodo y la instancia.
        
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)

            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as ex:
        error = ex

    
    #Se reutiliza el template crear_autor.html ya que posee los mismos cambos, a diferencia de que
    #en vez de pintar la instancia de autor, se pinta el form en el template.
    
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error} )

def eliminarAutorFisico(request, id):

    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})

def eliminarAutor(request, id):

    autor = Autor.objects.get(id = id)

    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html')
"""

###VISTAS BASADAS EN CLASES
class Inicio(TemplateView):

    template_name = 'index.html'

class ListadoAutor(ListView):

    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):

    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    succes_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):

    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

###DeleteView borra el registro de la base de datos, es decir, realiza una eliminacion fisica.
class EliminarAutor(DeleteView):

    model = Autor
    #success_url = reverse_lazy('libro:eliminar_autor') //no se puede utilizar reverse_lazy cuando se sobrescribe un metodo

    def post(self, request, pk, *args, **kwargs):

        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

class CrearLibro(CreateView):

    model = Libro
    template_name = 'libro/libro/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro_listar_libro')

class ListadoLibro(ListView):

    model = Libro
    template_name = 'libro/libro/listar_libro.html'
    queryset = Libro.objects.filter(estado = True)

class ActualizarLibro(UpdateView):

    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libro')

class EliminarLibro(DeleteView):

    model = Libro

    def post(self, rquest, pk, *args, **kwargs):

        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libro')


