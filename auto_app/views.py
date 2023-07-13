from django.views           import View
from django.urls            import reverse_lazy
from django.views.generic   import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models                import Coche, Venta
from django.http            import HttpResponse
from django.shortcuts       import render


# !!!!FIJATE QUE TENES QUE TENER UNA BASE , SINO NO TE VA A FUNCIONAR
class CocheBaseView(View):
    template_name = 'coches.html'
    model = Coche
    fields = '__all__'
    success_url = reverse_lazy('coche:all')
    

class CocheListView(CocheBaseView,ListView):
    ...

    
""" 

class CocheDetailView(DetailView):
    model = Coche
    template_name = 'coche_detail.html'
    context_object_name = 'coche'

class CocheCreateView(CreateView):
    model = Coche
    template_name = 'coche_create.html'
    fields = '__all__'
    extra_context = {
        "tipo": "Create Coche"
    }
    success_url = reverse_lazy('coche:all')

class CocheUpdateView(UpdateView):
    model = Coche
    template_name = 'coche_create.html'
    fields = '__all__'
    extra_context = {
        "tipo": "Update coche"
    }
    success_url = reverse_lazy('coche:all') """
