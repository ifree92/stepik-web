from django import forms
from .models import Feedback, Question, Answer
from django.contrib.auth.models import User


class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Ваша почта",
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Сообщение")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(email) == 0:
            raise forms.ValidationError("Email is empty", code="email_error")
        return email

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 3:
            raise forms.ValidationError("Message cannot be empty", code="empty_message")
        return message

    def clean(self):
        return self.cleaned_data

    def save(self):
        feedback = Feedback(email=self.cleaned_data["email"], text=self.cleaned_data["message"])
        feedback.save()
        return feedback

    def get_url(self):
        return "/"


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean_text(self):
        text = self.cleaned_data["text"]
        if len(text) == 0:
            raise forms.ValidationError("Text cannot be empty", code="text_error")
        return text

    def clean_question(self):
        question = self.cleaned_data["question"]
        if question <= 0:
            raise forms.ValidationError("Question is not correct", code="question_error")
        return question

    def save(self):
        id_question = self.cleaned_data["question"]
        text = self.cleaned_data["text"]
        question = Question.objects.get(id=id_question)
        answer = Answer(text=text, question=question, author=User.objects.get(id=1))
        answer.save()
