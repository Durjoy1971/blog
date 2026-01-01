from django.shortcuts import render
from django.http import Http404

# Temporary dummy data
POSTS = [
    {"id": 1, "title": "First Post", "content": "Hello Django"},
    {"id": 2, "title": "Second Post", "content": "Learning Templates"},
]

# Home page view → list all posts
def post_list(request):
    context = {"posts": POSTS}
    return render(request, 'posts/post_list.html', context)


# Detail view → single post
def post_detail(request, id):
    post = next((p for p in POSTS if p["id"] == id), None)
    if not post:
        raise Http404("Post not found")

    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)
