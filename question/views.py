from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.core.paginator import Paginator


def index(request, page_number=1):
    args = {}
    all_questions = [0,1,2,3,4,5,6,7,8,9]
    questions_on_page = Paginator(all_questions, 3)
    args['questions_on_page'] = questions_on_page.page(page_number)
    args['current_page'] = page_number
    return render_to_response('question/index.html', args)



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
