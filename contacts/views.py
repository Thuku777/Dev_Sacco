from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail, get_connection
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView

from .models import Contact
from .forms import ContactForm, CompanyContactForm


def contact(request):
  submitted = False
  if request.method == 'POST':
    form = ContactForm(request.POST)
    # message = request.POST['message']
    if form.is_valid():
      cd = form.cleaned_data
      con = get_connection('django.core.mail.backends.console.EmailBackend')
      send_mail(
                cd['phone_number'],
                cd['message'],
                settings.EMAIL_HOST_USER,
                ['thukuelvys@gmail.com'],
                connection=con
             )
      messages.success(request, 'Your message was submitted successfully. Thank you.')
      return HttpResponseRedirect('contact?submitted=True')
    
  else: 
    form = ContactForm()
    if 'submitted' in request.GET:
      submitted = True
    
  context = {
    'form': form,
    'submitted': submitted
   }
  return render(request, 'contact.html', context)


