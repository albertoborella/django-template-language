from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from e_commerce.forms import ComicForm

# Importamos vistas genericas:
from django.views.generic import TemplateView, CreateView, ListView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

class PruebaView(TemplateView):
    template_name = 'e-commerce/base.html'


class TablaView(TemplateView):
    template_name = 'e-commerce/1.mi_tabla.html'


class ListaView(TemplateView):
    template_name = 'e-commerce/2.mi_lista.html'


class FormularioView(TemplateView):
    template_name = 'e-commerce/3.mi_formulario.html'


class TextoView(TemplateView):
    template_name = 'e-commerce/4.mi_texto.html'


class ImagenView(TemplateView):
    template_name = 'e-commerce/5.mi_imagen.html'


class ImgTextoView(TemplateView):
    template_name = 'e-commerce/img-texto.html'


class LoginView(TemplateView):
    template_name = 'e-commerce/login.html'

class DatosUser(TemplateView):
    model = User
    template_name = 'e-commerce/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user.username
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        context['email'] = self.request.user.email
        return context
    

class ComicsFavoritos(TemplateView):
    template_name = 'e-commerce/wish.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comic_favorito'] = ['Titulo 1','Titulo 5','Titulo 8', 'Titulo 12', 'Título 14']
        return context


class GuardarComicBD(CreateView):
    model = Comic
    fields = '__all__'
    template_name = 'e-commerce/guardar_comic_bd.html'



class Carrito(TemplateView):
    template_name = 'e-commerce/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comic_carrito'] = ['Titulo 1','Titulo 8', 'Título 14']
        return context


class Gracias(TemplateView):
    template_name = 'e-commerce/thanks.html'