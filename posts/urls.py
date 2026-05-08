from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Blog home page: list of posts
    path('', views.home, name='home'),

    # Blog detail page: single post
    path('<int:id>/', views.post_detail, name='post_detail'),
]
