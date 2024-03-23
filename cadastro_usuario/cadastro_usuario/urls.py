from app_cadastro import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página de registro
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    # Adicionando a nova URL para editar um usuário
    path('editar_usuario/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id_usuario>/', views.deletar_usuario, name='deletar_usuario'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),  # Novo caminho para registrar usuário

    
]
