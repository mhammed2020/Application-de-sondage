from django.shortcuts import render
from .models import Question, Choice
# Create your views here.
def index(request):
    context = {}
    return render(request, 'polls/index.html', context)