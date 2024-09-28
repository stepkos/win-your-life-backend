

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from modules.authentication import views

urlpatterns = [
    path('api/client', views.Profile.as_view()),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]