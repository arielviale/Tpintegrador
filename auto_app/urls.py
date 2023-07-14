from django.urls     import path
from .views          import CocheListView ,\
                            CocheDetailView ,\
                            CocheUpdateView ,\
                            CocheDeleteView ,\
                            CocheCreateView

app_name = "coche"

urlpatterns = [
    path("", CocheListView.as_view(), name="all"),
    path("<int:pk>/detail/", CocheDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CocheUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CocheDeleteView.as_view(), name="delete"),
    path("create/", CocheCreateView.as_view(), name="create"),
]

