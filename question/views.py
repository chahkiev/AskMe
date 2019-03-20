from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    args = {}
    args['questions'] = [1,2,3,4]
    return render(request, 'question/index.html', args)


def ask(request):
    args = {}
    # args['questions'] = [1,2,3,4]
    return render(request, 'question/ask.html', args)
