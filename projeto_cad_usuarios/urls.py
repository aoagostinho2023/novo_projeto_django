from django.urls import path
from app_cad_usuarios import views
from app_cad_usuarios.views import run_migrations, chat_view

urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('run-migrations/', run_migrations),
    path('send_whatsapp_message/', views.send_whatsapp_message, name='send_whatsapp_message'),
    path('chat/', chat_view, name='chat')
]