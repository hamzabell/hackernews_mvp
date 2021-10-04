from django.urls import path
from .views import  PostDetail, PostList, UpVoteAPIView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('up-vote', UpVoteAPIView.as_view())
]
