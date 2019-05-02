"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from question.views import *

from .models import LikeDislike
from question.models import Question, Answer

urlpatterns = [
    url(r'^$', main, name='main'),

    url(r'^index/$', index, name='index'),
    url(r'^hot/$', hot, name='hot'),
    url(r'^tag/(?P<tag>.*)/$', tag, name='tag'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question, name='question'),
    url(r'^question/(?P<question_id>[0-9]+)/answer/$', new_answer, name='new_answer'),

    url(r'^signin/$', signin, name='signin'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signout/$', signout, name='signout'),

    url(r'^settings/$', settings, name='settings'),
    url(r'^ask/$', new_question, name='new_question'),

    url(r'^user/(?P<username>[a-zA-Zа-яА-Я_\-\.0-9]+?)$', profile, name='profile'),

    # url(r'^(\d+)/$', index, name='index'),
]
