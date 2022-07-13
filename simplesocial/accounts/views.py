from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, ListView
from . import models
from django.contrib.auth.models import User

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url: str = reverse_lazy('login')
    template_name: str = 'accounts/signup.html'

class UserList(ListView):
    model = models.User
    template_name: str = "accounts/user_list.html"

    def get_queryset(self):
        return User.objects.all()
    