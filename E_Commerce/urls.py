from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('Admin.urls')),   # Esta línea redirige a la aplicación Admin para la raíz del sitio
]
