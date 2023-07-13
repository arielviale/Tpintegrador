from django.contrib  import admin
from .views          import VentaView



from django.urls     import path, include
from .views          import CocheListView, CocheDetailView, CocheCreateView, CocheUpdateView, CocheDeleteView, VentaView

app_name = "coche"

urlpatterns = [
    path("", CocheListView.as_view(), name="all"),
    path("venta/", VentaView.as_view(), name="venta"),
    path("create/", CocheCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CocheDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CocheUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CocheDeleteView.as_view(), name="delete")
]

