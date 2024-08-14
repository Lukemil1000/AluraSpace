from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
        fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
        return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
        return render(request, 'galeria/imagem.html')
