
from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path('news/', PostList.as_view(), name= 'post-list'),
    path('<int:pk>/', PostDetail.as_view(), name= 'post-detail'),
]