from django.views                 import View
from django.urls                  import reverse_lazy
from django.views.generic.list    import ListView
from django.views.generic.detail  import DetailView
from django.views.generic.edit    import CreateView, UpdateView, DeleteView

from .models                     import Coche
from django.http                 import HttpResponse



# !!!!FIJATE QUE TENES QUE TENER UNA BASE , SINO NO TE VA A FUNCIONAR
class CocheBaseView(View):
    template_name = 'coches.html'
    model         = Coche
    fields        = '__all__'
    success_url   = reverse_lazy('coche:all')
    
class CocheListView(CocheBaseView, ListView):    
    ...

    
class CocheDetailView(CocheBaseView, DetailView):
    model = Coche
    template_name = 'coche_detail.html'
    context_object_name = 'coche'

class CocheCreateView(CocheBaseView, CreateView):
    model = Coche
    template_name = 'coche_create.html'
    fields = '__all__'
    extra_context = {
        "tipo": "Create Coche"
    }
    success_url = reverse_lazy('coche:all')

class CocheUpdateView(CocheBaseView, UpdateView):
    model = Coche
    template_name = 'coche_create.html'
    fields = '__all__'
    extra_context = {
        "tipo": "Update coche"
    }
    success_url = reverse_lazy('coche:all')
class CocheDeleteView(CocheBaseView, DeleteView):
    model = Coche
    template_name = 'coche_create.html'
    fields = '__all__'
    extra_context = {
        "tipo": "Update coche"
    }
    success_url = reverse_lazy('coche:all')
