from django.urls import path
from .views import AutoAcerca , AutoCatalogo ,AutoContacto, AutoView


urlpatterns = [
    path("", AutoView.as_view(), name="inicio"),
    path("acerca/", AutoAcerca.as_view(), name="acerca"),
    path("catalogo/", AutoCatalogo.as_view(), name="catalogo"),
    path("contacto/", AutoContacto.as_view(), name="contacto"),
    path("")
]
