from django.contrib import admin
from django.urls import path, include

from .views import CocheBaseView, CocheListView, CocheDetailView, CocheCreateView, CocheUpdateView, CocheDeleteView, View, venta

app_name = "coche"

urlpatterns = [
    path("", CocheListView.as_view(), name="all"),
    path("venta/", venta.as_view(), name="venta"),
    path("create/", CocheCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CocheDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CocheUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CocheDeleteView.as_view(), name="delete")
]

urlpatterns += [
    path("venta/", views.venta, name="venta"),
    path("coche/", include("auto_app.urls")),
    path("admin/", admin.site.urls),
]
