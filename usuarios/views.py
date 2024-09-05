from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from galeria.models import Fotografia
from usuarios.forms import LoginForms, CadastroForms, FotografiaForms

# Create your views here.

def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            usuario = auth.authenticate(
                request,
                username=form["nome"].value(),
                password=form["senha"].value()
            )

            if usuario is not None:
                messages.success(request, "Logado com sucesso!")
                auth.login(request, usuario)
                return redirect("index")
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form["nome"].value()).exists():
                messages.error(request, "Usuário já existente")
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=form["nome"].value(),
                email=form["email"].value(),
                password=form["senha_1"].value()
            )

            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Usuário deslogado com sucesso!")
    return redirect("login")

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
        
    return render(request, "usuarios/nova_imagem.html", {"form": form})

def editar_imagem(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'usuarios/editar_imagem.html', {'form': form, 'id': id})
    
def deletar_imagem(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')