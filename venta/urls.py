
from django.contrib import admin
from django.urls import path

from .views import AutoView
from .views import AutoAcerca
from .views import AutoCatalogo
from .views import AutoContacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", AutoView.as_view(), name = "inicio"),
    path("", AutoAcerca.as_view(), name = "acerca"),
    path("", AutoCatalogo.as_view(), name = "catalogo"),
    path("", AutoContacto.as_view(), name = "contacto"),
]
