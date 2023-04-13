from django.urls import path
from .views import UserView, UsersView
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/", UserView.as_view())
]
