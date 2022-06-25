from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = " id name ".split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "id title".split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "id text stars movie rating".split()
