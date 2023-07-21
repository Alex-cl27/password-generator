from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'home.html',)


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upperChar = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special = list('!@#$%^&*')

    if request.GET.get('uppercase'):
        characters.extend(upperChar)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    length = int(request.GET.get('length', 8))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'password.html', {'password':thepassword})


def about(request):
    return render(request, 'about.html',)


# def testpage(request):
#     return HttpResponse('<h1>this is test page!</h1>')
