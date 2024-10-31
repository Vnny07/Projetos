from django.shortcuts import render
from sistema.models import TblUsuarios
from django.views.generic import ListView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView


def lista_usuarios(request):
    usuarios = TblUsuarios.objetos.all()

    # Incluímos no contexto
    contexto = {'usuarios': usuarios}

    return render(request, "templates/usuarios.html", contexto)

class ListaUsuarios(ListView):
    template_name = "templates/usuarios.html"
    model = TblUsuarios
    context_object_name = "usuarios"

def cria_usuario(request, pk):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuarios'))

    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})

class IndexTemplateView(TemplateView):
    template_name = "index.html"

class TblUsuariosListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class TblUsuariosUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = TblUsuarios
    fields = '__all__'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        usuario = None

    id = self.kwargs.get(self.pk_url_kwarg)
    slug = self.kwargs.get(self.slug_url_kwarg)
    if id is not None:
    usuario = TblUsuarios.objects.filter(id=id).first()

    return usuario

class TblUsuariosDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = TblUsuarios
    context_object_name = 'usuario'
    success_url = reverse_lazy(
        "website:lista_usuarios"
    )

class TblUsuariosCreateView(CreateView):
    template_name = "website/cria.html"
    model = TblUsuarios
    form_class = InsereTblUsuariosForm
    success_url = reverse_lazy("website:lista_usuarios")