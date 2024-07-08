from django.urls import path

from .views import PostList, PostRetrieveUpdateDestroy
urlpatterns = [
    path('post', PostList.as_view(), name='post_list'),
     path('post/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
]

