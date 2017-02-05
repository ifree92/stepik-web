from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer


@require_GET
def questions_main_newer(request):
    page = request.GET.get("page", 1)
    if int(page) <= 0:
        page = 1
    qs_questions = get_list_or_404(Question.objects.new())
    paginator = Paginator(qs_questions, 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    paginator.base_url = "/?page="
    return render(request, "questions.html", {
        "title": "User's questions",
        "questions": page.object_list,
        "page": page,
        "paginator": paginator
    })


@require_GET
def questions_popular(request):
    page = request.GET.get("page", 1)
    if int(page) <= 0:
        page = 1
    qs_questions = get_list_or_404(Question.objects.popular())
    paginator = Paginator(qs_questions, 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    paginator.base_url = "/popular/?page="
    return render(request, "questions.html", {
        "title": "User's questions",
        "questions": page.object_list,
        "page": page,
        "paginator": paginator
    })


@require_GET
def question_viewer(request, id_question):
    question = get_object_or_404(Question, id=id_question)
    answers = get_list_or_404(Answer.objects.from_old_to_new_by_question(question))
    return render(request, "question.html", {
        "title": question.title,
        "question": question,
        "answers": answers
    })


def test(request, num=""):
    return HttpResponse("<b>OK</b> " + num)
