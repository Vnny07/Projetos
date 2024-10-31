from django.urls import path
from . import views

app_name = 'website'
# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
]