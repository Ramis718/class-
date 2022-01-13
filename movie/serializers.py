from rest_framework import serializers
from .models import Genre, Movie, Rating



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genreinit
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'id text value'.split()       

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    # ratings = RatingSerializer(many=True)
    ratings = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id', 'name', 'genres', 'ratings', 'cout_genres', 'rating']

    def get_ratings(self, movie):
        # rate = movie.ratings.filter(value__gt=3)
        rate = Rating.objects.filter(movie=movie, value__gt=3)
        data = RatingSerializer(rate, many=True).data
        return data 

    def get_genres(self, movie):
        # filtared_genres = movie.genres.filter(is_active=True)
        # data = GenreSerializer(filtared_genres, many=True).data
        return GenreSerializer(movie.genres.filter(is_active=True), many=True).data

class MovieDatailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id', 'name', 'description', 'duration', 'cout_genres']       