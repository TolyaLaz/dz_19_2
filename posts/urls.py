from django.urls import path
from . import views
from catalog.apps import PostConfig

app_name = PostConfig.name

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='post_form'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
