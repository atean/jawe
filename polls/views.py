from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    pass
