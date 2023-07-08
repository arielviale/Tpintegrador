from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Coches 

# Create your views here.

class CochesBaseView(View):
    template_name = 'coches.html'
    model = Coches
    fields = '__all__'
    success_url = reverse_lazy('coches:all')

class CochesListView(CochesBaseView, ListView):
    
    
class CochesDetailView(CochesBaseView, CreateView):
    template_name = 'coches_detail.html'
    
class CochesCreateView(CochesBaseView, CreateView):
    template_name = 'coches_create.html'
    extra_contex = {
        "tipo": "Crear coches"
    }    
class CochesUpdateView(CochesBaseView,UpdateView):
    template_name = 'coches_create.html'
    extra_contex = {
        "tipo": "Actualizar coches"
    }

class CochesDeleteView(CochesBaseView,DeleteView):
    template_name = 'coches_delete.html'
    extra_contex = {
        "tipo": "Borrar coches"
    }