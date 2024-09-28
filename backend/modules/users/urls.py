




from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from modules.users import views

urlpatterns = [
    path('api/user/friend', views.UserFriendsView.as_view()),
    path('api/user/profile', views.UserProfileView.as_view()),
    path('api/user', views.UserView.as_view()),
]