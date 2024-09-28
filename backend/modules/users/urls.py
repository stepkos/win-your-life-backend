from django.urls import path
from modules.users import views


urlpatterns = [
    path('api/user/friend', views.UserFriendsView.as_view()),
    path('api/user/profile', views.UserProfileView.as_view()),
    path('api/user', views.UserView.as_view()),
    path('api/user/info', views.UserInfoView.as_view()),
    path('api/user/streak', views.UserStreakView.as_view()),
]