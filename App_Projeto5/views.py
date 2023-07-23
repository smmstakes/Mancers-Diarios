from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from App_Projeto5.models import Diario

def home(request):
    return render(request, "App_Projeto5/base/home.html")


def contact(request):
    return render(request, "App_Projeto5/base/contact.html")


def pag_login(request):
    return render(request, "App_Projeto5/login/pag_login.html")


def login_verif(request):
    if request.method == 'POST':
        usuario = request.POST.get('nickname')
        senha = request.POST.get('senha')
        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            
            if user.is_superuser:
                return redirect('/admin/')  
            else:
                return redirect('pag_user1')  
            
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            return render(request, 'App_Projeto5/login/pag_login.html', {'error_message': error_message})
    else:
        return render(request, 'App_Projeto5/login/pag_login.html')


def pag_register(request):
    return render(request, "App_Projeto5/login/pag_register.html")


def register_verif(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        
        usuario = User.objects.create_user(username=nickname, password=senha)
        usuario.nome = nome
        usuario.email = email
        usuario.save()

        return redirect('pag_login') 
    else:
        return render(request, 'App_Projeto5/login/pag_register.html')
    

def deslogar(request):
    logout(request)
    return redirect('home')


def pag_user1(request):
    return render(request, "App_Projeto5/core/pag_user1.html")


def visualizar_entradas(request):
    entradas = Diario.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'App_Projeto5/diario/visualizar_entradas.html', {'entradas': entradas})


def criar_entrada(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        entrada = Diario(usuario=request.user, titulo=titulo, texto=texto)
        entrada.save()
        return redirect('visualizar_entradas')
    else:
        return render(request, 'App_Projeto5/diario/criar_entrada.html')


def editar_entrada(request, entrada_id):
    entrada = get_object_or_404(Diario, id_Diario=entrada_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        entrada.titulo = titulo
        entrada.texto = texto
        entrada.save()
        return redirect('visualizar_entradas')
    else:
        return render(request, 'App_Projeto5/diario/editar_entrada.html', {'entrada': entrada})


def excluir_entrada(request, entrada_id):
    entrada = get_object_or_404(Diario, id_Diario=entrada_id)
    entrada.delete()
    return redirect('visualizar_entradas')


def pag_inicial(request):
    if request.user.is_authenticated:
        return pag_user1(request)
    else:
        return home(request)  


def contact_user(request):
    return render(request, "App_Projeto5/diario/contact_user.html")

