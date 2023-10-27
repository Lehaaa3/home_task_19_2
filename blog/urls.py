from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]