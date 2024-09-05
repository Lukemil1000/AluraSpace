from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")

    if "buscar" in request.GET:
        nome = request.GET["buscar"]
        fotografias = fotografias.filter(nome__icontains=nome)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": fotografia})

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})
