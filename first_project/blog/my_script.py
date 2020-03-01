from .models import Post
from django.contrib.auth.models import User

posts = Post.objects.all()
user = User.objects.first()

post_1 = Post(title='Blog 1', content='First Content here!', author=user)
post_1.save()
