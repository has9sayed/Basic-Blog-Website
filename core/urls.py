from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_post, name='create'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_com'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='del_com'),
]