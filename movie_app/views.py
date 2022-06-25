from django.shortcuts import render
from .models import Director, Movie, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import DirectorSerializer, DirectorDetailSerializer
from .serializer import MovieSerializer, MovieDetailSerializer
from .serializer import ReviewSerializer, ReviewDetailSerializer, ReviewRatingSerializer


@api_view(["GET"])
def directors_list_view(request):
    try:
        director = Director.objects.all()
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "not exist"})
    data = DirectorSerializer(director, many=True).data
    return Response(data=data)


@api_view(["GET"])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "not exist"})
    data = DirectorDetailSerializer(director, many=False).data
    return Response(data=data)


@api_view(["GET"])
def movies_list_view(requst):
    try:
        movie = Movie.objects.all()
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "not exist"})
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)


@api_view(["GET"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "not exist"})
    data = MovieDetailSerializer(movie, many=False).data
    return Response(data=data)


@api_view(["GET"])
def review_list_view(request):
    try:
        review = Review.objects.all()
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "not exist"})
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(["GET"])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND, data={"error": "list is empty"}
        )
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)


@api_view(["GET"])
def review_rating_view(request):
    try:
        review = Review.objects.all()
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND, data={"error": "Does not exists"}
        )
    data = ReviewRatingSerializer(review, many=True).data
    return Response(data=data)


# Create your views here.
