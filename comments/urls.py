# comments/urls.py
from django.urls import path
from comments.views import create_comment, get_comments

urlpatterns = [
    path('', create_comment, name='create-comment'),
    path('<int:userId>/', get_comments, name='get-comments'),
]
