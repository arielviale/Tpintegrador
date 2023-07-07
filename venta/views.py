from django.views.generic import TemplateView

class AutoView(TemplateView):
    template_name = "index.html"
class AutoAcerca(TemplateView):
    template_name = "acerca.html"
class AutoCatalogo(TemplateView):
    template_name = "catalogo.html"
class AutoContacto(TemplateView):
    template_name = "contacto.html"