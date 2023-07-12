from django.contrib import admin
from django.urls import path , include

from .views import   CocheListView    ,\
                     CocheDetailView ,\
                     CocheCreateView ,\
                     CocheUpdateView ,\
                     CocheDeleteView 
                    
app_name = "coche" 

urlpatterns = [
    path("", CocheListView.as_view(), name="all"),
    path("create/", CocheCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CocheDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CocheUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CocheDeleteView.as_view(), name="delete")     
]
       
from django.contrib import admin
from django.urls    import path , include

from .views         import coche
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("", coche.as_view(), name="venta"),
    path("coche/", include("auto_app.urls")),
]     