from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia esto a la ruta a la que quieres redirigir después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
