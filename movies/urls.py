from django.urls import path
from .views import MovieView, MoviesView, MovieOrderView
from rest_framework_simplejwt import views

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MovieView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view())
]
