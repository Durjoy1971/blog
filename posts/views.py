from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

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

# Create new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'is_edit': False
    }
    return render(request, 'posts/post_form.html', context)

# Edit existing post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'is_edit': True,
        'post': post
    }
    return render(request, 'posts/post_form.html', context)
