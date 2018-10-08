from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from . import views

from .models import Choice, Question

class IndexView(generic.ListView): template_name = 'polls/index.html' context_object_name = 'latest_question_list'

def get_queryset(self): return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): model = Question template_name = 'polls/detail.html'

class ResultView(generic.DetailView): model = Question template_name = 'polls/results.html'

def question(request, question_id):
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
