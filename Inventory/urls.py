from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Ruta para la vista de inicio
]
