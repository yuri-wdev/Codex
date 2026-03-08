"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import login
from dashboard.views import dashboard
from control.views import control,salvar_livro,editar_livro,remover_livro,salvar_emprestimo,devolver_emprestimo, salvar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login,name='login'),
    path('dash/', dashboard,name='dashboard'),
    path('control/', control, name='controle'),
    path('livro/salvar/', salvar_livro, name='salvar_livro'),
    path('livro/editar/', editar_livro, name='editar_livro'),
    path('livro/remover/', remover_livro, name='remover_livro'),
    path('emprestimo/salvar/', salvar_emprestimo, name='salvar_emprestimo'),
    path('emprestimo/devolver/', devolver_emprestimo, name='devolver_emprestimo'),
    path('cliente/salvar/', salvar_cliente, name='salvar_cliente'),
]