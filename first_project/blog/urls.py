from django.urls import path
from . import views  # import views.py from the current dir

urlpatterns = [
    path('', views.home, name='blog-home'),  # '' empty so this blog is home page, views.home is function
    path('about/', views.about, name='blog-about'),  # 'about/' so about page, views.about function, /blog/about actually
]
