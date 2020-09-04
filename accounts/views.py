from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe

from .forms import *
from .mixins import *
from .models import *
from .signals import *
from contacts.models import *


class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'
    def get_object(self):
        return self.request.user



class LoginView(NextUrlMixin, RequestFormAttachMixin, SuccessMessageMixin, FormView):
    form_class = LoginForm
    success_url = '/accounts/dashboard'
    template_name = 'accounts/login.html'
    default_next = '/accounts/dashboard'
    success_message = "You have Logged in successfully"
 
    def form_valid(self, request):
        next_path = self.get_next_url()
        return redirect(next_path)


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login'
    success_message = "Your Registration was Successful"

class UserDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UserDetailChangeForm
    template_name = 'accounts/detail-update.html'
    

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Change Your Account Details'
        return context

    def get_success_url(self):
        return reverse('home')

    success_message = "You have Updated your credentials successfully"


def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  form = ProfileForm()

  context = {
    'contacts': user_contacts,
    'form': form
  }
  return render(request, 'accounts/dashboard.html', context)


