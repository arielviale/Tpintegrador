
from django.contrib import admin
from django.urls import path

from .views import AutoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", AutoView.as_view(), name = "inicio"),
]
