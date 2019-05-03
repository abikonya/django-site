from django.shortcuts import render
from django.http import HttpResponse


def success(request):
    return HttpResponse('success')
