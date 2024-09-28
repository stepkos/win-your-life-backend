from django.urls import path
from modules.users import views


urlpatterns = [
    path("user/friend/", views.UserFriendsView.as_view()),
    path("user/profile/", views.UserProfileView.as_view()),
    path("user/", views.UserView.as_view()),
    path("user/info/", views.UserInfoView.as_view()),
    path("user/streak/", views.UserStreakView.as_view()),
]
