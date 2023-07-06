from django.views.generic import TemplateView

class AutoView(TemplateView):
    template_name = "index.html"