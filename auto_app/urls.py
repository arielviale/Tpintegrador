from django.urls     import path, include
from .views          import CocheListView

app_name = "coche"

urlpatterns = [
    path("", CocheListView.as_view(), name="all"),
]

