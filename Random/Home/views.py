from django.shortcuts import render
from django.http import HttpResponse
from Functions import generatenumber
from Functions import generatenumfromrange
from Functions import randomwfromt
from Functions import generatepassword
from Functions import gensetpassword
from .forms import RequestForm
from users.models import UserRequest
from django.contrib.auth.models import User
from django.utils import timezone

def home(request):
    if request.method == 'POST':
        if 'metod1button' in request.POST:
            if request.user.is_authenticated:
                a = request.POST.get("range1")
                b = request.POST.get("range2")
                res1 = generatenumber.genfromrange(int(a),int(b))
                new1 = UserRequest()
                new1.requester = request.user
                new1.type = 1
                new1.result = res1
                new1.request_time = timezone.now()
                new1.save()
                return render(request, 'Home/home.html', { 'reqnum1': new1 })
            else:
                a = request.POST.get("range1")
                b = request.POST.get("range2")
                res1 = generatenumber.genfromrange(int(a),int(b))
                context1 = {
                    'reqnum1': res1
                }
                return render(request, 'Home/home.html', context1)
        elif 'metod2button' in request.POST:
            if request.user.is_authenticated:
                a = request.POST.get("range11")
                b = request.POST.get("range21")
                c = request.POST.get("range31")
                res2 = generatenumfromrange.genfromrange3(int(a),int(b),int(c))
                new2 = UserRequest()
                new2.requester = request.user
                new2.type = 2
                new2.result = res2
                new2.request_time = timezone.now()
                new2.save()
                return render(request, 'Home/home.html', { 'reqnum2': new2 })
            else:
                a = request.POST.get("range11")
                b = request.POST.get("range21")
                c = request.POST.get("range31")
                res2 = generatenumfromrange.genfromrange3(int(a),int(b),int(c))
                context2 = {
                    'reqnum2': res2
                }
                return render(request, 'Home/home.html', context2)
        elif 'metod3button' in request.POST:
            if request.user.is_authenticated:
                text = request.POST.get("text")
                res3 = randomwfromt.randomword(text)
                new3 = UserRequest()
                new3.requester = request.user
                new3.type = 3
                new3.result = res3
                new3.request_time = timezone.now()
                new3.save()
                return render(request, 'Home/home.html', { 'reqnum3': new3 })
            else:
                text = request.POST.get("text")
                res3 = randomwfromt.randomword(text)
                context3 = {
                    'reqnum3': res3
                }
                return render(request, 'Home/home.html', context3)
        elif 'metod4button' in request.POST:
            if request.user.is_authenticated:
                length = request.POST.get("len41")
                res4 = generatepassword.genpassword(length)
                new4 = UserRequest()
                new4.requester = request.user
                new4.type = 4
                new4.result = res4
                new4.request_time = timezone.now()
                new4.save()
                return render(request, 'Home/home.html', { 'reqnum4': new4 })
            else:
                length = request.POST.get("len41")
                res4 = generatepassword.genpassword(length)
                context4 = {
                    'reqnum4': res4
                }
                return render(request, 'Home/home.html', context4)
        elif 'metod5button' in request.POST:
            if request.user.is_authenticated:
                numberpasswd = request.POST.get("numberpasswd")
                len = request.POST.get("len")
                res5 = gensetpassword.gensetpassword(int(numberpasswd),int(len))
                new5 = UserRequest()
                new5.requester = request.user
                new5.type = 5
                new5.result = res5
                new5.request_time = timezone.now()
                new5.save()
                return render(request, 'Home/home.html', { 'reqnum5': new5 })
            else:
                numberpasswd = request.POST.get("numberpasswd")
                len = request.POST.get("len")
                res5 = gensetpassword.gensetpassword(int(numberpasswd),int(len))
                context5 = {
                    'reqnum5': res5
                }
                return render(request, 'Home/home.html', context5)
        else:
            return render(request, 'Home/home.html')
    else:
        return render(request, 'Home/home.html')

    
