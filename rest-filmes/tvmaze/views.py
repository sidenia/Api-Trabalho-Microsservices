from django.shortcuts import render
from rest_framework import status, request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import requests
from tvmaze.models import *
from tvmaze.serializers import *

def home(request):
   # get the list of todos
   response = requests.get('https://api.tvmaze.com/search/shows?q=star%20wars')
   # transfor the response to json objects
   todos = response.json()
   context = {
      "todos": todos
   }
   return render(request, "../templates/home.html", context)

class filmesViewset(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Filmes.objects.all()
   serializer_class = FilmesSerializer
