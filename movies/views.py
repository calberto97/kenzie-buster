from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.permissions import IsEmployeeOrReadOnly
from movies.serializers import MovieSerializer


class MoviesView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, 200)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, 201)


class MovieView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, 200)

    def delete(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=204)
        ...
