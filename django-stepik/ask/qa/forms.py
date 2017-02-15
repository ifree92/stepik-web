from django import forms
from .models import Feedback, Question, Answer
from django.utils import timezone
import random
from django.contrib.auth.models import User


class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Your mail",
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Message")

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
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) == 0:
            print("AskForm clean_title raise ValidationError");
            raise forms.ValidationError("Title cannot be empty", code="title_error")
        return title

    def clean_text(self):
        text = self.cleaned_data["text"]
        if len(text) == 0:
            print("AskForm clean_text raise ValidationError");
            raise forms.ValidationError("Text cannot be empty", code="text_error")
        return text

    def clean(self):
        return self.cleaned_data

    def save(self):
        title = self.cleaned_data["title"]
        text = self.cleaned_data["text"]
        q = Question(title=title, text=text, added_at=timezone.now(), rating=random.randint(0, 100))
        q.save()
        return q.id


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
        answer = Answer(text=text, question=question)
        answer.save()


class UserRegister(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), max_length=100)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 5:
            raise forms.ValidationError("Username should be longer than 5 symbols")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(email) < 4:
            raise forms.ValidationError("Email field is not correct")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 5:
            raise forms.ValidationError("Password should be longer than 5 symbols")
        return password

    def save(self):
        user = User(username=self.cleaned_data["username"], email=self.cleaned_data["email"], password=self.cleaned_data["password"])
        user.save()


class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), max_length=100)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 5:
            raise forms.ValidationError("Username should be longer than 5 symbols")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 5:
            raise forms.ValidationError("Password should be longer than 5 symbols")
        return password

    def get_user(self):
        return User.objects.get(username=self.cleaned_data["username"], password=self.cleaned_data["password"])
