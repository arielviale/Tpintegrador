
from django.contrib import admin
from django.urls import path

from .views import AutoView
from .views import AutoAcerca
from .views import AutoCatalogo
from .views import AutoContacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", AutoView.as_view(), name = "inicio"),
    path("acerca/", AutoAcerca.as_view(), name="acerca"),
    path("catalogo/", AutoCatalogo.as_view(), name="catalogo"),
    path("contacto/", AutoContacto.as_view(), name="contacto"),
]
