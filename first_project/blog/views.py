from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  # inside blog/templates/blog/about.html, title: About is variable
