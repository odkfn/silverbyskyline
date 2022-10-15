from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views
from .models import Post

app_name = 'silverbyskyline'
urlpatterns = [
    path('', views.silverbyskyline, name='silverbyskyline'),
    path('bandupdates/',
        ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:10],
            template_name="updates.html"          
            ),
        name='bandupdates'),
    path('bandupdates/<int:pk>/',
        DetailView.as_view(
            model = Post,
            template_name="post.html"
            )
        ),
]
