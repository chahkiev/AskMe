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


def tag(request,tag):
    args = {}
    args['tag'] = tag
    args['questions'] = [1,2,3,4]
    # args['questions'] = [1,2,3,4]
    return render(request, 'question/tag.html', args)


def login(request):
    args = {}
    return render(request, 'question/login.html', args)


def singup(request):
    args = {}
    return render(request, 'question/singup.html', args)

def settings(request):
    args = {}
    return render(request, 'question/settings.html', args)

def question(request,question):
    args = {}
    args['questions'] = [1,2,3,4]
    args['answers'] = [1,2]
    return render(request, 'question/question.html', args)
