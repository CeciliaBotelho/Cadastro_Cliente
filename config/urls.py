from app_cadastro import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('editar_usuario/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id_usuario>/', views.deletar_usuario, name='deletar_usuario'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),  
]
