from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View

from question.models import *
from question.forms import UserRegistrationForm, UserLoginForm, NewQuestionForm, UserSettingsForm, AnswerForm


def main(request):
    return redirect('index')

def index(request):
    # question = [0,1,2,3,4,5,6,7,8,9,
    #             0,1,2,3,4,5,6,7,8,9,
    #             0,1,2,3,4,5,6,7,8,9,
    #             0,1,2,3,4,5,6,7,8,9,
    #             0,1,2,3,4,5,6,7,8,9,
    #             0,1,2,3,4]
    #
    # return render(request, 'question/index.html',
    #                 {'questions' : paginator(request, objects_list = question)
    #                 })
	return render(request, 'question/index.html',
                  {'questions': paginator(request, objects_list=Question.objects.get_new()),
				   'headers': header_content("new")
				   })


def hot(request):
	return render(request, 'question/index.html',
				  {'questions': paginator(request, objects_list=Question.objects.get_hot()),
				   'headers': header_content("hot")
				   })


def tag(request, tag):
	return render(request, 'question/index.html',
				  {'questions': paginator(request, objects_list=Tag.objects.get_by_tag(tag_name=tag)),
				   'headers': header_content("tag", tag_name=tag)
				   })


# def tag(request,tag):
#     args = {}
#     args['tag'] = tag
#     args['questions'] = [1,2,3,4]
#     # args['questions'] = [1,2,3,4]
#     return render(request, 'question/tag.html', args)


def signin(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(request.GET.get('next') if request.GET.get('next') != '' else '/')
	else:
		form = UserLoginForm()
		logout(request)
	return render(request, 'question/login.html', {'form': form})


def signup(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data['password'])
			user.save()
			login(request, user)
			return redirect('/')
	else:
		form = UserRegistrationForm()
		logout(request)
	return render(request, 'question/signup.html', {'form': form})


def signout(request):
	if not request.user.is_authenticated:
		raise Http404
	logout(request)
	return redirect(request.GET['from'])


@login_required(login_url='/signin/')
def settings(request):
	user = get_object_or_404(User, username=request.user)

	if request.method == 'POST':
		form = UserSettingsForm(instance=user,
                               data=request.POST,
                               files=request.FILES
                              )
		if form.is_valid():
			form.save()
			# return profile(request, user.username)
	else:
		form = UserSettingsForm(instance=user)

	return render(request, 'question/settings.html', {'form': form})


def question(request, question_id):
    # question = [1]
    question = Question.objects.get_by_id(int(question_id)).first()
    # answer = [0,1,2,3,4,5,6,7,8,9,
    #           0,1,2,3,4,5,6,7,8,9,
    #           0,1,2,3,4,5,6,7,8,9,
    #           0,1,2,3]
    if question is not None:
        # answers = paginator(request, objects_list = answer)
        answers = paginator(request, objects_list=Answer.objects.get_hot_for_answer(question.id))
        return render(request, 'question/question.html',
                        {'question' : question,
                        'answers' : answers})
    else:
        raise Http404


@login_required(login_url='/signin/')
def new_question(request):
	if request.method == 'POST':
		form = NewQuestionForm(request.POST)
		if form.is_valid():
			ques = Question.objects.create(author=request.user,
							date=timezone.now(),
							is_active=True,
							title=form.cleaned_data['title'],
							text=form.cleaned_data['text'])
			ques.save()

			for tagTitle in form.cleaned_data['tags'].split():
				tag = Tag.objects.get_or_create(name=tagTitle)[0]
				ques.tags.add(tag)
				ques.save()
			return question(request, ques.id)
	else:
		form = NewQuestionForm()
	return render(request, 'question/ask.html', {'form': form})


@login_required(login_url='/signin/')
def new_answer(request, question_id):
	if Question.objects.filter(id=question_id).exists():
		if request.method == 'POST':
			form = AnswerForm(request.POST)
			if form.is_valid():
				answeredQuestion = Question.objects.get_by_id(question_id)[0]
				answer = Answer.objects.create(author=request.user,
								date=timezone.now(),
								text=form.cleaned_data['text'],
								question_id=answeredQuestion.id)
				answer.save()
				return redirect('/question/{}/#{}'.format(question_id, answer.id))
		else:
			form = AnswerForm()
		return render(request, 'question/answer.html', {'form': form})
	else:
		raise Http404


def profile(request, username):
	user = User.objects.by_username(username)
	if user is not None:
		return render(request, 'question/profile.html', {'profile': user})
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


def header_content(type, tag_name=""):
    if (type == "new"):
        content_header = [
            {'title': 'New Questions', 'url': 'index', 'is_active': True},
            {'title': 'Hot Questions', 'url': 'hot', 'is_active': False}
        ]
    if (type == "hot"):
        content_header = [
            {'title': 'New Questions', 'url': 'index', 'is_active': False},
            {'title': 'Hot Questions', 'url': 'hot', 'is_active': True}
        ]
    if (type == "tag"):
        content_header = [
            {'title': 'Tag: ' + tag_name, 'url': 'index', 'is_active': True},
        ]
    return content_header
