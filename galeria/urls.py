from django.urls import path
from galeria.views import index, imagem, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro')
]