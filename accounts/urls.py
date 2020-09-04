from django.urls import path

from . import views
from .views import *  

urlpatterns = [
    path('home', AccountHomeView.as_view(), name='home'),
    path('details', UserDetailUpdateView.as_view(), name='user-update'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('dashboard', views.dashboard, name='dashboard')
]
