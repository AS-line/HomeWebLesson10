from django.shortcuts import render, reverse, redirect
from .forms import CommentForm
from django.views.generic import FormView


class CommentFormView(FormView):
    form_class = CommentForm
    template_name = "comment.html"

    def form_valid(self, form):
        form.send_mail()
        return redirect(reverse('ok'))

    def form_invalid(self, form):
        print('Что то делаю')
        return super().form_invalid(form)
