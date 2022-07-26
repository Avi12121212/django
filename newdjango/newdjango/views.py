from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to new DJango")


def hello(request):
    return HttpResponse("Hello from DJango")


def avinash(request):
    return HttpResponse("hello Avinash singh")

def facebook(request):
    return HttpResponse("facebook")
