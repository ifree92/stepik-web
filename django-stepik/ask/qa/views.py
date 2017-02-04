from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse


def questions_main_newer(request):
    page = request.GET.get("page", 0)
    print(page)
    return HttpResponse("OKKK")


def questions_popular(request):
    page = request.GET.get("page", 0)
    print(page)
    return HttpResponse("Ok!")


def question_viewer(request, question):
    print("question:", question)
    return HttpResponse(question)


def test(request, num=""):
    return HttpResponse("<b>OK</b> " + num)
