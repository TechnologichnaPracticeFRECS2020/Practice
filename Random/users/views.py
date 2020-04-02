from django.shortcuts import render, redirect
from users.models import UserRequest
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('random-home')
    else:
        form = UserRegisterForm ()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def user(request):
    context = {
        'requestpage': UserRequest.objects.all()
    }
    return render(request, 'users/user.html', context)


def login(request):
    return render(request, 'Home/login.html')
