from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# List of posts with id, title, and content
posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the content of the first post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the content of the second post.'},
    {'id': 3, 'title': 'Third Post', 'content': 'This is the content of the third post.'},
]

# Create your views here.
def post_list(request):
    html = '<h1>Blog Posts</h1><ul>'
    for post in posts:
        html += f'<li><a href="/posts/{post["id"]}/">{post["title"]}</a></li>'
    html += '</ul>'
    
    return HttpResponse(html)

def post_detail(request, id):
    post = next((post for post in posts if post['id'] == id), None)
    if post is None:
        return HttpResponseNotFound('<h1>Post not found</h1>')
    
    html = f'<h1>{post["title"]}</h1><p>{post["content"]}</p>'
    return HttpResponse(html)