from django.shortcuts import redirect, render, get_object_or_404
from .models import Usuario
from .fuzzy import calcular_credito

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        idade = int(request.POST.get('idade', 0))
        renda_mensal = float(request.POST.get('renda_mensal', 0))
        novo_usuario = Usuario.objects.create(
            nome=request.POST.get('nome'),
            idade=idade,
            renda_mensal=renda_mensal,
            # O crédito é calculado diretamente aqui, não precisamos chamar save() duas vezes
            credito=calcular_credito(idade, renda_mensal)
        )
        return redirect('usuarios:listagem_usuarios')
    else:
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})


def deletar_usuario(request, id_usuario):
    # Busca o usuário no banco de dados
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    # Deleta o usuário
    usuario.delete()
    # Redireciona para a página de listagem de usuários após a exclusão
    return redirect('listagem_usuarios')

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = int(request.POST.get('idade', 0))
        usuario.renda_mensal = float(request.POST.get('renda_mensal', 0))
        # Recalcular o crédito após editar
        usuario.credito = calcular_credito(usuario.idade, usuario.renda_mensal)
        usuario.save()
        
        return redirect('listagem_usuarios')
    
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = int(request.POST.get('idade', 0))
        renda_mensal = float(request.POST.get('renda_mensal', 0))
        credito = calcular_credito(idade, renda_mensal)

        novo_usuario = Usuario.objects.create(
            nome=nome,
            idade=idade,
            renda_mensal=renda_mensal,
            credito=credito
        )
        return redirect('listagem_usuarios')
    return render(request, 'home.html')