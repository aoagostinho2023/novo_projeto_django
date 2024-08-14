from django.urls import path
from app_cad_usuarios import views
from app_cad_usuarios.views import run_migrations

urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('run-migrations/', run_migrations)
]