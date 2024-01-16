from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Me! <br> <a href = ' / '> Back </a>")


def contact(request):
    return HttpResponse("Contact Me! <br> <a href = ' / '> Back </a>")


def hire_me(request):
    return HttpResponse("Please Hire Me! <br> <a href = ' / '> Back </a>")


def thanks(request):
    djmsg = request.GET.get('message', 'default message')
    print(djmsg)
    return HttpResponse("Thanks for leaving a message! <br> <a href = ' / '> Back </a>")
