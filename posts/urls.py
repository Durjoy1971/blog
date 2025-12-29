from django.urls import path
from . import views

urlpatterns = [
    # Blog home page: list of posts
    path('', views.post_list, name='post_list'),

    # Blog detail page: single post
    path('<int:id>/', views.post_detail, name='post_detail'),
]
