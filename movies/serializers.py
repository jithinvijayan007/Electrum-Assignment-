from rest_framework import serializers
from movies.models import MoviesModel

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:

        model = MoviesModel
        fields = "__all__"
