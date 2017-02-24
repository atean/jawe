from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def poll_index(request):
    template = loader('polls/index.html',)

def detail(request, question_id):
    pass

def vote(request, question_id):
    pass