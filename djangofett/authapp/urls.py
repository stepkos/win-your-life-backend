

from django.urls import path
from .views import Profile, Login, Register

urlpatterns = [
    path('api/client/<str:email>', Profile.as_view()),
    path('api/auth/register', Register.as_view()),
    path('api/auth/login', Login.as_view())
]