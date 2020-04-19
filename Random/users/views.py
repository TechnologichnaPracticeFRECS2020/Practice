from django.shortcuts import render, redirect
from users.models import UserRequest
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from Functions.generatenumber import genfromrange

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('random-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def user(request):
    context = {
        'requestpage': UserRequest.objects.filter(requester=request.user).order_by('-request_time'),
        'type1': UserRequest.objects.filter(requester=request.user).filter(type=1),
        'type2': UserRequest.objects.filter(type=2).filter(requester=request.user),
        'type3': UserRequest.objects.filter(type=3).filter(requester=request.user),
        'type4': UserRequest.objects.filter(type=4).filter(requester=request.user),
        'type5': UserRequest.objects.filter(type=5).filter(requester=request.user),
    }
    if request.method == 'POST':
        if 'randombutton' in request.POST:
            a = UserRequest.objects.first().id
            b = UserRequest.objects.last().id
            result = genfromrange(a, b)
            context['randomhistory']= UserRequest.objects.filter(id=result)
    return render(request, 'users/user.html', context)


def login(request):
    return render(request, 'Home/login.html')
