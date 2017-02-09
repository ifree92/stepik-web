from django.contrib.auth.models import User
from django.db import models
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404, get_list_or_404


class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')

    def new_paginator(self, page):
        if int(page) <= 0:
            page = 1
        qs_questions = Question.objects.new()
        paginator = Paginator(qs_questions, 10)
        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        return page, paginator

    def popular(self):
        return Question.objects.order_by('-rating')

    def popular_paginator(self, page):
        if int(page) <= 0:
            page = 1
        qs_questions = Question.objects.popular()
        paginator = Paginator(qs_questions, 10)
        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        return page, paginator


class AnswerManager(models.Manager):
    def from_old_to_new_by_question(self, question):
        return Answer.objects.order_by('added_at').filter(question=question)


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    objects = AnswerManager()


class Feedback(models.Model):
    email = models.CharField(max_length=255)
    text = models.TextField()
