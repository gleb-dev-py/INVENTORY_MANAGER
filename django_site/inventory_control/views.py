from django.shortcuts import render, HttpResponse


def base_version(request):
    return render(request, 'register.html')


def dark_version(request):
    return render(request, 'dark.html')
