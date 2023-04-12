from rest_framework import serializers
from .models import Movie, MovieOrder, RatingChoices
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
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def get_added_by(self, movie):
        return movie.user.email


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj):
        print(obj)
        return obj.movie.title

    def get_buyed_by(self, obj):
        # return obj.movie.user.email
        return obj.user.email

    def create(self, validated_data) -> MovieOrder:
        # return MovieOrder.objects.create(
        #     user=self.user, movie=self.movie, **validated_data
        # )
        return MovieOrder.objects.create(**validated_data)

    # def title(self):
    #     return self.title

    # def buyed_by(self):
    #     return self.buyed_by

    # def buyed_at(self):
    #     return self.buyed_at

    ...
