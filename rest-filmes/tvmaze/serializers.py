from tvmaze.models import *
from rest_framework import serializers
import requests

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['id', 'name', 'url']

    def create(self, validated_data):
        # get the list of todos
        response = requests.get('https://api.tvmaze.com/search/shows?q=star%20wars')
        # transfor the response to json objects
        validated_data = response.json()
        
        id = validated_data[5]['show']['id']
        url = validated_data[5]['show']['url']
        name = validated_data[5]['show']['name']

        import pdb
        pdb.set_trace()

        filme = Filmes.objects.create(id=id, url=url, name=name)
        filme.save()

        return Filmes.objects.create(**validated_data)