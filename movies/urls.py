from django.urls import path
from movies.views import(
	api_detail_movie_view,
    api_list_movie_view_rating,
    api_list_movie_view_id,
    api_list_movie_view_genres
)

app_name = 'movies'

urlpatterns = [
	path('search/title/<title>/', api_detail_movie_view, name="detail_name"),
    path('search/rating/<rating>/', api_list_movie_view_rating, name="detail_rating"),
    path('search/id/<id>/', api_list_movie_view_id, name="detail_id"),
    path('search/genres/<genres>/', api_list_movie_view_genres, name="detail_genres"),

]
