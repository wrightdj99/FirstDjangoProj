from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

from .models import Question


# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join(q.question_text for q in latest_questions)
    return HttpResponse(output)
def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)
def results(request, question_id):
    return HttpResponse("This is the results page of question: %s" % question_id)
def vote(request, question_id):
    return HttpResponse("This is the vote page for question: %s" % question_id)