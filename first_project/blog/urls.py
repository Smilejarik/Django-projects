from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views  # import views.py from the current dir

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # '' empty so this blog is home page, views.home is function
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # '' empty so this blog is home page, views.home is function
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # '' empty so this blog is home page, views.home is function
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # '' empty so this blog is home page, views.home is function
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # '' empty so this blog is home page, views.home is function
    path('about/', views.about, name='blog-about'),  # 'about/' so about page, views.about function, /blog/about actually
]
