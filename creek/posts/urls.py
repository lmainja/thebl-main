#posts/urls.py
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('coming/', views.coming_soon, name='coming'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('careers/', views.careers, name='careers'),
    path('team/', views.team, name='team'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]