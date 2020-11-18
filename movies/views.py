from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.models import MoviesModel
from movies.serializers import MoviesSerializer

@api_view(['GET', ])
def api_detail_movie_view(request, title):

	try:
		movie = MoviesModel.objects.filter(title__contains = title)
	except MoviesModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MoviesSerializer(movie, many=True)
		return Response(serializer.data)

@api_view(['GET', ])
def api_list_movie_view_rating(request, rating):

	try:
		movie = MoviesModel.objects.filter(rating__gte = rating)
	except MoviesModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MoviesSerializer(movie, many=True)
		return Response(serializer.data)

@api_view(['GET', ])
def api_list_movie_view_id(request, id):

	try:
		movie = MoviesModel.objects.get(id = id)
	except MoviesModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MoviesSerializer(movie)
		return Response(serializer.data)

@api_view(['GET', ])
def api_list_movie_view_genres(request, genres):

	try:
		movie = MoviesModel.objects.filter(genres__contains = genres)
	except MoviesModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MoviesSerializer(movie, many = True)
		return Response(serializer.data)
