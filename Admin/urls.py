# Admin/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # Asegúrate de importar auth_views
from .views import home, login_view, register  # Asegúrate de que estas vistas existan

urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('login/', login_view, name='login'),  # Vista de inicio de sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Vista de cierre de sesión
    path('register/', register, name='register'),  # Vista de registro
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  # Vista de cambio de contraseña
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # Vista de confirmación de cambio de contraseña
]
