from django.urls import path
from usuarios.views import login, cadastro, logout, nova_imagem

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('nova_imagem', nova_imagem, name='nova_imagem')
]