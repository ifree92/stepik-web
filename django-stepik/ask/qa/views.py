from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Answer
from .forms import FeedbackForm, AnswerForm, AskForm, UserRegister, UserLogin
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError


@require_GET
def questions_main_newer(request):
    page = request.GET.get("page", 1)
    page, paginator = Question.objects.new_paginator(page)
    paginator.base_url = "/?page="
    return render(request, "questions.html", {
        "title": "User's questions sorted by date",
        "questions": page.object_list,
        "page": page,
        "paginator": paginator
    })


@require_GET
def questions_popular(request):
    page = request.GET.get("page", 1)
    page, paginator = Question.objects.popular_paginator(page)
    paginator.base_url = "/popular/?page="
    return render(request, "questions.html", {
        "title": "User's questions sorted by rating",
        "questions": page.object_list,
        "page": page,
        "paginator": paginator
    })


@csrf_exempt
def ask(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    if request.method == "GET":
        ask_form = AskForm()
        return render(request, "ask.html", {
            "title": "Ask a question",
            "ask_form": ask_form
        })
    if request.method == "POST":
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            question_id = ask_form.save(user=request.user)
            return HttpResponseRedirect("/question/" + str(question_id) + "/")
        else:
            ask_form = AskForm()
            return render(request, "ask.html", {
                "title": "Ask a question",
                "ask_form": ask_form
            })
    else:
        raise Http404()


@csrf_exempt
def question_viewer(request, id_question):
    if request.method == "GET":
        question = get_object_or_404(Question, id=id_question)
        answers = Answer.objects.from_old_to_new_by_question(question)
        form_answer = AnswerForm(initial={"question": id_question})

        return render(request, "question.html", {
            "title": question.title,
            "question": question,
            "answers": answers,
            "form_answer": form_answer,
            "user": request.user
        })
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login/")
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.set_user(request.user)
            answer_form = form.save(user=request.user)

            return HttpResponseRedirect("/question/" + str(form.cleaned_data["question"]) + "/")
        else:
            question = get_object_or_404(Question, id=id_question)
            answers = Answer.objects.from_old_to_new_by_question(question)
            form_answer = AnswerForm(initial={"question": id_question})
            return render(request, "question.html", {
                "title": question.title,
                "question": question,
                "answers": answers,
                "form_answer": form_answer,
                "user": request.user
            })
    else:
        raise Http404()


@csrf_exempt
def signup(request):
    if request.method == "GET":
        register_form = UserRegister()
        return render(request, "signup.html", {
            "title": "User's registration",
            "register_form": register_form
        })
    if request.method == "POST":
        register_form = UserRegister(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "signup.html", {
                "title": "User's registration",
                "register_form": register_form
            })


@csrf_exempt
def signin(request):
    if request.method == "GET":
        login_form = UserLogin()
        return render(request, "signin.html", {
            "title": "User login",
            "login_form": login_form
        })
    if request.method == "POST":
        login_form = UserLogin(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data["username"],
                                password=login_form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, "signin.html", {
                    "title": "User login",
                    "login_form": login_form,
                    "alerts": {"danger": ["Incorrect login or password"]}
                })
        else:
            return render(request, "signin.html", {
                "title": "User login",
                "login_form": login_form
            })


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_post = form.save()
            url = form.get_url()
            return HttpResponseRedirect(url)
        else:
            return render(request, "feedback.html", {
                "title": "Feedback form",
                "form": form
            })
    else:
        form = FeedbackForm
        return render(request, "feedback.html", {
            "title": "Feedback form",
            "form": form
        })


def test(request, num=""):
    return HttpResponse("<b>OK</b> " + num)
