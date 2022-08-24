from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'.format(nome, idade))

def soma(request, num1, num2):
    resul = num1 + num2
    return HttpResponse('<h1>A soma de {} mais {} é igual a {}.'.format(num1, num2, resul))
