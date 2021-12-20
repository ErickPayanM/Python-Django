from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('movimientos/', views.movimientos, name='movimientos'),
    path('catalogo/<int:art_id>/', views.det_art, name='det_art'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)