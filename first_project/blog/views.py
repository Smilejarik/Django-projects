from django.shortcuts import render
from .models import Post

posts = Post.objects.all()
"""
posts = [
    {
        'author': 'Aske programmer',
        'title': 'Pierwszy post 1',
        'content': 'Zdelav Delo - gulaj smelo',
        'date_posted': '27 Jan 1988'
    },
    {
        'author': 'Tesla',
        'title': 'Drugi post 1',
        'content': 'A davajte zdelajem Cybertruck! =)',
        'date_posted': '21 Nov 2019'
    }
]
"""

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)  # inside blog/templates/blog/home.html


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  # inside blog/templates/blog/about.html, title: About is variable
