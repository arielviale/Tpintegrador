from .models       import Coche
from django.urls   import reverse_lazy
from django.views.generic import View

from auto_app.models import Coche, Venta
from django.views.generic.list     import ListView
from django.views.generic.edit     import DeleteView, UpdateView, CreateView
from django.views.generic.detail   import DetailView

from auto_app.models  import Venta 
from django.urls import path
class CocheBaseView(View):
    template_name = 'coche.html'
    model       = Coche
    fields      = '__all__'
    success_url = reverse_lazy('coche:all')

class CocheListView(CocheBaseView, ListView):
    ...
        
    
class CocheDetailView(CocheBaseView, DetailView):
    template_name = 'coche_detail.html'
    
    
class CocheCreateView(CocheBaseView, CreateView):
    template_name = 'coche_create.html'
    extra_contex = {
        "tipo": "Create Coche"
    }    
class CocheUpdateView(CocheBaseView,View):
    template_name = 'coche_create.html'
    extra_contex = {
        "tipo": "Update coche"
    }

class CocheDeleteView(CocheBaseView,View):
    template_name = 'coche_delete.html'
    extra_contex = {
        "tipo": "Delete coche"
    }
class VentaView(View):
    def get(self, request):
        # Lógica para mostrar la página de venta de coches
        return render(request, 'venta.html')

    def post(self, request):
        # Lógica para procesar la venta de un coche
        return HttpResponse('Venta procesada correctamente')

urlpatterns = [
    path("venta/", VentaView.as_view(), name="venta"),
    # ...
]