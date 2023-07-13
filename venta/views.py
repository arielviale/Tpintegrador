from django.views.generic import TemplateView, Venta

class AutoView(TemplateView):
    template_name = "index.html"
class AutoAcerca(TemplateView):
    template_name = "acerca.html"
class AutoCatalogo(TemplateView):
    template_name = "catalogo.html"
class AutoContacto(TemplateView):
    template_name = "contacto.html"

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