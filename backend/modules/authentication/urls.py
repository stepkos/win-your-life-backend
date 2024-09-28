from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from modules.authentication import views

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path(
        "api/activation/<str:token_id>",
        views.ActivationView.as_view(),
        name="auth_activation",
    ),
]
