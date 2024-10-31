"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls.conf import include
from . import views
from django.views.generic import TemplateView
from sistema.views import IndexTemplateView
from sistema.views import TblUsuariosListView
from sistema.views import TblUsuariosUpdateView
from sistema.views import TblUsuariosDeleteView
from sistema.views import TblUsuariosCreateView

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),

    path('', include('web.urls', namespace='web')),
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name="index.html")),

    path('', IndexTemplateView.as_view(), name='index'),

    path('usuarios/', TblUsuariosListView.as_view(), name='lista_usuarios')

    path('usuarios/<id>', TblUsuariosUpdateView.as_view(), name='atualiza_usuario'),

    path('usuarios/excluir/<pk>', TblUsuariosDeleteView.as_view(), name='deleta_usuario')

    path('usuarios/cadastrar/', TblUsuariosCreateView.as_view(), name='cadastra_usuario'),
]
