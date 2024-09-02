from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from usuarios.forms import LoginForms, CadastroForms

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
                auth.login(request, usuario)
                return redirect("index")
            else:
                return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect("cadastro")
            
            if User.objects.filter(username=form["nome"].value()).exists():
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=form["nome"].value(),
                email=form["email"].value(),
                password=form["senha_1"].value()
            )

            usuario.save()
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})
