from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UseRegisterForm


def register(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан:можно войти на сайт.')
            return redirect('login')
    else:
        form = UseRegisterForm
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')
