from django.contrib import admin
from django.urls import path , include

from .views import    CochesListView    \
                    , CochesDetailView  \
                    , CochesCreateView  \
                    , CochesUpdateView  \
                    , CochesDeleteView 
                    
app_name = 'coches' 

urlpatterns = [
    path("", CochesListView.as_view(), name="all"),
    path("create", CochesCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CochesDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CochesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CochesDeleteView.as_view(), name="delete")     
]
       
from django.contrib import admin
from django.urls import path , include

from .views import venta
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", Venta.as_view(), name="venta"),
    path("coches/", include("auto_app.urls")),
]     