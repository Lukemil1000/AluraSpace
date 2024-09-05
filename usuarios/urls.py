from django.urls import path
from usuarios.views import login, cadastro, logout, nova_imagem, editar_imagem, deletar_imagem

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('deletar_imagem/<int:id>', deletar_imagem, name='deletar_imagem'),
    path('editar_imagem/<int:id>', editar_imagem, name='editar_imagem'),
]