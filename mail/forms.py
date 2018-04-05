from django import forms
from django.core.mail import mail_admins, send_mail
from .models import Person


class CommentForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    text = forms.CharField(max_length=1024)

    def send_mail(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        text = self.cleaned_data.get('text')
        subject = 'Новый отзыв'
        message = '''Отзыв от {0}:
        {1}
        email: {2}'''.format(name, text, email)
        mail_admins(subject, message, )


class RequestForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "age", "email"]
