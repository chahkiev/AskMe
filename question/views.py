from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def main(request):
    return redirect('index')

def index(request):
    question = [0,1,2,3,4,5,6,7,8,9,
                0,1,2,3,4,5,6,7,8,9,
                0,1,2,3,4,5,6,7,8,9,
                0,1,2,3,4,5,6,7,8,9,
                0,1,2,3,4,5,6,7,8,9,
                0,1,2,3,4]

    return render(request, 'question/index.html',
                    {'questions' : paginator(request, objects_list = question)
                    })

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


def signup(request):
    args = {}
    return render(request, 'question/singup.html', args)

def settings(request):
    args = {}
    return render(request, 'question/settings.html', args)

def question(request, question_id):
    question = [1]
    answer = [0,1,2,3,4,5,6,7,8,9,
              0,1,2,3,4,5,6,7,8,9,
              0,1,2,3,4,5,6,7,8,9,
              0,1,2,3]
    if question is not None:
        answers = paginator(request, objects_list = answer)
        return render(request, 'question/question.html',
                        {'question' : question,
                        'answers' : answers})
    else:
        raise Http404


def paginator(request, objects_list):
        paginator = Paginator(objects_list, 10)
        page = request.GET.get('page')

        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        return objects
