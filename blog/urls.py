from django.urls import path
from . import views

urlpatterns = [
    path('post-list', views.post_list, name='post-list'),
    path('post/<int:pk>/<str:slug>/', views.post_detail, name='post-detail'),
    path('post/edit/<int:pk>/', views.post_edit, name='post-edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post-delete'),
    path('post/create', views.post_create, name='post-create'),
    path('like/', views.like_post, name='like-post'),
    path('favourites/', views.post_favourite_list, name='post-favourite-list'),
]