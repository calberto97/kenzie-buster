from rest_framework import serializers
from .models import Movie, RatingChoices
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, required=False, default=None
    )
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, required=False
    )
    synopsis = serializers.CharField(default=None, required=False)
    # user =
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def get_added_by(self, movie):
        return movie.user.email
