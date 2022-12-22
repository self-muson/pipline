from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse('hello world!')


def categories(request, testid):
    return HttpResponse(f'<h1>Testovaya stranica</h1><p>{testid}</p>')

def archive(request, year):
    if int(year)>2020:
        return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return redirect('home', permanent=True)
