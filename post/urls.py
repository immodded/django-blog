from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("posts/", views.PostlistView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(),name='post-detail'),
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/<slug:slug>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('post/<slug:slug>/comment/create', views.CommentCreate.as_view(), name='post-comment'),
    path('post/comment/reply/<int:pk>', views.ReplyCreate.as_view(), name='comment-reply'),
    path('post/comment/<int:pk>', views.CommentDetailView.as_view(), name='comment-detail'),
    


]
