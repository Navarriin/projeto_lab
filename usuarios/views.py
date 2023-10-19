from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login

# criando function 'cadastro'
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        # checando se a senha e a confirmacao dela e igual
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')
        # checando se a senha tem pelo menos 6 caracteres
        elif len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve conter no minimo 6 caracteres')
            return redirect('/usuarios/cadastro')
       
        try:
            user = User.objects.create_user(
                first_name = primeiro_nome,
                last_name = ultimo_nome,
                username= username,
                email = email,
                password= senha
            )
                    
            messages.add_message(request, constants.SUCCESS, 'Usuario criado com sucesso!')
        except: 
            messages.add_message(request, constants.ERROR, 'Username existente')
            return redirect('/usuarios/cadastro')

        return redirect('/usuarios/cadastro')
    
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # armazenando user e password
        username= request.POST.get('username')
        senha = request.POST.get('senha')
        # validando user e pass
        user = authenticate(username= username, password= senha)
        
        if user:
           login(request, user)
           return redirect('/') # vai dar erro por enquanto 
        else: 
            messages.add_message(request, constants.ERROR, 'Usuario invalido')
            return redirect('/usuarios/login')
