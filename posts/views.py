from django.shortcuts import render, get_object_or_404
from .models import Post

# Detail view → single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)

# Home page view → list all posts from database
def home(request):
    all_posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': all_posts
    }
    return render(request, 'posts/post_list.html', context)
