from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


urlpatterns = [
    # NOTE: e_commerce base:
    path('base', PruebaView.as_view(), name='base'),
    
    #TODO: Tarea! 
    path('tabla', TablaView.as_view(), name='tabla'),
    path('lista', ListaView.as_view(), name='lista'),
    path('formulario', FormularioView.as_view(), name='formulario'),
    path('texto', TextoView.as_view(), name='texto'),
    path('imagen', ImagenView.as_view(), name='imagen'),
    path('img-texto', ImgTextoView.as_view(), name='img-texto'),
    path('login', LoginView.as_view(), name='login'),
    path('datos_user', DatosUser.as_view(), name='datos_user'),
    path('comics_favoritos', ComicsFavoritos.as_view(), name='comics_favoritos'),
    path('carrito', Carrito.as_view(), name='carrito'),
    path('gracias', Gracias.as_view(), name='gracias'),
    path('agregar-comics', GuardarComicBD.as_view(), name='agregar-comics'),
    ]