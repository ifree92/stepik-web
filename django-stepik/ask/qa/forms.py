from django import forms


class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Ваша почта", widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Сообщение")

    def clean_email(self):
        print("[FeedbackForm]", "clean_email")
        email = self.cleaned_data["email"]
        if len(email) == 0:
            raise forms.ValidationError("Email is empty", code="email_error")
        return email

    def clean_message(self):
        print("[FeedbackForm]", "clean_message")
        message = self.cleaned_data["message"]
        if len(message) < 3:
            raise forms.ValidationError("Message cannot be empty", code="empty_message")
        return message

    def clean(self):
        print("[FeedbackForm]", "clean", self.cleaned_data)
        return self.cleaned_data

    def save(self):
        print("[FeedbackForm]", "save")

    def get_url(self):
        return "/"


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)


class AnswerForm(forms.Form):
    pass
