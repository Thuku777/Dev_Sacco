from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
    contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id )
    contact.save()

    messages.success(request, 'Submitted Successfully')
    return redirect('/accounts/dashboard')

