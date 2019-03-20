from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    args = {}
    return render(request, 'question/base.html', args)
